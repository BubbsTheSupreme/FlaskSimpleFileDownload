from flask import url_for, render_template, send_file, current_app
from app import app
import os


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    folder = 'files\\'
    return send_file(folder + filename)
    