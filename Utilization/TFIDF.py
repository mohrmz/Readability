
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re


class TFIDFCalculation:

    @classmethod
    def calculate_TFIDF(cls, input_text, *args):
        #cleaning text
        sentences = sent_tokenize(input_text)
        stemmer = PorterStemmer()
        corpus = []

        for sent in sentences:
            review = re.sub("[^a-zA-Z]", " ", sent)
            review = re.sub("\b[a-zA-Z]\b", " ", review)
            review = review.lower()
            review = review.split()
            review = [stemmer.stem(word) for word in review if not word in set(stopwords.words('english'))]
            review = " ".join(review)
            corpus.append(review)

        #vectorization
        from sklearn.feature_extraction.text import CountVectorizer
        cv = CountVectorizer()
        bow = cv.fit_transform(corpus).toarray()

        from sklearn.feature_extraction.text import TfidfVectorizer
        tf = TfidfVectorizer()
        tfidf = tf.fit_transform(corpus).toarray()

if __name__ == '__main__':   
    TFIDFCalculation.calculate_TFIDF('execute')