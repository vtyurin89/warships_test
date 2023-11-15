from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x, self._y = x, y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]

    def set_start_coords(self, x, y):
        if self._x is None and self._y is None:
            self._x = x
            self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            pass

    def is_collide(self, ship):
        pass

    def is_out_pole(self, size):
        if self._x + self._length - 1 not in range(size) or self._y + self._length - 1 not in range(size):
            return True
        return False

    def __getitem__(self, item):
        if type(item) != int or item not in range(len(self._cells)):
            raise IndexError("Неверный индекс!")
        return self._cells[item]

    def __setitem__(self, key, value):
        if type(key) != int or key not in range(len(self._cells)):
            raise IndexError("Неверный индекс!")
        if value not in (1, 2):
            raise ValueError("Недопустимое значение для палубы")
        self._cells[key] = value


class GamePole:
    def __init__(self, size):
        self._size = size
        self._ships = []
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]

    def init(self):
        deck_list = [4,3,3,2,2,2,1,1,1,1]
        for deck in deck_list:
            ship = Ship(deck, tp=randint(1, 2))
            self._ships.append(ship)

    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        for row in self._pole:
            print(*row)

    def get_pole(self):
        return tuple([tuple(row) for row in self._pole])

g = GamePole(10)
g.init()
print(g.get_pole())