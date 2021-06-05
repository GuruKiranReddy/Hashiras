from flask import Flask, render_template, request ,redirect
import speech_recognition as sr
import pyaudio
import pyttsx3

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    command = ""
    if request.method == 'POST':
        if request.form.get('action1') == 'Tap to Speak':
            listener = sr.Recognizer()
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    print(command)
            except:
                pass
        if request.form.get('action2') == 'Resubmit':
            return redirect(request.url)
        elif request.method == "GET":
            return render_template("index1.html", command = command)
    # return command
    print(command)
    return render_template("index1.html", command=command)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
