from dataclasses import dataclass


@dataclass
class Bowler:
    name: str
    average: int
    high_score: int

    def __eq__(self, other):
        return self.average == other.average

    def __gt__(self, other):
        return self.average > other.average

    def __ge__(self, other):
        return self.average >= other.average

    def __lt__(self, other):
        return self.average < other.average

    def __le__(self, other):
        return self.average <= other.average
