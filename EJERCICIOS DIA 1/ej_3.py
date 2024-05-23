def counter(text):
    words = text.split()
    num_words = len(words)
    return num_words

# Ejemplo de uso
text = "Hola como estan"
res = counter(text)
print("Número de palabras:", res)
