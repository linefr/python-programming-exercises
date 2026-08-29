# extra: reading a JSON file 
import json
from pathlib import Path
with open(Path("data.json")) as file:
    dados = json.load(file)
print(dados["nome"])
print(dados["valores"])