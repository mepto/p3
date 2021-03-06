from helpers.database import Database


class Player:
    """Create a player"""

    def __init__(self, player: dict = {}):
        self._db = Database()
        self.id = player['id'] if 'id' in player else self._db.get_next_id('player')
        self.last_name = player['last_name'] if 'last_name' in player else ''
        self.first_name = player['first_name'] if 'first_name' in player else ''
        self.dob = player['dob'] if 'dob' in player else ''
        self.gender = player['gender'] if 'gender' in player else ''
        self.ranking = int(player['ranking']) if 'ranking' in player else ''

    def create(self):
        self._db.create('player', self.serialize())

    def update(self, new_data: dict):
        doc = self._db.read('player', **{'id': new_data['id']})[0][0]
        doc_id = doc.doc_id
        self._db.update('player', item_id=doc_id, **new_data)

    def serialize(self):
        return {
            'id': self.id,
            'last_name': self.last_name.upper(),
            'first_name': self.first_name.capitalize(),
            'dob': self.dob,
            'gender': self.gender,
            'ranking': self.ranking
        }

    def get_rank(self, p_id):
        item = self.get_item(p_id)
        return item['id'], item['ranking']

    def get_players(self):
        return self._db.read('player')

    def get_player_name(self):
        item = self.get_item(self.id)
        return f"{item['last_name'].upper()} {item['first_name'].capitalize()}"

    def get_item(self, p_id):
        return self._db.read(table='player', **{'id': p_id})[0][0]
