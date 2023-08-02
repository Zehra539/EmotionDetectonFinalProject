"""
This is a Flask application for Emotion Detection.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This function calls the application '''
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_predictor(text_to_analyze)

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return f"For the given statement, the system response is {dominant_emotion} and " \
           f"The dominant emotion is {dominant_emotion['dominant_emotion']}"
@app.route("/")
def render_index_page():
    ''' This is the function to render the html interface '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
