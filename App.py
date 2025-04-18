# Definición de la API e implementación de los endpoints

#  Tener en cuenta Flask para crear la API.

from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    data = request.get_json()
    cantidad = int(data['cantidad'])

    resultados = {}

    try:
        subprocess.run(['python', 'Algorithms/Algoritmo_1.py', str(cantidad)], check=True)
        resultados['Algoritmo_1'] = "Cadenas generadas correctamente."

        with open('String.txt', 'r', encoding='utf-8') as f:
            resultados['Cadenas_generadas'] = f.read()
    except Exception as e:
        resultados['Algoritmo_1'] = f"Error: {str(e)}"
        return jsonify(resultados), 500

    try:
        subprocess.run(['python', 'Algorithms/Algoritmo_2.py'], check=True)
        resultados['Algoritmo_2'] = "Cadenas evaluadas correctamente."

        with open('AcceptedStrings.txt', 'r', encoding='utf-8') as f:
            resultados['Cadenas_aceptadas'] = f.read()
    except Exception as e:
        resultados['Algoritmo_2'] = f"Error: {str(e)}"
        return jsonify(resultados), 500

    try:
        subprocess.run(['python', 'Algorithms/Algoritmo_3.py'], check=True)
        resultados['Algoritmo_3'] = "Árboles de configuración generados correctamente."

        with open('config_trees.txt', 'r', encoding='utf-8') as f:
            resultados['Arboles_configuracion'] = f.read()
    except Exception as e:
        resultados['Algoritmo_3'] = f"Error: {str(e)}"
        return jsonify(resultados), 500

    return jsonify(resultados), 200

if __name__ == '__main__':
    app.run(debug=True)