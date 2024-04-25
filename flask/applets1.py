from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una ruta y una función de vista
@app.route('/')
def hello_world():
    return '¡Hola, mundo! Esta es mi primera aplicación web con Flask.'

# Ejecuta la aplicación si este archivo es el punto de entrada
if __name__ == '__main__':
    app.run(debug=True)