import os
import sys

with open("nome-tamanho.html", "w", encoding="utf-8") as html:
    for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
        html.write(f"\n Caminho: {raiz}")
        for d in diretorios:
            print(d)