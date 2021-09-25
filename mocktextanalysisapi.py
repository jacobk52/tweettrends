def mock_get_sentiment(data):
    return [{'classifications':[{'tag_name':'Positive'}]}]*len(data)
