with open("data/interim/corpus.txt", "r") as infile:
    corpus = infile.read().strip()

wds = corpus.split()
print(len(wds), len(set(wds)))
