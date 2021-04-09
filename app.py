from bertopic import BERTopic
from flask import Flask, jsonify, request

from exceptions.access_denied_exception import AccessDeniedException
from services.client_service import ClientService
from services.topic_predictor_service import TopicPredictorService
from settings import get_parameter_by_key

app = Flask(__name__)
topic_model = BERTopic(language="multilingual")
topic_model.load("model")


@app.route('/api/v1/topics')
def get_topics_by_text():
    req = {"public_id": request.headers.get('TPS_PUBLIC_ID', ""),
           "secret": request.headers.get("TPS_SECRET_KEY", ""),
           "text": request.args.get("text", "")}

    try:
        ClientService.check_access(request=req)
        tps = TopicPredictorService(topic_model=topic_model)

        return jsonify(tps.predict_topics(text=req["text"]))
    except AccessDeniedException as e:
        return jsonify({"message": str(e)}), 403
    except Exception:
        return jsonify({"message": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(host=get_parameter_by_key("TPS_HOST"),
            port=get_parameter_by_key("TPS_PORT"),
            debug=get_parameter_by_key("FLASK_DEBUG"))
