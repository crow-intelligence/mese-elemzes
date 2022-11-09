import pickle

lm = pickle.load(open("data/mle_model/lm.pkl", "rb"))


def generate_sequence(length=100):
    candidate = lm.generate(length)
    candidate = [e for e in candidate if e not in ['</s>', '<s>']]
    return " ".join(candidate)


def generate_with_seed(seed="Szegény", length=100):
    candidate = lm.generate(length, text_seed=seed.split())
    candidate = [e for e in candidate if e not in ['</s>', '<s>']]
    return " ".join(candidate)


print(generate_sequence())
print()
print(generate_with_seed())
