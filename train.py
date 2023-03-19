import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib
#Loading the Dataset
data = pd.read_csv(r'Reddit_Data.csv')


#Pre-Prcoessing and Bag of Word Vectorization using Count Vectorizer
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
text_counts = cv.fit_transform(data['clean_comment'].values.astype('U'))
# #Splitting the data into trainig and testing
X_train, X_test, Y_train, Y_test = train_test_split(text_counts, data['category'], test_size=0.2, random_state=10)
#Training the model
MNB = MultinomialNB()
MNB.fit(X_train, Y_train)

joblib.dump(MNB, "model")
joblib.dump(cv, "vectorizer")
