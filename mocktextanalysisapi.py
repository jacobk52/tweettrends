def mock_get_sentiment(data):
    return [{'classifications':[{'tag_name':'Positive'}]}]*len(data)

def mock_extract_keywords(data):
    return ['test']*len(data)
