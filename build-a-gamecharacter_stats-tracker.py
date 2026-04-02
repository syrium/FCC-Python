class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name
    """
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError(f"Character name must be string.")
        return self._name = new_name
    """
    
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, new_health):
        if not isinstance(new_health, int):
            raise TypeError(f"Character health must be an integer.")

        #if not (0 <= new_health <= 100):
        #    raise ValueError(f"Character health must be between 0 and 100.")
        if new_health < 0:
            self._health = 0
            #raise ValueError(f"Character health must be between 0 and 100.")
        elif new_health > 100:
            self._health = 100
            #raise ValueError(f"Character health must be between 0 and 100.")
        else:
            self._health = new_health
        print(f"Character health is set to {self.health}.")

    @property
    def mana(self):
        return self._mana
    @mana.setter
    def mana(self, new_mana):
        if not isinstance(new_mana, int):
            raise TypeError(f"Character mana must be an integer.")
        #if not (0 <= new_mana <= 50):
        #    raise ValueError(f"Character mana must be between 0 and 50.")
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana
        print(f"Character mana is set to {self.mana}.")

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        string = [
            f"Name: {self.name}",
            f"Level: {self.level}",
            f"Health: {self.health}",
            f"Mana: {self.mana}"
        ]

        return '\n'.join(string)

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 30  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up

hero.mana = -1
print(hero)

hero.mana = 101
print(hero)
