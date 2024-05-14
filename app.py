from flask import Flask, render_template
from flask import Flask, render_template, request
from utilities import translate_sequence

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_text = request.form['text']
    output_text = translate_sequence(input_text)
    return output_text

if __name__ == '__main__':
    app.run(debug=True)