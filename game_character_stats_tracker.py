"""This module defines a GameCharacter class to track and manage game character stats."""
class GameCharacter:
    """Class representing a game character with health, mana, and level."""
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        """Get the name of the character."""
        return self._name

    @property
    def health(self):
        """Get the health of the character."""
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:    
            self._health = new_health

    @property
    def mana(self):
        """Get the mana of the character."""
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana

    @property
    def level(self):
        """Get the level of the character."""
        return self._level

    def level_up(self):
        """Increase the character's level by 1 and reset health and mana."""
        self._level = self._level + 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        return (
        f"Name: {self.name}\n"
        f"Level: {self.level}\n"
        f"Health: {self.health}\n"
        f"Mana: {self.mana}"
    )

hero = GameCharacter('Kratos') # Creates a new character named Kratos
print(hero)  # Displays the character's stats

hero.health -= 15  # Decreases health by 30
hero.mana -= 10    # Decreases mana by 10
print(hero)  # Displays the updated stats

hero.level_up()  # Levels up the character
print(hero)  # Displays the stats after leveling up
