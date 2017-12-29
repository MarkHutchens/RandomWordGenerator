__author__ = 'mark'

#from sklearn.feature_extraction.text import *
from sklearn.feature_extraction.text import CountVectorizer
import csv
import random
import string

class WordList(object):
    def __init__(self):
        cv = CountVectorizer()
        self.listOfStrings = []
        #listOfRandom = []

    def create_list(self,path='./EOWL-v1.1.2/CSV Format/',filelist=' Words.csv'):
        #Make a wordlist from a dictionary folder.
        for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            #Values
            with open(path + c + filelist, 'rt') as csvfile:
                csvr = csv.reader(csvfile)
                for i in csvr:
                    self.listOfStrings.append(i[0])
        random.shuffle(self.listOfStrings)

    def create_random_list(self,to_match):
        #Make a random string of the same length for each word in the nonrandom wordlist
        for i in to_match.listOfStrings:
            length = len(i)
            s = ''.join(random.choice(string.ascii_lowercase) for c in range(length))
            self.listOfStrings.append(s)
        random.shuffle(self.listOfStrings)  #lengths are nonrandom, so not wholly meaningless

if __name__ == "__main__":
    eng = WordList()
    eng.create_list()
    rand = WordList()
    rand.create_random_list(eng)
    print(len(rand.listOfStrings),len(eng.listOfStrings))

    test_set_real = eng.listOfStrings[:1000]
    test_set_rand = rand.listOfStrings[:1000]
    del eng.listOfStrings[:1000]
    del rand.listOfStrings[:1000]
    print(eng.listOfStrings[0:10], '\n', rand.listOfStrings[0:10])

    #vocabulary is just letters. Again, since I'm doing word-recognition and not sentence-level.
    cv = CountVectorizer(analyzer='char',ngram_range=(1,2))
    print('helloworld')
    x = cv.fit_transform(eng.listOfStrings)
    print(x)
    print(x.toarray())

    print(cv)


#cv._char_ngrams(csvr)
#X_train_counts = cv.fit_transform()