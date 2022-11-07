from flask import Flask

app = Flask(__name__)

@app.route('/') 
def inicio():
    return '<h1>Página principal, Bienvenidos</h1>'

@app.route('/articulos/') 
def articulos():
    return 'Lista de artículos'

@app.route('/acercade/') 
def acercade():
    return 'A cerca de.../'

@app.route('/pagina-html/')
@app.route('/pagina-html/<nombre>')
def pagina_html(nombre=''):
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Ejemplo HTML y flask</title>
    </head>
    <body>
        <h2>Hola {nombre}, Bienvenido/a</h2>
    </body>
    </html>
    '''

from flask import render_template, request
'''
Agregar a los usuarios la edad, luego renderizarlos en una tabla html, así:
    nombre      edad
    alicia      30
    beto        35
    carlos      40
    eva         45
'''
@app.route('/primer-template/')
def primer_template():
    usuarios = ['alicia:', 'beto', 'camila', 'diana']
    return render_template('primer-template.html', usuarios = usuarios)
'''
@app.route('/tabla-datos/')
def tabla_datos():
    infopersona = {
        'alicia':30,
        'beto': 35,
        'camila': 40,
        'diana': 45
    }
    return render_template('primer-template.html', infopersona = infopersona)
'''
@app.route('/persona/', methods=['GET', 'POST'])
def persona():
    if request.method=='POST':
        nombre = request.form['nombre']
        edad = request.form['edad']

        return render_template('persona.html', nombre=nombre, edad=edad)
    
    return render_template('persona.html')


if __name__ == "__main__":
    app.run()

    