import pickle as cPickle
import codecs
import os
from sklearn import *
from collections import Counter
import pandas as pd
import numpy as np

def loadModel(clf_file):
	with codecs.open(clf_file, 'rb') as fp:
		clf = cPickle.load(fp)
	return clf

clf = loadModel("Classified_Text.mdl")

d = pd.read_csv('Spam_Dictionary.csv')
d = d.iloc[:, 0]
while True:
	features = []
	newMail = input(">>").split()
	if newMail[0] == 'exit':
		break

	for i in range(len(d)):
		features.append(newMail.count(d[i]))
	features.append(0) # because there was an error in the shape of this array/matrix
	
	features = np.asmatrix(features)
	result = clf.predict(features)
	print(["Ham/Not Spam", "Spam"][result[0]])