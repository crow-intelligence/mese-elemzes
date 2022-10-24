import huspacy
from nltk.tokenize import sent_tokenize

with open("data/interim/corpus.txt", "r") as infile:
    corpus = infile.read()

nlp = huspacy.load()

lemmatized_corpus = []
texts = corpus.split("\n")
for text in texts:
    sents = sent_tokenize(text)
    for sent in sents:
        doc = nlp(sent)
        lemmas = [token.lemma_.lower() for token in doc if token.lemma_.isalpha()]
        if lemmas:
            o = " ".join(lemmas)
            lemmatized_corpus.append(o)
        print(
            f"so far we have {len(lemmatized_corpus)} tokens and {len(set(lemmatized_corpus))} types"
        )

with open("data/processed/lemmatized.txt", "w") as outfile:
    outfile.write("\n".join(lemmatized_corpus))

print("Done")
