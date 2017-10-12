import pandas as pd

amazonas = pd.read_json("amazonas.json")
amazonas.to_csv("amazonas.csv", sep=';')

lambayeque = pd.read_json("lambayeque.json")
lambayeque.to_csv("lambayeque.csv", sep=';')

cajamarca = pd.read_json("cajamarca.json")
cajamarca.to_csv("cajamarca.csv", sep=';')