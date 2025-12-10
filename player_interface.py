"""Player interface and implementations for a game."""
from abc import ABC, abstractmethod
import random


class Player(ABC):
    """Abstract base class for a player in the game."""

    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        """Make a move and update the player's position."""
        move = random.choice(self.moves)

        # update position
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        self.position = new_position

        # record new position
        self.path.append(self.position)

        return self.position

    @abstractmethod
    def level_up(self):
        """Level up the player, potentially adding new moves."""
        pass


class Pawn(Player):
    """Concrete class representing a Pawn player."""

    def __init__(self):
        super().__init__()

        self.moves = [
            (0, 1),   # up
            (0, -1),  # down
            (-1, 0),  # left
            (1, 0)    # right
        ]

    def level_up(self):
        diagonal_moves = [
            (-1, 1),   # up-left
            (1, 1),    # up-right
            (-1, -1),  # down-left
            (1, -1)    # down-right
        ]
        self.moves.extend(diagonal_moves)

p = Pawn()
p.make_move()