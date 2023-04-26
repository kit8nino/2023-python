from avatar import Avatar


class Surrogat(Avatar):
    _power = 'lithium'
    _charge = 100

    def __init__(self, x=0, y=0, name='n0n@me'):
        super().__init__(x, y)
        self.set_name(name)

    def is_charge(self):
        return self._charge > 0

    def make_step(self, alg='greedy'):
        if self.is_charge():
            super().make_step(alg)
            self._charge -= 5
        else:
            print('Charge too low')


a = Surrogat(13, 14)
while a.is_charge():
    print('Thug life!')
    a.make_step()
a.make_step()
print(a)
