from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/translate_eng_to_urdu', methods=['POST'])
def eng_to_urdu():
    pass

@app.route('/translate_eng_to_sindhi', methods=['POST'])
def eng_to_sindhi():
    pass

@app.route('/translate_eng_to_pashto', methods=['POST'])
def eng_to_pashto():
    pass

@app.route('/translate_eng_to_punjabi', methods=['POST'])
def eng_to_punjabi():
    pass

@app.route('/translate_urdu_to_eng', methods=['POST'])
def urdu_to_eng():
    pass

@app.route('/translate_sindhi_to_eng', methods=['POST'])
def sindhi_to_eng():
    pass

@app.route('/translate_pashto_to_eng', methods=['POST'])
def pashto_to_eng():
    pass

@app.route('/translate_punjabi_to_eng', methods=['POST'])
def punjabi_to_eng():
    pass

if __name__ == '__main__':
    app.run(debug=True)