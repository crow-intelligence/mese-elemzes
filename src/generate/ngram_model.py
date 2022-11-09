import pickle

from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.tokenize import sent_tokenize, word_tokenize

with open("data/interim/corpus.txt", "r") as infile:
    raw_corpus = infile.read().strip()

sentences = sent_tokenize(raw_corpus)
sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
text = [word_tokenize(s) for s in sentences]
train, vocab = padded_everygram_pipeline(5, text)

lm = MLE(2)
lm.fit(train, vocab)

with open("data/mle_model/lm.pkl", "wb") as outfile:
    pickle.dump(lm, outfile)
