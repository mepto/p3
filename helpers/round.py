from datetime import datetime


class Round:
    def __init__(self, round_nb: int, matches: list):
        self.round_nb = f'Round {round_nb}'
        self.matches = matches
        self.start_time = self.get_now()
        self.end_time = None

    @staticmethod
    def get_now():
        return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    def serialize(self):
        return {
            self.round_nb: {
                'start_time': self.start_time,
                'end_time': self.end_time,
                'matches': self.matches
            }
        }
