import GameApp.Adenauer.cards as cards

card1 = cards.Card(1)
card2 = cards.Card(10)
card3 = cards.Card(2)
card4 = cards.Card(7)

print(card1)
print(card2)
print(card3)
print(card4)
print("min", cards.Card.card_max([card1, card2, card3, card4]))
