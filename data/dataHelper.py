from models.ritual import Ritual, Level
import json


def jsonLoadRitualList():
    with open('data/rituals.json', 'r') as f:
        rawRitualList = json.load(f)
        return rawRitualList


def dictToRitual():
    raw = jsonLoadRitualList()
    ritualList = []

    for ritual_data in raw['rituals']:
        levels = [Level(level['levelName'], level['damage']) for level in ritual_data['level']]
        ritual = Ritual(ritual_data['name'], levels, ritual_data['element'])
        ritualList.append(ritual)

    return ritualList


def getRitual(ritualName):
    ritualList = dictToRitual()
    for ritual in ritualList:
        if ritual.name == ritualName:
            return ritual
    raise "Ritual não encontrado"
