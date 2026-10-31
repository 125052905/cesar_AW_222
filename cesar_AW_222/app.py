from flask import Flask, render_template, request, redirect, url_for, session
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
            session["rol"] = usuario[6]

            if session["rol"] == "Administrador":
                return redirect(url_for("admin"))

            return redirect(url_for("usuario"))

        return render_template(
            "login.html",
            error="Correo o contraseña incorrectos"
        )
        
    return render_template("login.html")

@app.route("/admin")
def admin():
    if "id_usuario" not in session:
        return redirect(url_for("login"))
        
    if session.get("rol") != "Administrador":
        return "Acceso denegado"
    return render_template("administrador.html")
    


@app.route("/usuario")
def usuario():
    if "id_usuario" not in session:
        return redirect(url_for("login"))
            
    if session.get("rol") != "Usuario":
        return "Acceso denegado"

    return render_template("usuario.html", nombre=session["nombre"])

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
    
@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nombre = request.form["nombre"]
        apellido_p = request.form["apellido_p"]
        apellido_m = request.form["apellido_m"]
        correo = request.form["correo"]
        
        password_hash = request.form["password"] 
        
        id_rol = request.form["id_rol"]

        password = generate_password_hash(password_hash)

        cursor = mysql.connection.cursor()

      
        consulta = "INSERT INTO usuarios (nombre, apellido_p, apellido_m, correo, password_hash, id_rol) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido_p, apellido_m, correo, password, id_rol)
        cursor.execute(consulta, valores)

       
        mysql.connection.commit()
        
        cursor.close()
        
      
        return redirect("/")
        
    return render_template("registro.html")
if __name__ == "__main__":
    app.run(debug=True)