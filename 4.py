# Этажи подземелья хранятся в плеере, как уровень
# У плеера может быть меч, броня и 3 скилла
# У плеера есть атака и хп и инвентарь
# У брони будет прочность и кол-во поглащаемого урона
# У оружие будет атака и прочность
# У монстра будет атака и хп и броня на 1 удар


class Weapon:
    def __init__(self, name: str, offense: int):
        self.name = name
        self.offense = offense


class Armor:
    def __init__(self, name: str, defense: int, endurance: int):
        self.name = name
        self.defense = defense
        self.endurance = endurance


class Spell:
    def __init__(self, name: str, value: int, type: str):
        self.name = name
        self.value = value
        self.type = type

    def use(self, caster, target=None):
        if self.type == "damage":
            if target:
                # target hp - self.value 
            else:
                # caster hp - self.value
        if self.type == "heal":
            pass
            # caster hp + self.value


class Player:
    def __init__(self, name: str, hp: int, offense: int):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.weapon: Weapon = None
        self.armor: Armor = None
        self.spells: dict[Spell] = {1: None, 2: None, 3: None}
        self.inventory = {1: None, 2: None, 3: None, 4: None, 5: None}

    def attack(self, target: Enemy):
        summary_offense = self.offense
        if self.weapon:
            summary_offense += self.weapon.offense
        damage = target.defense - summary_offense
        if damage > 0:
            target.hp -= damage

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def change_armor(self, new_armor: Armor):
        self.armor = new_armor

    def add_to_inventory(self, item: Weapon | Armor):
        for place, key in self.inventory:
            if place == None:
                self.inventory[key] = item


class Enemy:
    def __init__(self, name: str, hp: int, offense: int, defense: int):
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self, target: Player):
        if target.armor:
            target.armor.endurance -= self.offense / 2
            damage = target.armor.defense - self.offense
            if damage > 0:
                target.hp -= damage
