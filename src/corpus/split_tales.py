import re

with open("data/interim/corpus.txt", "r") as infile:
    corpus = infile.read().encode("iso-8859-2").decode("utf-8").strip().replace("\t", " ")

# pattern = re.compile(r"tartalom\n(.*\n)+\n+", flags=re.I|re.UNICODE|re.MULTILINE)
titles = re.finditer(r"tartalom\n(.*\n)+\n+", corpus, flags=re.I|re.UNICODE|re.MULTILINE)

for e in titles:
    print(e.string)

