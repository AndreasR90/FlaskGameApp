from __future__ import annotations

from typing import List, Union


class Card:
    colors = [
        "herz",
        "schellen",
        "eichel",
        "gras",
    ]
    values = [
        "7",
        "8",
        "9",
        "10",
        "U",
        "O",
        "K ",
        "A",
    ]

    def __init__(self, number=None, color=None, value=None):
        if number is not None:
            self.number = number
            if color or value:
                raise ValueError("Only provide number or (color + value)")
        elif (color is not None) and (value is not None):
            self.number = self.get_number_from_color_value(color=color, value=value)
        else:
            raise ValueError("You must provide any of number or (color + value)")
        self.color = self.get_color()
        self.color_value = self.get_color_value()
        self.color_value_string = self.values[self.color_value]

    def get_color(self):
        colnum = self.number // len(self.values)
        return self.colors[colnum]

    def get_color_value(self):
        return self.number % len(self.values)

    def get_number_from_color_value(self, color, value):
        color_idx = [i for i, col in enumerate(self.colors) if col == color][0]
        if isinstance(value, str):
            value_idx = [i for i, val in enumerate(self.values) if val == value][0]
        else:
            value_idx = value
        return color_idx * len(self.values) + value_idx

    def __str__(self):
        return "Card [Number : {.number} ; Color : {.color}, ColorValue : {.color_value}]".format(
            self, self, self
        )

    @staticmethod
    def card_max(card_list: List, played_color=None, idx=False) -> Union[int, Card]:
        if not played_color:
            played_color = card_list[0].color
        idx_use = None
        min_value = -1
        for cnt, card in enumerate(card_list):
            if card.color == played_color:
                if card.color_value > min_value:
                    min_value = card.color_value
                    idx_use = cnt
        if idx_use is None:
            raise ValueError(played_color + " is not in trick")
        if idx:
            return idx_use
        return card_list[idx_use]

    def __eq__(self,other):
        return self.number == other.number
