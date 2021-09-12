import os
from monkeylearn import MonkeyLearn

def get_sentiment(data):
    m = MonkeyLearn(os.environ.get('MONKEYLEARNAPIKEY'))
    response = m.classifiers.classify('cl_pi3C7JiL',data)
    return response.body