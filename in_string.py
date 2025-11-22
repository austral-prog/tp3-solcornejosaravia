nombre = input().lower()

def check_vowels():
  print(f"Contiene a: {'a' in nombre}")
  print(f"Contiene e: {'e' in nombre}")
  print(f"Contiene i: {'i' in nombre}")
  print(f"Contiene o: {'o' in nombre}")
  print(f"Contiene u: {'u' in nombre}")
check_vowels(nombre)
