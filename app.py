from flask import Flask, render_template
from flask import request
from TuclaseExamen import TuclaseExamen
from pytest import main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("formulario.html")

@app.route("/resolver", methods=["POST"])
def result():
    operaciones = request.form["operaciones"]
    operaciones = operaciones.split(",")
    resultado = TuclaseExamen.arithmetic_arranger(operaciones, mostrarRespuesta=True)
    test = main(['-vv'])
    return render_template("resultados.html", resultado=resultado, test=test)

if __name__ == "__main__":
    app.run(debug=True, port=3000)