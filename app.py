# app.py
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Directory where text files are stored
TEXT_FILES_DIR = 'files'

@app.route('/')
def index():
    # List all text files in the directory
    files = [f for f in os.listdir(TEXT_FILES_DIR) if f.endswith('.txt')]
    return render_template('index.html', files=files)

@app.route('/read-file', methods=['POST'])
def read_file():
    filename = request.json.get('filename')
    try:
        file_path = os.path.join(TEXT_FILES_DIR, filename)
        with open(file_path, 'r') as file:
            content = file.read()
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/save-file', methods=['POST'])
def save_file():
    filename = request.json.get('filename')
    content = request.json.get('content')
    try:
        file_path = os.path.join(TEXT_FILES_DIR, filename)
        with open(file_path, 'w') as file:
            file.write(content)
        return jsonify({'message': 'File saved successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)