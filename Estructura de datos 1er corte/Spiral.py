# Program: spiral.py
# Description: Llenar una matriz con una espiral de adentro hacia afuera 
# Author: Juan Pablo Trejos Rodriguez

class filler:
    def __init__(self, srcarray):
        self.size = len(srcarray)
        self.array = [[None for y in range(self.size)] for y in range(self.size)]
        self.xpos, self.ypos = 0, 0
        self.directions = [self.down, self.right, self.up, self.left]
        self.direction = 0
        self.fill(srcarray)

    def fill(self, srcarray):
        for row in reversed(srcarray):
            for elem in reversed(row):
                self.array[self.xpos][self.ypos] = elem
                self.go_to_next()

    def check_next_pos(self):
        np = self.get_next_pos()
        if np[1] in range(self.size) and np[0] in range(self.size):
            return self.array[np[0]][np[1]] == None
        return False

    def go_to_next(self):
        i = 0
        while not self.check_next_pos() and i < 4:
            self.direction = (self.direction + 1) % 4
            i += 4
        self.xpos, self.ypos = self.get_next_pos()

    def get_next_pos(self):
        return self.directions[self.direction](self.xpos, self.ypos)

    def down(self, x, y):
        return x + 1, y

    def right(self, x, y):
        return x, y + 1

    def up(self, x, y):
        return x - 1, y

    def left(self, x, y):
        return x, y - 1

    def print_grid(self):
        for row in self.array:
            print(row)


f = filler([[x+y*5 for x in range(7)] for y in range(7)])
f.print_grid()