
##import spacy

##from scispacy.abbreviation import AbbreviationDetector

##nlp = spacy.load("en_core_sci_sm")

##nlp.add_pipe("abbreviation_detector")

##def abbreviated_names(input):
##    doc = nlp(input)
##    print(doc._.abbreviations)
##    for abrv in doc._.abbreviations:
	    ##print(f"{abrv} \t ({abrv.start}, {abrv.end}) {abrv._.long_form}")

#import nltk
#import normalise
#for dependency in ("brown", "names", "wordnet", "averaged_perceptron_tagger", "universal_tagset"):
#    nltk.download(dependency)

#text = ["On", "the", "28", "Apr.", "2010", ",", "Dr.", "Banks", "bought", "a", "chair", "for", "£35", "."]

#normalise(text, verbose=True)

#import numpy as np
#from sklearn import datasets
#from sklearn.semi_supervised import LabelPropagation
#label_prop_model = LabelPropagation()
#iris = datasets.load_iris()
#rng = np.random.RandomState(42)
#random_unlabeled_points = rng.rand(len(iris.target)) < 0.3
#labels = np.copy(iris.target)
#labels[random_unlabeled_points] = -1
#label_prop_model.fit(iris.data, labels)
#print(labels)

#text = ["On", "the", "28", "Apr.", "2010", ",", "Dr.", "Banks", "bought", "a", "chair", "for", "£35", "."]

#from normalise import tokenize_basic
#normalise(text, verbose=True)

from .MeaninglessNames import *

def abbreviated_names(input,*args):
    return meaningless_names(input)