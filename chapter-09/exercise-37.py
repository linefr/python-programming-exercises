import json
from pathlib import Path

aluno_notas = {}

aluno_notas["aluno"] = input("Nome do aluno: ")

aluno_notas["notas"] = []
for i in range(3):
    aluno_notas["notas"].append(input(f"Nota {i + 1}:"))

print(aluno_notas)

with open(Path("notas-do-aluno"),"w") as file:
    json.dump(aluno_notas, file, indent= 2)