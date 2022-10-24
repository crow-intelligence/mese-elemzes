from src.utils.svd_algebra import SVDAlgebra

a = SVDAlgebra("data/processed/")
a.save_model("mese", "data/lm")

print("Done")
