import nltk 
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


import numpy
import tflearn
import tensorflow
import random

import json
with open('data/basic_ecom.json') as file :
    data = json.load(file)
    
    
words = []
labels = []
x = []
y = []

for user in data['users']:
    for pattern in user['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        x.append(wrds)
        y.append(user['tag'])
    
    if user['tag'] not in labels:
        labels.append(user['tag'])
        

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, i in enumerate(x):
    bag= []
    
    wrds = [stemmer.stem(w.lower()) for w in i]
    
    for w in words:
        if w in wrds:
            bag.append(1)
        else:
            bag.append(0)
            
    output_row = out_empty[:]
    output_row[labels.index(y[x])] = 1
    
    training.append(bag)
    output.append(output_row)
    
training = numpy.array(training)
output = numpy.array(output)

tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]

        for tg in data["users"]:
            if tg['tag'] == tag:
                responses = tg['responses']

        print(random.choice(responses))

chat()