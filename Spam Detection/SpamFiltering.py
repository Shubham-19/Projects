import os
import codecs
from collections import Counter
import _pickle as cPickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

def save(clf, name):
	with open(name, 'wb') as fp:
		cPickle.dump(clf, fp)
	print("Saved")

def Dictionary():
	files = os.listdir('Emails/')
	Emails = ['Emails/' + email for email in files]
	words = []
	c = len(Emails)
	for email in Emails:
		f = codecs.open(email, 'r', encoding = 'utf-8', errors = 'ignore')
		words += f.read().split(" ")

		for i in range(len(words)):
			if not (words[i].isalpha()):
				words[i] = ""

		print(c)
		c -= 1
	dictionary = Counter(words)
	del dictionary[""]
	return dictionary.most_common(3000)

# making data suitable to apply a ML algorithm
def dataset(dictionary):
	files = os.listdir('Emails/')
	Emails = ['Emails/' + email for email in files]
	feature_set = []
	labels = []
	c = len(Emails)
	for email in Emails:
		data = []
		f = codecs.open(email, encoding = 'utf-8', errors = 'ignore')
		words = f.read().split(" ")

		for entry in dictionary:
			data.append(words.count(entry[0]))
		feature_set.append(data)

		if "ham" in email:
			labels.append(0)
		if "spam" in email:
			labels.append(1)

		print(c)
		c -= 1

	return feature_set, labels

d = Dictionary()
print(len(d))
import csv
 
w = csv.writer(open("Spam_Dictionary.csv", "w"))
for i in d:
	w.writerow([i[0], i[1]])

features, labels = dataset(d)

x_train, x_test, y_train, y_test = tts(features, labels, test_size = 0.2)
clf = MultinomialNB()
clf.fit(x_train, y_train)

predictedValues = clf.predict(x_test)
print("Accuracy: {}", accuracy_score(y_test, predictedValues))
save(clf, "Classified_Text.mdl")
