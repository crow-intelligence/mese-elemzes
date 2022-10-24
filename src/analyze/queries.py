from src.utils.svd_algebra import SVDAlgebra

a = SVDAlgebra("data/lm/")

# leghasonlóbb n
print(a.most_similar_n("királylány", 30))

# távolság két szó között
print(a.distance("alma", "körte"))
print(a.distance("király", "királylány"))

# analogy difference -> analógia
print(a.similar(["szegény", "legény"], "királylány", topn=5))

# kakukktojás
print(a.doesnt_match(["legény", "király", "kutya"]))
