from typing import Mapping


class TopicPredictorService:
    def __init__(self, topic_model) -> None:
        super().__init__()
        self.topic_model = topic_model

    def predict_topics(self, text: str) -> Mapping[str, int]:
        topic_ids, _ = self.topic_model.find_topics(text, top_n=1)

        return self.topic_model.get_topic(topic_ids[0])[0:10]
