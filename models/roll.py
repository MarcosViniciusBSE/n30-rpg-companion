import random
import re


class Roll:
    def __init__(self, roll):
        self.roll = roll

    def rollDice(self):
        match = re.fullmatch(r'(\d+)d(\d+)([+-]\d+)?', self.roll)
        if not match:
            return f"Invalid dice notation: {self.roll}"

        num_dice, num_sides = int(match.group(1)), int(match.group(2))
        modifier = int(match.group(3) or 0)

        if num_dice < 1 or num_sides < 1:
            return "Number of dice and sides must be greater than zero."

        rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
        total_NoModifier = sum(rolls)
        total_WithModifier = total_NoModifier + modifier

        if modifier == 0:
            return f"Resultado: {rolls} -> {total_NoModifier}"

        if modifier < 0:
            return f"Resultado: {rolls} -> {total_NoModifier} - {abs(modifier)} -> {total_WithModifier}"

        return f"Resultado: {rolls} -> {total_NoModifier} + {modifier} -> {total_WithModifier}"
