import os
from monkeylearn import MonkeyLearn

monkey_learn_api_key=os.environ.get('MONKEY_LEARN_API_KEY')
monkey_learn_model_id=os.environ.get('MONKEY_LEARN_MODEL_ID')

def get_sentiment(data):
    m = MonkeyLearn(monkey_learn_api_key)
    response = m.classifiers.classify(monkey_learn_model_id, data)
    return response.body