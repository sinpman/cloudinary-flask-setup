from flask import Flask, render_template, request

import cloudinary

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        uploaded_file = cloudinary.uploader.upload(request.files['image_file'])
        image_url = cloudinary.utils.cloudinary_url(uploaded_file['public_id'], format="jpg", width="100", height="100")
        return render_template("success.html", image_url=image_url)