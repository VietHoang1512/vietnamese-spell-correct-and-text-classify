from collections import Counter
from keras.models import load_model
from nltk.tokenize import word_tokenize
from nltk import ngrams,word_tokenize
import numpy as np
import re
import unidecode
import string
from tqdm import tqdm

import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

model = load_model("./spell.h5")
model._make_predict_function()



NGRAM=5
MAXLEN=40
alphabet = ['\x00', ' ', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'á', 'à', 'ả', 'ã', 'ạ', 'â', 'ấ', 'ầ', 'ẩ', 'ẫ', 'ậ', 'ă', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ', 'ó', 'ò', 'ỏ', 'õ', 'ọ', 'ô', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ơ', 'ớ', 'ờ', 'ở', 'ỡ', 'ợ', 'é', 'è', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'ú', 'ù', 'ủ', 'ũ', 'ụ', 'ư', 'ứ', 'ừ', 'ử', 'ữ', 'ự', 'í', 'ì', 'ỉ', 'ĩ', 'ị', 'ý', 'ỳ', 'ỷ', 'ỹ', 'ỵ', 'đ', 'Á', 'À', 'Ả', 'Ã', 'Ạ', 'Â', 'Ấ', 'Ầ', 'Ẩ', 'Ẫ', 'Ậ', 'Ă', 'Ắ', 'Ằ', 'Ẳ', 'Ẵ', 'Ặ', 'Ó', 'Ò', 'Ỏ', 'Õ', 'Ọ', 'Ô', 'Ố', 'Ồ', 'Ổ', 'Ỗ', 'Ộ', 'Ơ', 'Ớ', 'Ờ', 'Ở', 'Ỡ', 'Ợ', 'É', 'È', 'Ẻ', 'Ẽ', 'Ẹ', 'Ê', 'Ế', 'Ề', 'Ể', 'Ễ', 'Ệ', 'Ú', 'Ù', 'Ủ', 'Ũ', 'Ụ', 'Ư', 'Ứ', 'Ừ', 'Ử', 'Ữ', 'Ự', 'Í', 'Ì', 'Ỉ', 'Ĩ', 'Ị', 'Ý', 'Ỳ', 'Ỷ', 'Ỹ', 'Ỵ', 'Đ']
letters=list("abcdefghijklmnopqrstuvwxyzáàảãạâấầẩẫậăắằẳẵặóòỏõọôốồổỗộơớờởỡợéèẻẽẹêếềểễệúùủũụưứừửữựíìỉĩịýỳỷỹỵđABCDEFGHIJKLMNOPQRSTUVWXYZÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÉÈẺẼẸÊẾỀỂỄỆÚÙỦŨỤƯỨỪỬỮỰÍÌỈĨỊÝỲỶỸỴĐ")
accepted_char=list((string.digits + ''.join(letters)))

def extract_phrases(text):
    pattern = r'\w[\w ]*|\s\W+|\W+'
    return re.findall(pattern, text)

def encoder_data(text, maxlen=MAXLEN):
        text = "\x00" + text
        x = np.zeros((maxlen, len(alphabet)))
        for i, c in enumerate(text[:maxlen]):
            x[i, alphabet.index(c)] = 1
        if i < maxlen - 1:
          for j in range(i+1, maxlen):
            x[j, 0] = 1
        return x
      
def decoder_data(x):
    x = x.argmax(axis=-1)
    return ''.join(alphabet[i] for i in x)


def nltk_ngrams(words, n=5):
    return ngrams(words.split(), n)
      
def guess(ngram):
    text = ' '.join(ngram)
    preds = model.predict(np.array([encoder_data(text)]), verbose=0)
    return decoder_data(preds[0]).strip('\x00')

def correct(sentence):
    for i in sentence:
        if i not in accepted_char:
            sentence=sentence.replace(i," ")
    ngrams = list(nltk_ngrams(sentence, n=NGRAM))
    guessed_ngrams = list(guess(ngram) for ngram in ngrams)
    candidates = [Counter() for _ in range(len(guessed_ngrams) + NGRAM - 1)]
    for nid, ngram in (enumerate(guessed_ngrams)):
        for wid, word in (enumerate(re.split(' +', ngram))):
            candidates[nid + wid].update([word])
            
    output = ' '.join(c.most_common(1)[0][0] for c in candidates)  
    return output


r"""def accent_sentence(sentence):
  list_phrases = extract_phrases(sentence)
  in_put= word_tokenize(sentence)
  new_list_phrases=list(list_phrases)
  not_phrase=[]
  must_del=[]
  for i in range(len(new_list_phrases)):
    if len(new_list_phrases[i].split()) < 2 or not re.match("\w[\w ]+", new_list_phrases[i]):
        new_list_phrases[i-1]+=" "
        not_phrase.append(new_list_phrases[i])
        must_del.append(i)
  for k in must_del[::-1]:
    del new_list_phrases[k]
  new_text=" ".join(new_list_phrases)
  output = add_accent(new_text)
  out_put=word_tokenize(output)
  result=""
  j=0
  for i  in range(len(in_put)):
    if not re.match("\w[\w ]+", in_put[i]) and (len(in_put[i])!=1 or in_put[i] not in 'abcdefghijklmnopqrstuvwxyz'):
      result+=in_put[i]
    else:
      if j==len(out_put):
        break
      else :
        result+=out_put[j]+" "
        j+=1
  return result"""