import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL

app= Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]= True

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud_calificaciones'
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    con = mysql.connection.cursor()
    con.execute('SELECT * FROM tb_calificaciones')
    conCalificaciones = con.fetchall()
    return render_template('index.html', listCalificaciones=conCalificaciones)

@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method=='POST':
        matricula=request.form['txtMatricula']
        alumno=request.form['txtAlumno']
        calificacion=request.form['txtCalificacion']
        con=mysql.connection.cursor()
        con.execute('INSERT INTO tb_calificaciones (matricula, alumno, calificacion) VALUES (%s, %s, %s)', (matricula, alumno, calificacion))
        mysql.connection.commit()
        flash('!La Calificacion fue agregada correctamente!')
        return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    con =mysql.connection.cursor()
    con.execute('SELECT * FROM tb_calificaciones WHERE id=%s',(id))
    consultarId= con.fetchone()
    con.close()
    return render_template('editarCalificaciones.html',Calificacion=consultarId)

@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        matricula = request.form['txtMatricula']
        alumno = request.form['txtAlumno']
        calificacion = request.form['txtCalificacion']
        
        con = mysql.connection.cursor()
        con.execute('UPDATE tb_calificaciones SET matricula=%s, alumno=%s, calificacion=%s WHERE id=%s', (matricula, alumno, calificacion, id))
        mysql.connection.commit()
        
        flash('Se actualizó la calificación del alumno ' + alumno)
        return redirect(url_for('index'))

@app.route('/eliminar/<int:id>',methods=['POST'])
def eliminar(id):
    if request.method =='POST':
        con =mysql.connection.cursor()
        con.execute('DELETE FROM tb_calificaciones WHERE id=%s',(id))
        mysql.connection.commit()
        flash('se elimino el registro correctamente')
        return redirect(url_for('index'))
    
if __name__ == '__main__':
 app.run(debug=True)
