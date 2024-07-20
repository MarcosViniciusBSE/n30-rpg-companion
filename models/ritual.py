from typing import List
from models.roll import Roll


class Level:
    def __init__(self, levelName, damage):
        self.levelName = levelName
        self.damage = damage


class Ritual:
    def __init__(self, name, level: List[Level], element):
        self.name = name
        self.level = level
        self.element = element

    def getDamage(self, levelName: str):
        for level in self.level:
            if level.levelName == levelName:
                return level.damage
        return "Level não encontrado"

    def getLevelName(self, levelName: str):
        for level in self.level:
            if level.levelName == levelName:
                return level.levelName
        return "Level não encontrado"

    def rollRitual(self, levelName: str):
        damage = self.getDamage(levelName)
        return Roll(self.getDamage(levelName)).rollDice()[0], damage

    def ritualToResponse(self, levelName):
        ritualRoll = self.rollRitual(levelName)
        return f"{self.name.capitalize()}! {ritualRoll[1]} -> {ritualRoll[0]} -> {sum(ritualRoll[0])} de dano de {self.element.upper()}!"
