from flask import Flask, render_template, request, redirect, session, url_for, flash # config
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'syntax'
app.config['MYSQL_PASSWORD'] = 'syntax'
app.config['MYSQL_DB'] = 'mensajito'
mysql = MySQL(app)

app.secret_key = 'mysecretkey'

@app.route('/')#Ruta para el home signup
def index():
   return render_template('index.html')
      
@app.route('/add_message', methods= ['POST']) #Añadir usuarios en el formulario
def add():
   if request.method == 'POST':
      nombre = request.form ['nombre']
      mensaje = request.form ['mensaje']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO formulario (nombre, mensaje) VALUES (%s, %s)', (nombre, mensaje))
      mysql.connection.commit()
      flash('Gashas pol el menchajito :3')
      return redirect('/')

@app.route('/subidos') #Mostrar los datos de usuarios en la tabla 
def mostrar_mensajes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM formulario')
    datos = cur.fetchall()
    print('datos')
    return render_template('subidos.html', mensaje = datos)

if __name__=='__main__':
 app.run(debug=True)
