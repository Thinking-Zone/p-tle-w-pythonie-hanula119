import random

def losuj_pogode():
    return random.choice(['pada', 'nie pada'])

pogoda = losuj_pogode()

while True:
    odpowiedz = input("Czy pada deszcz? (odpowiedz 'pada' lub 'nie pada'): ").lower()

    if odpowiedz == pogoda:
        print("Brawo! Zgadłeś!")
        break  
    else:
        print("Nie zgadłeś. Spróbuj ponownie!")
