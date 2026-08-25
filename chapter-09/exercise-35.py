import os
import sys

with open("nome-tamanho.html", "w", encoding="utf-8") as html:
    html.write("""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
    <meta charset="utf-8">
    <title>Tamanho arquivos</title>
    </head>
    <body>
    """)
    print("hello")
    for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
        html.write(f"<h1> Caminho: {raiz} </h1>")
        bytes = os.path.getsize(raiz)
        for d in diretorios:
            bytes = os.path.getsize(d)
            kilobytes = bytes / 1024
            html.write(f"<p> {d} - <strong> Tamanho: {kilobytes:.2f} KB </strong> </p>")
        for f in arquivos:
            bytes = os.path.getsize(f)
            kilobytes = bytes / 1024
            html.write(f"<p> {f} - <strong> Tamanho: {kilobytes:.2f} KB </strong> </p>")
        html.write(f"<footer> {len(diretorios)} diretórios(s), {len(arquivos)} arquivo(s) </footer>")
