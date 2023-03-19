import praw
import joblib

MNB = joblib.load("model")
cv = joblib.load("vectorizer")

def prediction(post):
    sentiment_lookup = {-1: "negative", 0: "neutral", 1: "positive"}
    count_text = cv.transform([post])
    predicted = MNB.predict(count_text)
    print(post, sentiment_lookup[predicted[0]])


reddit = praw.Reddit(
    client_id="vkehb98SP7DXk-zpouJJPg",
    client_secret="Mh9_kBMneiQyl-aqYIoP6rNTMxaf3A",
    user_agent="praw"
)
reddit.read_only = True

count = 0
for comment in reddit.subreddit('worldnews').stream.comments(skip_existing=True):
    prediction(comment.body)
    if count >= 5:
        break
    count += 1
