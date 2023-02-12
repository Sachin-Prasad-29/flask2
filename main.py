from flask import Flask, jsonify,request
from youtube_transcript_api import YouTubeTranscriptApi
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/getcaption', methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        srt = YouTubeTranscriptApi.get_transcript(data["id"])
        # Do something with the received data
        return srt
    except Exception as e:
        return 'Error: {}'.format(str(e)), 404

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
