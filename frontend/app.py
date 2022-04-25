from webbrowser import get
from flask import Flask, Request, render_template
from flask import request
import requests


app = Flask (__name__)
@app.route('/')
def index():
    return ("Principal")

@app.route('/clientes')
def mostrarclientes():
    mostrarclientes=requests.get("http://127.0.0.1:8000/clientes").json()

    return render_template("mostrarclientes.html",mostrarclientes=mostrarclientes)

@app.route('/productos')
def mostrarproductos():
    mostrarproductos=requests.get("http://127.0.0.1:8000/productos").json()

    return render_template("mostrarproductos.html",mostrarproductos=mostrarproductos)
if __name__ == '__main__':
    app.run(debug=True, port=9000)