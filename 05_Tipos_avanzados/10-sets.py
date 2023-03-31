# Set significa grupo o conjunto

primer = {1, 1, 2, 2, 3, 4}
# print(primer)

# primer.add(5)
# primer.remove(1)

# print(primer)

segundo = [3, 4, 5]
segundo = set(segundo)

print(primer | segundo)  # Union
print(primer & segundo)  # Interseccion
print(primer - segundo)  # Diferencia
print(primer ^ segundo)  # Diferencia simetrica

if 5 in segundo:
    print("Hello, World!")
