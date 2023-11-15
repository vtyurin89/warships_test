from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x, self._y = x, y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(self._length)]

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            pass

    @staticmethod
    def get_rect_coords(ship):
        return ship.x - 1, ship.y - 1

    @staticmethod
    def get_rect_width_height(ship) -> tuple:
        if ship._tp == 1:
            rect_width = ship._length + 2
            rect_height = 3
        else:
            rect_width = 3
            rect_height = ship._length + 2
        return rect_width, rect_height

    def is_collide(self, ship):
        if ship.x is None and ship.y is None:
            return False
        me_rect_x, me_rect_y = self.x, self.y
        ship_rect_x, ship_rect_y = self.get_rect_coords(ship)
        me_width, me_height = list(map(lambda x: x-2, self.get_rect_width_height(self)))
        ship_width, ship_height = self.get_rect_width_height(ship)
        if not (me_rect_x + me_width <= ship_rect_x or ship_rect_x + ship_width <= me_rect_x
                or me_rect_y + me_height <= ship_rect_y or ship_rect_y + ship_height <= me_rect_y):
            return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:
            if self._x + self._length - 1 not in range(size):
                return True
        elif self._tp == 2:
            if self._y + self._length - 1 not in range(size):
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

    def change_pole(self):
        for ship in self._ships:
            for i in range(ship._length):
                if ship._tp == 1:
                    self._pole[ship.y][ship.x + i] = 1
                if ship._tp == 2:
                    self._pole[ship.y + i][ship.x] = 1

    def init(self):
        deck_list = [4,3,3,2,2,2,1,1,1,1]
        for deck in deck_list:
            ship = Ship(deck, tp=randint(1, 2))
            self._ships.append(ship)
        for ship in self._ships:
            while True:
                inside_pole = False
                collision = False
                ship.set_start_coords(randint(0, self._size-1), randint(0, self._size-1))
                if not ship.is_out_pole(self._size):
                    inside_pole = True
                else:
                    continue
                for other_ship in self._ships:
                    if id(other_ship) == id(ship):
                        continue
                    if ship.is_collide(other_ship):
                        collision = True
                        break
                if inside_pole and not collision:
                    break
        self.change_pole()

    def get_ships(self):
        return self._ships

    def move_ships(self):
        pass

    def show(self):
        for row in self._pole:
            print(*row)

    def get_pole(self):
        return tuple([tuple(row) for row in self._pole])


p = GamePole(10)
p.init()
p.show()