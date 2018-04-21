import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
from nltk import RegexpTokenizer,word_tokenize
from sklearn.preprocessing import Imputer,StandardScaler
from sklearn.tree import DecisionTreeClassifier
from nltk.corpus import stopwords
import StringIO
data = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/sms_spam.csv',encoding='utf8')
token = RegexpTokenizer(r'\w+')
stop_words = set(stopwords.words('english'))
data['text'] = data['text']
data['text'] = [set(token.tokenize(i)) for i in data.text]
data['text'] = [" ".join(word) for word in data.text]
data['type'] = data['type'].map({'ham':0,'spam':1}) 
X = data.text
y = data.type
data.head()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2)
vect = CountVectorizer(stop_words='english')
X_train_dtm = vect.fit_transform(X_train)
X_test_dtm = vect.transform(X_test)
linreg = DecisionTreeClassifier()
linreg.fit(X_train_dtm,y_train)
y_pred = linreg.predict(X_test_dtm)
print metrics.confusion_matrix(y_test,y_pred)
print metrics.accuracy_score(y_test,y_pred)

temp = []
for i in range(len(df)):
    value = list(df.loc[i,:])[0]
    value = value.split(",")
    print (len(value))
    value[0] = value[0][1:]
    value[-1] = value[0][:-1]
    for j in range(len(value)):
        value[j] = value[j][2:-1]
        value[j] = value[j].split(":")
        temp.append(value[j][0])
dataframe = pd.DataFrame(temp)
dataframe.columns = ['Name']
print (len(dataframe))
