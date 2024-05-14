from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate_eng_to_urdu', methods=['POST'])
def eng_to_urdu():
    pass

if __name__ == '__main__':
    app.run(debug=True)