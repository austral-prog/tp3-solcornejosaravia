texto = input().strip()

if len(texto) < 5:
    print("La entrada tiene menos de 5 caracteres")
else:
    print(texto[4::2])
