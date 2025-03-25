meme_dict = {
    "Pacior": "Określenie jakiegos smiesznego wydarzenia lub cos co jest smieszne.",
    "Sigma": "Powiedzenie do kogos gdy cos zrobił smiesznego ale zarazem powaznego.",
    "XD": "Coś bardzo śmiesznego.",
}

word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Nie znaleziono słowa w słowniku.")
