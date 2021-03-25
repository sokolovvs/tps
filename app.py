from flask import Flask
from flask import request
from bertopic import BERTopic
import json

app = Flask(__name__)

topic_model = BERTopic()
topic_model.load("model")


@app.route('/topics')
def get_topics_by_text():

    return json.dumps(topic_model.find_topics(request.args.get("text")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
