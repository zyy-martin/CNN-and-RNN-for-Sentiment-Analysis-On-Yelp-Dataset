import csv
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# nltk.download()

# stopwords_set = set(stopwords.words('english'))

train_X = []
train_Y = []
valid_X = []
valid_Y = []

with open('balanced_10k_train.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    i = 0
    for line in reader:
        if i == 0:
            i += 1
            continue
        train_X.append(line[5])
        train_Y.append(int(line[3]))

with open('balanced_4k_vali.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    i = 0
    for line in reader:
        if i == 0:
            i += 1
            continue
        valid_X.append(line[5])
        valid_Y.append(int(line[3]))


cv = CountVectorizer(max_features= 500)
features_train = cv.fit_transform(train_X)
features_valid = cv.transform(valid_X)

clf = GaussianNB()
clf.fit(features_train.toarray(), train_Y)
y_predict = clf.predict(features_valid.toarray())
print(accuracy_score(valid_Y, y_predict))
y_predict = clf.predict(features_train.toarray())
print(accuracy_score(train_Y, y_predict))



#
# valid_X_cleaned = []
# for review in valid_X:
#     tokenized = word_tokenize(review)
#     filtered = [w.lower() for w in tokenized if not w.lower() in stopwords_set]
#     valid_X_cleaned.append(filtered)
#
# print(valid_X_cleaned[0])