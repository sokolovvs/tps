from flask import Flask, jsonify, request
from bertopic import BERTopic
from settings import get_parameter_by_key
from services.client_service import ClientService

app = Flask(__name__)

topic_model = BERTopic()
topic_model.load("model")


@app.route('/topics')
def get_topics_by_text():
    try:
        ClientService.check_access(request=request.args)
    except Exception as e:
        return jsonify({"message": str(e)}), 403

    return jsonify(topic_model.find_topics(request.args.get("text")))


if __name__ == '__main__':
    app.run(host=get_parameter_by_key("TPS_HOST"),
            port=get_parameter_by_key("TPS_PORT"),
            debug=get_parameter_by_key("FLASK_DEBUG"))
