# extra: file properties
import os
import time
file = "exercise-30.py"
print(f"Tamanho: {os.path.getsize(file)}")
print(f"Acessado: {time.ctime(os.path.getatime(file))}")
print(f'Criado: {time.ctime(os.path.getctime(file))}')

