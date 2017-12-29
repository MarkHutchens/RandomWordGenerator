__author__ = 'mark'

from RWG.WordList import *
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pandas as pd
from RWG.matplothelper import *
from sklearn.model_selection import train_test_split

random.seed('Linguistics')

eng = WordList()
eng.create_list()
rand = WordList()
rand.create_random_list(eng)
print(len(rand.listOfStrings),len(eng.listOfStrings))

print(eng.listOfStrings[0:10], '\n', rand.listOfStrings[0:10])

length = 2000 #len(eng.listOfStrings)
combined = eng.listOfStrings[:2000] #Make it shorter for testing. SVM can't actually handle full length
combined.extend(rand.listOfStrings[:2000])

cv = CountVectorizer(analyzer='char',ngram_range=(1,2))
print('helloworld')
x = cv.fit_transform(combined)
x_arr = x.toarray()
x_arr_classes = [1] * length
x_arr_classes.extend([2] * length)

test_strings = [0] * len(x_arr)
for i in range(len(x_arr)): #To find out what was misclassified later
    test_strings[i] = x_arr[i][0]
    x_arr.itemset((i,0),i)   #Will keep track of the original places, we'll preserve the data in test_strings

print(x_arr[0])


eng_train, eng_test, eng_train_class, eng_test_class = train_test_split(x_arr, x_arr_classes, test_size=0.3, random_state=0)

for i in range(len(eng_test)):  #Removes the actual string, puts in external list
    temp = (eng_test[i][0])
    eng_test.itemset((i,0),test_strings[i])   #fixed now, eh?
    test_strings[i] = temp
add = len(eng_test)


for i in range(len(eng_train)):  #Removes the actual string, puts in external list
    j = i + add
    temp = (eng_train[i][0])
    eng_train.itemset((i,0),test_strings[j])    #fixed now, eh?
    test_strings[j] = temp

sc = StandardScaler()
sc.fit(eng_train)
eng_train_std = sc.transform(eng_train)
eng_test_std  = sc.transform(eng_test)
#print(eng_train_std)

df = pd.DataFrame(eng_train_std)
df.describe()

# The choice kernel='linear' is important.
svm = SVC(kernel='linear', C=1, random_state=0)
svm.fit(eng_train_std, eng_train_class)

eng_combined_std = np.vstack((eng_train_std, eng_test_std))
eng_class_combined = np.hstack((eng_train_class, eng_test_class))

ntest, nfeatures  = eng_train_std.shape
ntotal, nfeatures = eng_combined_std.shape
print(ntest, nfeatures, ntotal)

# Compute confusion matrix
y_pred = svm.predict(eng_test_std)
cm = metrics.confusion_matrix(eng_test_class, y_pred)
np.set_printoptions(precision=2)
print('Confusion matrix, without normalization')
print(cm)

# Normalize the confusion matrix by row (i.e by the number of samples
# in each class)
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print('Normalized confusion matrix: SVM')
print(cm_normalized)

to_print_fake = []
to_print_real = []
for i in range(len(y_pred)):
    #print out the text of the word that was misclassified
    if y_pred[i] != eng_test_class[i]:
        if eng_test_class[i] == 1:
            to_print_real.append(combined[test_strings[i]])
        else:
            to_print_fake.append(combined[test_strings[i]])
to_print_fake.sort()
to_print_real.sort()

print(to_print_fake)
print(to_print_real)