"""
This module defines a Flask web application for emotion detection.

It contains routes for rendering the home page and for handling
emotion analysis requests, using the emotion_detector function
from the EmotionDetection package.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle GET requests to the /emotionDetector endpoint.

    Extracts the 'textToAnalyze' parameter from the request, analyzes the text
    for emotions using the emotion_detector function, and returns a formatted
    response with the detected emotions. If the dominant emotion is None, 
    it returns an error message.

    Returns:
        str: A formatted string containing the emotion analysis results or an 
             error message if the input is invalid.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyse)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return formatted_response

@app.route('/')
def home():
    """
    Render the home page.

    Renders and returns the index.html template when a request is made
    to the root (/) endpoint.

    Returns:
        str: Rendered HTML content of the index.html template.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
