class Horse:
    x_distance = 0
    sound = 'Frr'

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        pegas = [self.x_distance, self.y_distance]
        pegas = tuple(pegas)
        return pegas

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
