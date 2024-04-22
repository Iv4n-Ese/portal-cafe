from flask import Flask, render_template, redirect, url_for

app = Flask (__name__, template_folder="templates")



@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/precios')
def Precios():
    return render_template('precios.html')

@app.route('/ofertas')
def Ofertas():
    return render_template('ofertas.html')

@app.route('/catalogo')
def Catalogos():
    return render_template('catalogo.html')

@app.route('/contacto')
def Contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(port = 3030, debug = True)