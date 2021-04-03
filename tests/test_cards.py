import GameApp.Adenauer.cards as cards
import pytest


class TestCards:
    def test_init(self):
        with pytest.raises(ValueError):
            cards.Card(number=2, color="herz", value=2)

    def test_get_color(self):

        color_pairs = []
        for i in range(0, 8):
            color_pairs += [(i, "herz")]
        for i in range(8, 16):
            color_pairs += [(i, "schellen")]
        for i in range(16, 24):
            color_pairs += [(i, "eichel")]
        for i in range(24, 32):
            color_pairs += [(i, "gras")]

        for number, color in color_pairs:
            card = cards.Card(number=number)
            assert card.get_color() == color, "Number :" + str(number)

    def test_get_color_value(self):
        value_pairs = []
        for i, j in zip(range(0, 8), range(0, 8)):
            value_pairs += [(i, j)]
        for i, j in zip(range(8, 16), range(0, 8)):
            value_pairs += [(i, j)]
        for i, j in zip(range(16, 24), range(0, 8)):
            value_pairs += [(i, j)]
        for i, j in zip(range(24, 32), range(0, 8)):
            value_pairs += [(i, j)]
        for number, value in value_pairs:
            card = cards.Card(number=number)
            assert card.get_color_value() == value, "Number :" + str(number)

    def test_get_number_from_color_value(self):
        value_pairs = []
        number = 0
        for color in cards.Card.colors:
            for values in cards.Card.values:
                value_pairs += [(color, values, number)]
                number += 1

        for color, value, number in value_pairs:
            card = cards.Card(color=color, value=value)
            assert card.get_number_from_color_value(color=color, value=value) == number

    def test_eq(self):
        assert cards.Card(color="herz", value=3) == cards.Card(color="herz", value=3)
        assert cards.Card(color="herz", value=3) != cards.Card(color="herz", value=4)

    def test_card_max(self):
        cardsCmp = [
            cards.Card(color="herz", value=3),
            cards.Card(color="herz", value=6),
            cards.Card(color="schellen", value=7),
        ]
        assert cards.Card.card_max(cardsCmp) == cards.Card(color="herz", value=6)
        assert cards.Card.card_max(cardsCmp, idx=True) == 1
        assert cards.Card.card_max(cardsCmp, played_color="schellen", idx=True) == 2

        with pytest.raises(ValueError):
            cards.Card.card_max(cardsCmp, played_color="gras")
        #    [
        #        cards.Card(color="eichel", value=3),
        #        cards.Card(color="herz", number=6),
        #        cards.Card(color="schellen", number=7),
        #    ],
        # ]
