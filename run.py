#Importar
from flask import Flask

#Crear app medante instancia
app = Flask(__name__)

#Crear rutas con sus correspondientes funciones
@app.route('/', methods=['GET']) #Indicamos metodo GET
def holamundo():
    return 'Hola Mundo!'

@app.route('/mis-proyectos', methods=['GET'])
def mostrarproyectos():
    return 'Aquí se mostrarán mis proyectos'

#Ejecutar nuestra app cuando ejecutemos este archivo run.py

if __name__ == '__main__':
    app.run(debug=True)