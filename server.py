'''Server configuration where flash app is initialized and deployed.'''
# Importing required flask functions
from flask import Flask, request, render_template
# Importing emotion detector function from the package
from EmotionDetection.emotion_detection import emotion_detector
# Initializing the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    '''Function to handle the /emotionDetector app route. Returns the output provided 
    by the emotion detector module based on user input.'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is\
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}.\
     The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    '''Function to handle landing page, redirects to index.html template'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
