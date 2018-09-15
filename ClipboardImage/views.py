from flask import render_template, send_file,request
import os
import sys
from urllib.parse import unquote

from . import app


@app.route('/')
def index():
    return render_template('index.html', imagePath=os.getenv('DESTINATION', 'image/'))


@app.route('/images')
def get_image():
    return send_file(os.path.abspath(unquote(request.args.get('filename'))))
