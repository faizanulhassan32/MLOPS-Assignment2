import praw
import joblib
import json

MNB = joblib.load("model")
cv = joblib.load("vectorizer")

def prediction(comment):
    sentiment_lookup = {-1: "negative", 0: "neutral", 1: "positive"}
    count_text = cv.transform([comment.body])
    predicted = MNB.predict(count_text)
    output = {"Title": comment.submission.title, "Comment": comment.body, "Prediction": sentiment_lookup[predicted[0]]}
    print(json.dumps(output, indent=4))


reddit = praw.Reddit(
    client_id="vkehb98SP7DXk-zpouJJPg",
    client_secret="Mh9_kBMneiQyl-aqYIoP6rNTMxaf3A",
    user_agent="praw"
)
reddit.read_only = True

count = 0
for comment in reddit.subreddit('worldnews').stream.comments(skip_existing=True):
    prediction(comment)
    if count >= 5:
        break
    count += 1
