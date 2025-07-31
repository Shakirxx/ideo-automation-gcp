from flask import Flask, render_template, request, send_file
from utils.voiceover import generate_voiceover
from utils.images import generate_images
from utils.captions import generate_captions
from utils.render import render_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        script_text = request.form["script"]
        voice_file = generate_voiceover(script_text)
        captions_file = generate_captions(script_text, voice_file)
        images = generate_images(script_text)
        output_path = render_video(images, voice_file, captions_file)
        return send_file(output_path, as_attachment=True)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

