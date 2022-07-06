from flask import Flask, render_template, url_for, request, flash, redirect
from colorizers.siggraph17 import siggraph17
from server import colorize
from PIL import Image
from werkzeug.utils import secure_filename
import base64
import urllib.request
import os

app = Flask(__name__)
PHOTO_EXTENSION = set(['png', 'jpg', 'jpeg'])
def allowed_file(before):
    return '.' in before and before.rsplit('.', 1)[1].lower() in PHOTO_EXTENSION

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def upload_photo():
    if file.filename == "":
        flash("Please upload a photo.")
        return redirect(request.url)
    file = request.files["file"]
    if allowed_file(file.filename) and file:
        before = secure_filename(file.filename)
        path = os.path.join(app.config["static/images/"], before)
        file.save(path)
        flash("Photo is now ready to be colorized.")
        return render_template("index.html", filename=before, base64=colorize(path))
    else:
        flash("Please only upload png or jpg files.")
        return redirect(request.url)

if __name__ == "___main__":
    app.run(debug=True)
    app.debug=True