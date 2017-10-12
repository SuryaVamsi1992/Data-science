import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from nltk import RegexpTokenizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
data = pd.read_csv("https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/yelp.csv",header=0,encoding='utf8')
# data = data[data.stars.isin([1,5])]
token =RegexpTokenizer(r'\w+')
data['text'] = [' '.join(token.tokenize(i)) for i in data.text]
X = data.text.values
y = data.stars.values
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state = 42)
vect = CountVectorizer(stop_words='english')
X_train_dtm = vect.fit_transform(X_train).toarray()
X_test_dtm = vect.transform(X_test).toarray()
model = MultinomialNB()
model.fit(X_train_dtm,y_train)
y_pred = model.predict(X_test_dtm)
print metrics.accuracy_score(y_test,y_pred)
print metrics.confusion_matrix(y_test,y_pred)
print metrics.classification_report(y_test,y_pred)