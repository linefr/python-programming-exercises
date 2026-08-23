# Hangman with a timer
import time
antes = time.localtime()
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
depois = time.localtime()
terceira = ""
# Para cada letra na primeira string
for letra in primeira:
    # Se a letra está na segunda string (comum a ambas)
    # Para evitar repetidas, não deve estar na terceira.
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print(f"Caracteres em comum: {terceira}")

print(time.strftime("Antes: %S segundo(s)",antes))
print(time.strftime("Depois: %S segundo(s)",depois))