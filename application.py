from flask import Flask, render_template, request

from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        uploaded_file = upload(request.files['image_file'])
        image_url, options = cloudinary_url(uploaded_file['public_id'], format="jpg", width="100", height="100")
        return render_template("success.html", image_url=image_url)