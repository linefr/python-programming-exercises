# extra: directory tree being traversed
import os
import sys
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print("\nCaminho:", raiz)
    for d in diretorios:
        print(f"  {d}/")
    for f in arquivos:
        print(f"  {f}/")
    print(f"{len(diretorios)} diretórios(s), {len(arquivos)} arquivo(s)")
