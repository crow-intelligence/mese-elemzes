from nltk.corpus.reader import PlaintextCorpusReader
from nltk.text import Text

# A concordance view shows us every occurrence of a given word, together with some context.
# https://www.nltk.org/howto/concordance.html
corpus = PlaintextCorpusReader("data/processed/", ".*", encoding="utf-8")
text = Text(corpus.words())


def get_concordance(wd, destination, width=200, lines=10000):
    # kiírja az összes előfordulást, a width szabályozza hogy egy soron mennyi karakter jelenik meg
    c_list = text.concordance_list(wd, width=width, lines=lines)
    if isinstance(wd, list):
        wd = " ".join(wd)
    with open(f"data/analyze/{destination}", "w") as outfile:
        for line in c_list:
            o = " ".join(line.left) + "\t" + wd + "\t" + " ".join(line.right) + "\n"
            outfile.write(o)


get_concordance("legény", "legény.txt")
get_concordance(["szegény", "legény"], "szlegyény.txt")

# ha nem akarjuk elmenteni, csak nézni az outputot
text.concordance(
    "legény", width=120, lines=100
)  # width a karakterek számát, lines a kiírt sorokat szabályozza
text.concordance(["szegény", "legény"], width=120, lines=100)
