from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectar con tu base de datos de 5 tablas
def conectar_db():
    # Asegúrate de que este nombre sea igual al de tu archivo .db
    conexion = sqlite3.connect('sistema_inscripcion.db') 
    conexion.row_factory = sqlite3.Row
    return conexion

# Función READ: Muestra los datos de los alumnos en la página web
@app.route('/')
def index():
    db = conectar_db()
    # Aquí le pedimos a la base de datos la lista de alumnos
    alumnos = db.execute('SELECT * FROM Alumnos').fetchall()
    db.close()
    return render_template('index.html', alumnos=alumnos)

# Función CREATE: Permite registrar un nuevo alumno desde la web
@app.route('/registrar', methods=['POST'])
def registrar():
    nombre_nuevo = request.form['nombre']
    db = conectar_db()
    db.execute('INSERT INTO Alumnos (nombre) VALUES (?)', (nombre_nuevo,))
    db.commit()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)