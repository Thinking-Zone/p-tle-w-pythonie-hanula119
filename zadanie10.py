
licznik = 0


for liczba in range(1, 51):
    if liczba % 3 == 0 and liczba % 5 != 0:
        print(liczba) 
        licznik += 1  

print(f"Liczba liczb podzielnych przez 3, ale nie przez 5: {licznik}")
