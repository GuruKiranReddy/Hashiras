
from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # point to home page and specify method get and post on homepage
def index():  # index page route to homepage , define what comes on homepage
    # return 'hello world and stuff'
    # get and post request - send information
    transcript = ""
    if request.method == 'POST':
        print('FORM DATA RECEIVED')

        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            print(transcript)
    return render_template('index.html',transcript=transcript)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)  # basic start flask syntax, both true debug command s the file falshk refresh
    # process multiple req at same time
'''

from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    
'''