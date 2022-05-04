#Importar
from flask import Flask, render_template
#Importar
from flask import Flask, render_template


#Crear app medante instancia
app = Flask(__name__)


#Crear rutas con sus correspondientes funciones
#INICIO
@app.route('/', methods=['GET'])
def index():
    return render_template('/index.html')

#MIS PROYECTOS
@app.route('/mis-proyectos', methods=['GET'])
def mostrarproyectos():
    return render_template('mis-proyectos.html')

#MI BLOG
@app.route('/blog', methods=['GET'])
def blog():
    return render_template('/blog.html')

#CONTACTO
@app.route('/contacto', methods=['GET'])
def contacto():
    return render_template('/contacto.html')
#Ejecutar nuestra app cuando ejecutemos este archivo run.py

if __name__ == '__main__':
    app.run(debug=True)