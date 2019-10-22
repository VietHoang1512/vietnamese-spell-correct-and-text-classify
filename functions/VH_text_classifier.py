from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
from sklearn import metrics,naive_bayes
from sklearn import preprocessing
from pyvi import ViTokenizer, ViPosTagger # thư viện NLP tiếng Việt chuyên để tiền xử lí
from gensim.utils import decode_htmlentities
import numpy as np
import gensim 
import os
stop_word = []
with open("vnstopword3.txt",encoding="utf-8") as f :
  text = f.read()
  text=text.replace(" ", "_")
  for word in text.split() :
      stop_word.append(word)
  del(word)
  f.close()

import pickle

X_data = pickle.load(open('x.pkl', 'rb'))
y_data = pickle.load(open('y.pkl', 'rb'))
categorize=['Chính trị-Xã hội', 'Đời sống', 'Khoa học', 'Kinh doanh', 'Pháp luật', 'Sức khoẻ', 'Thế giới', 'Thể thao', 'Văn hoá', 'Vi tính']

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
def BigClassifier(contents):
    input_ = []
    contents = gensim.utils.simple_preprocess(contents)
    contents = ' '.join(contents)
    contents = ViTokenizer.tokenize(contents)
    contents = contents.split()
    result  = [word for word in contents if word.lower() not in stop_word] 
    contents = ' '.join(result)
    input_.append(contents)
    X_data.append(input_[0])
    tfidf_vect = TfidfVectorizer(analyzer='word',max_features=7000, max_df=0.8, min_df=1)
    tfidf_vect.fit(X_data)

    X_data_tfidf =  tfidf_vect.transform(X_data)

    X_test_tfidf=X_data_tfidf[-1]
    X_data_tfidf=X_data_tfidf[0:6000] 
    feature=tfidf_vect.get_feature_names()
    encoder = preprocessing.LabelEncoder()
    y_data_n = encoder.fit_transform(y_data)
    classifier=naive_bayes.MultinomialNB()           
    classifier.fit(X_data_tfidf, y_data_n)
    test_predictions = classifier.predict(X_test_tfidf)[0]

    return (categorize[test_predictions])


