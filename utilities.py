import re
import string
import pickle
from string import digits
from model import decode_sequence
from keras_preprocessing.sequence import pad_sequences

def translate_sequence(input_text):
    # define the constants variables
    exclude = set(string.punctuation)
    remove_digits = str.maketrans('', '', digits)
    with open('static/model_data/input_token_index.pickle', 'rb') as handle:
        input_token_index = pickle.load(handle)

    # Preprocess the input text
    input_text = input_text.lower()
    input_text = re.sub("'", '', input_text)
    input_text = ''.join(ch for ch in input_text if ch not in exclude)
    input_text = input_text.translate(remove_digits)
    input_text = input_text.strip()
    input_text = re.sub(" +", " ", input_text)

    # Tokenize the input text
    input_seq = []
    for word in input_text.split():
        if word in input_token_index:
            input_seq.append(input_token_index[word])
        else:
            input_seq.append(input_token_index.get('<UNK>', 0)) 

    # Pad the input sequence
    input_seq = pad_sequences([input_seq], maxlen=18, padding='post')

    decoded_sentence = decode_sequence(input_seq)

    return decoded_sentence[:-4]
