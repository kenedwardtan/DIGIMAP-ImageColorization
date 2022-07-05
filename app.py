from flask import Flask, render_template, url_for, request, flash, redirect
from colorizers.siggraph17 import siggraph17
from server import colorize
from PIL import Image
from werkzeug.utils import secure_filename
import base64
import urllib.request
import os

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')
