from avatartest import Avatar
from mobtest import Mob

a = Avatar()
m = Mob()

for i in range(50):
    a.step(a.A_star())
    if a.A_star() == None:
        break
    if i > 1:
        m.step(m.dijkstra((a.x, a.y)))

input()
