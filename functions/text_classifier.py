from pyvi import ViTokenizer, ViPosTagger # thư viện NLP tiếng Việt
from tqdm import tqdm
import numpy as np
import gensim # thư viện NLP
import os 
from sklearn import preprocessing

stop_words = []
with open("vietnamese-stopwords-dash.txt",encoding="utf-8") as f :
  text = f.read()
  text=text.replace(" ", "_")
  for word in text.split() :
      stop_words.append(word)
  del(word)
  f.close()
def get_data(contents):
    contents = gensim.utils.simple_preprocess(contents)
    contents = ' '.join(contents)
    contents = ViTokenizer.tokenize(contents)
    contents = contents.split()
    result  = [word for word in contents if word.lower() not in stop_words] 
    contents = ' '.join(result)
        
    return contents

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
tfidf_vect = pickle.load(open("Model/Model/vectorizer.pickle", "rb"))
svd = pickle.load(open("Model/Model/selector.pickle", "rb"))
from keras.models import model_from_json
json_file = open('Model/Model/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()


loaded_model = model_from_json(loaded_model_json)
# load weights int|o new model
loaded_model.load_weights("Model/Model/model.h5")
encoder = preprocessing.LabelEncoder()
encoder.classes_ = np.load('Model/Model/classes.npy')
loaded_model._make_predict_function()

def BigClassifier(content):
    categorize=['Chính trị-Xã hội', 'Đời sống', 'Khoa học', 'Kinh doanh', 'Pháp luật', 'Sức khoẻ', 'Thế giới', 'Thể thao', 'Văn hoá', 'Vi tính']
    x=get_data(content)
    x=[x]
    tfidf_x = tfidf_vect.transform(x)
    tfidf_x_svd = svd.transform(tfidf_x)
    return categorize[np.argmax(loaded_model.predict(np.array(tfidf_x_svd)))]
