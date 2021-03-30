from flask import Flask, jsonify, request
from settings import get_parameter_by_key
from services.client_service import ClientService
from exceptions.access_denied_exception import AccessDeniedException
from bertopic import BERTopic

app = Flask(__name__)
topic_model = BERTopic()
topic_model.load("model")


@app.route('/api/v1/topics')
def get_topics_by_text():
    req = {"public_id": request.headers.get('TPS_PUBLIC_ID', ""),
           "secret": request.headers.get("TPS_SECRET_KEY", ""),
           "text": request.args.get("text", "")}

    try:
        ClientService.check_access(request=req)
    except AccessDeniedException as e:
        return jsonify({"message": str(e)}), 403
    except Exception as e:
        return jsonify({"message": str(e)}), 500

    return jsonify(topic_model.find_topics(request.args.get("text")))


if __name__ == '__main__':
    import logging

    logging.basicConfig(filename='error.log', level=logging.DEBUG)

    app.run(host=get_parameter_by_key("TPS_HOST"),
            port=get_parameter_by_key("TPS_PORT"),
            debug=get_parameter_by_key("FLASK_DEBUG"))
