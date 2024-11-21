
liczba_nie = 0


while True:
    odpowiedz = input("Czy pada? (odpowiedz 'tak', 'nie' lub 'nie wiem'): ").lower()

    if odpowiedz == "tak":
        print(f"Program zakończony. Liczba odpowiedzi 'nie': {liczba_nie}")
        break 
    elif odpowiedz == "nie":
        liczba_nie += 1 
    elif odpowiedz == "nie wiem":
        print("To wyjdź na zewnątrz i się dowiedz.")
    else:
        print("Proszę odpowiedzieć 'tak', 'nie' lub 'nie wiem'.")
