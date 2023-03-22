import praw
import joblib
import json
import time
from flask import Flask, render_template,request

app = Flask(__name__)

MNB = joblib.load("model")
cv = joblib.load("vectorizer")

def predict_sentiment(comment):
    sentiment_lookup = {-1: "negative", 0: "neutral", 1: "positive"}
    count_text = cv.transform([comment.body])
    predicted = MNB.predict(count_text)
    return sentiment_lookup[predicted[0]]

@app.route('/')
def index():
    reddit = praw.Reddit(
        client_id="vkehb98SP7DXk-zpouJJPg",
        client_secret="Mh9_kBMneiQyl-aqYIoP6rNTMxaf3A",
        user_agent="praw"
    )
    reddit.read_only = True

    data = []
    count = 0
    for comment in reddit.subreddit('all').stream.comments(skip_existing=True):
        prediction = predict_sentiment(comment)
        data.append({"title": comment.submission.title, "comment": comment.body, "prediction": prediction})
        count += 1
        if count >= 10:
            break

    while True:
        time.sleep(10)
        for comment in reddit.subreddit('all').stream.comments(skip_existing=True):
            prediction = predict_sentiment(comment)
            data.append({"title": comment.submission.title, "comment": comment.body, "prediction": prediction})
            data = data[-10:] # keep only the last 10 comments
            break
        else:
            continue
        break

    return render_template('index.html', data=data)

def predict_comment(comment):
    sentiment_lookup = {-1: "negative", 0: "neutral", 1: "positive"}
    count_text = cv.transform([comment])
    predicted = MNB.predict(count_text)
    return sentiment_lookup[predicted[0]]


@app.route('/search', methods=['POST'])
def search():
    comment = request.form['query']
    prediction = predict_comment(comment)
    data = [{"title":"Users comment","comment": comment, "prediction": prediction}]
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()
