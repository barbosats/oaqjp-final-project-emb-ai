from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    text_to_analyze = request.form['text']
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)    