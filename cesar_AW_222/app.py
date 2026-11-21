from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flasktiid'
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

# INICIO DE SESIÓN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        correo_form = request.form["correo"]
        password_form = request.form["password"]

        cursor = mysql.connection.cursor()
        sql = """
        SELECT 
            usuarios.id,
            usuarios.nombre,
            usuarios.apellido_p,
            usuarios.apellido_m,
            usuarios.correo,
            usuarios.password_hash,
            usuarios.id_rol,
            roles.nombre
        FROM usuarios
        INNER JOIN roles
            ON usuarios.id_rol = roles.id_rol
        WHERE usuarios.correo = %s
        """

        cursor.execute(sql, (correo_form,))
        usuario = cursor.fetchone()
        cursor.close()

        if usuario and check_password_hash(usuario[5], password_form):
            session["id_usuario"] = usuario[0]
            session["nombre"] = usuario[1]
            session["id_rol"] = usuario[6]
            session["rol"] = usuario[7]

            if session["id_rol"] == 1:
                return redirect(url_for("admin"))

            return redirect(url_for("usuario"))

        return render_template(
            "login.html",
            error="Correo o contraseña incorrectos"
        )
        
    return render_template("login.html")


# PANEL DE ADMINISTRADOR
@app.route("/admin")
def admin():
    if "id_usuario" not in session:
        return redirect(url_for("login"))

    if session.get("id_rol") != 1:
        return "Acceso denegado", 403

    con = mysql.connection.cursor()
    con.execute("""
        SELECT usuarios.id,
               usuarios.nombre,
               usuarios.apellido_p,
               usuarios.apellido_m,
               usuarios.correo,
               roles.nombre
        FROM usuarios
        INNER JOIN roles
            ON usuarios.id_rol = roles.id_rol
    """)

    conUsuarios = con.fetchall()
    con.close()

    return render_template(
        "administrador.html",
        nombre=session["nombre"],
        listUsers=conUsuarios
    )


# PANEL DE USUARIO
@app.route("/usuario")
def usuario():
    if "id_usuario" not in session:
        return redirect(url_for("login"))
            
    if session.get("id_rol") != 2:
        return "Acceso denegado", 403

    return render_template("usuario.html", nombre=session["nombre"])


# CERRAR SESIÓN
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# REGISTRO DE USUARIOS
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        password = request.form["password"]
        id_rol = int(request.form.get("id_rol", 2))

        con = mysql.connection.cursor()

        # Comprobar si el correo ya existe
        con.execute(
            "SELECT id FROM usuarios WHERE correo = %s",
            (correo,)
        )

        if con.fetchone():
            con.close()
            flash("El correo ya está registrado")

            if session.get("id_rol") == 1:
                return redirect(url_for("admin"))

            return redirect(url_for("registro"))

        # Generar hash de contraseña
        password_hash = generate_password_hash(password)

        # Insertar usuario
        con.execute("""
            INSERT INTO usuarios
            (nombre, apellido_p, apellido_m, correo, password_hash, id_rol)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            nombre,
            apellido_p,
            apellido_m,
            correo,
            password_hash,
            id_rol
        ))

        mysql.connection.commit()
        con.close()

        flash("El usuario fue agregado correctamente")

        if session.get("id_rol") == 1:
            return redirect(url_for("admin"))

        return redirect(url_for("login"))

    return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug=True)