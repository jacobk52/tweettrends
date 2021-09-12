import os
from monkeylearn import MonkeyLearn

def get_sentiment(data):
    m = MonkeyLearn(os.environ.get('MONKEYLEARNAPIKEY'))
    response = m.classifiers.classify(os.environ.get('MONKEYLEARNMODELID'),data)
    return response.body