"""
Markov Chain 

To train on a text and generate a model, run: 
  $ python3 markov.py train text.txt model_name bucket_size

To generate text using a model, run:
  $ python3 markov.py generate model_name "prompt"
"""

import sys
import pickle
import random

WORD_CHARS = [',', '.', '!', '?', '"']

def extract_words(text):
    for word in WORD_CHARS:
        text = text.replace(word, ' '+word+' ')

    return list(filter(None, text.split()))

def train(text, bucket_size):
    """
    Given some text, returns a model dict
    """
    words = extract_words(text)
    model = {'bucket_size': bucket_size}

    for i in range(0, len(words)-bucket_size):
        key = tuple(words[i : i+bucket_size])

        if key not in model:
            model[key] = []
        
        model[key].append(words[i + bucket_size])

    return model
        
def generate(model, max_len, prompt):
    """
    Given a model dict and a prompt text, returns some text
    """
    bucket_size = model['bucket_size']
    words = extract_words(prompt)
    starting_words = words[-bucket_size:]
    text = prompt

    last_n_words = starting_words
    while len(text) < max_len:
        key = tuple(last_n_words)

        if (key not in model):
            break

        possible_words = model[key]
        next_word = random.choice(possible_words)
        text = text + ' ' + next_word
        last_n_words = last_n_words[1:]

        last_n_words.append(next_word)

        if key == tuple(last_n_words):
            break

    return text

def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

if __name__ == '__main__':
    args = sys.argv[1:]

    if args[0] == 'train':
        input_file_name, model_name, bucket_size_str = args[1:]
        bucket_size = int(bucket_size_str)
        
        with open(input_file_name, 'r') as in_file:
            text = in_file.read()
            model = train(text, bucket_size)

            save_obj(model, model_name)


    elif args[0] == 'generate':
        model_name, max_len_str, prompt = args[1:]
        model = load_obj(model_name)
        text = generate(model, int(max_len_str), prompt)
        
        print(text)
