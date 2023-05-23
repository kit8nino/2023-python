class Avatar():
    name = 'Noname'
    max_x, max_y = 100, 100
    __secret = 'looks like a girlfriend'
    _step_count = 0

    def __init__(self, name='Noname', x=0, y=0, target=(10, 10)):
        self.x, self.y = x, y
        self.x0, self.y0 = x, y
        self.name = name
        self.target = target
        print(f'Avatar {self.name} created at ({self.x}, {self.y})')
        print('Secret:', self.__secret)

    def __str__(self):
        return self.name + ' (' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def set_name(self, name):
        if len(name) < 15:
            self.name = name
        else:
            print('Name should be less than 15 symbols!')
            self.name = name[:15]
            print(f'Trunkated to {name[:15]}')

    def get_name(self):
        return self.name

    def get_secret(self):
        return self.__secret

    def set_coord(self, x, y):
        if x < self.max_x:
            self.x = x
        if y < self.max_y:
            self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        if x < self.max_x:
            self.x = x

    def set_y(self, y):
        if y < self.max_y:
            self.y = y

    def make_step(self, alg='a_star'):
        self._step_count += 1
        # as a result - avatar will have new coordinates X and Y
        pass
