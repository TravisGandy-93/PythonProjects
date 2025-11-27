"""Module for managing a musical instrument inventory."""
class MusicalInstrument:
    """Class implementing a musical instrument."""
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        """Method to simulate playing the instrument."""
        print(f'The {self.name} is playing!')

    def get_fact(self):
        """Method to get a fact about the instrument."""
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())
instrument_2.play()
print(instrument_2.get_fact())
