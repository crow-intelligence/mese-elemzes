import nltk
from nltk.corpus.reader import PlaintextCorpusReader
from nltk.collocations import *

# https://www.nltk.org/howto/collocations.html
# Collocations are expressions of multiple words which commonly co-occur

corpus = PlaintextCorpusReader("data/processed/", ".*", encoding="utf-8")

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
fourgram_measures = nltk.collocations.QuadgramAssocMeasures()

# bigrams
bg_finder = BigramCollocationFinder.from_words(corpus.words())
bg_finder.apply_freq_filter(5)
ignored_words = nltk.corpus.stopwords.words("hungarian")
bg_finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
bigram_collocations = bg_finder.nbest(bigram_measures.pmi, 10000)

# trigrams
tg_finder = TrigramCollocationFinder.from_words(corpus.words())
tg_finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
trigram_collocations = tg_finder.nbest(bigram_measures.pmi, 10000)

# fourgrams
fg_finder = QuadgramCollocationFinder.from_words(corpus.words())
fg_finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
fg_collocations = fg_finder.nbest(bigram_measures.pmi, 10000)


def get_collocates(wd):
    if wd in corpus.words():
        bgs = [e for e in bigram_collocations if wd in e]
        tgs = [e for e in trigram_collocations if wd in e]
        fgs = [e for e in fg_collocations if wd in e]
        return bgs, tgs, fgs
    else:
        return "Word is not in dictionary"


bgs, tgs, fgs = get_collocates("legény")

for e in bgs:
    print(f"bigram collocate {e}")

for e in tgs:
    print(f"trigram collocate {e}")

for e in fgs:
    print(f"fourgram collocate {e}")
