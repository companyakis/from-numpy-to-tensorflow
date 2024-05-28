#print(raw_data.sentiment.unique()) # ['positive' 'negative']

sentiments = {"negative": 0, "positive": 1}

raw_data["sentiment_encoded"] = raw_data["sentiment"].map(sentiments)

print(raw_data[["sentiment", "sentiment_encoded"]].head())

"""
  sentiment  sentiment_encoded
0  positive                  1
1  positive                  1
2  positive                  1
3  negative                  0
4  positive                  1

"""
