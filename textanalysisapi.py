import os
from monkeylearn import MonkeyLearn

def get_sentiment(data):
    m = MonkeyLearn(os.environ.get('MONKEY_LEARN_API_KEY'))
    response = m.classifiers.classify(os.environ.get('MONKEY_LEARN_MODEL_ID'),data)
    return response.body