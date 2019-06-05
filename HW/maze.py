#!/usr/bin/env python3
"""
DU5
"""

import sys


class Maze():
    def __init__(self, structure, num_steps):
        self._structure = structure
        self._num_steps = num_steps
        self._position, self._direction = self.find_position()


    def __str__(self):
        if self._structure[self._position[0]][self._position[1]] != self._direction:
            self._structure[self.find_position()[0][0]][self.find_position()[0][1]] = "."
            self._structure[self._position[0]][self._position[1]] = self._direction
        text_lines = []
        for line in self._structure:
            text_lines.append(" ".join(line))
        return "\n".join(text_lines)

    def find_position(self):
        for i, e in enumerate(self._structure):
            try:
                return [i, e.index("<")], "<"
            except ValueError:
                try:
                    return [i, e.index(">")], ">"
                except ValueError:
                    try:
                        return [i, e.index("^")], "^"
                    except ValueError:
                        try:
                            return [i, e.index("v")], "v"
                        except:
                            pass


    def is_wall_on_right(self):
        if self._direction == "<" and self._structure[self._position[0]-1][self._position[1]] == "#":
            return True  
        elif self._direction == ">" and self._structure[self._position[0]+1][self._position[1]] == "#":
            return True
        elif self._direction == "^" and self._structure[self._position[0]][self._position[1]+1] == "#":
            return True
        elif self._direction == "v" and self._structure[self._position[0]][self._position[1]-1] == "#":
            return True
        else:
            return False


    def is_corner(self):
        if self._structure[self._position[0]][self._position[1]-1] == "#" and self._structure[self._position[0]-1][self._position[1]] == "#" and self._structure[self._position[0]-1][self._position[1]-1] == "#":
            return True
        if self._structure[self._position[0]][self._position[1]-1] == "#" and self._structure[self._position[0]+1][self._position[1]] == "#" and self._structure[self._position[0]+1][self._position[1]-1] == "#":
            return True
        if self._structure[self._position[0]][self._position[1]+1] == "#" and self._structure[self._position[0]+1][self._position[1]] == "#" and self._structure[self._position[0]+1][self._position[1]+1] == "#":
            return True
        if self._structure[self._position[0]][self._position[1]+1] == "#" and self._structure[self._position[0]-1][self._position[1]] == "#" and self._structure[self._position[0]-1][self._position[1]+1] == "#":
            return True
        else:
            return False


    def turn_left(self):
        if self._direction == "<":
            self._direction = "v"
        elif self._direction == "v":
            self._direction = ">"
        elif self._direction == ">":
            self._direction = "^"
        elif self._direction == "^":
            self._direction = "<"
    

    def turn_right(self):
        if self._direction == "<":
            self._direction = "^"
        elif self._direction == "v":
            self._direction = "<"
        elif self._direction == ">":
            self._direction = "v"
        elif self._direction == "^":
            self._direction = ">"


    def do_move(self):
        if self._direction == "<":
            self._position[1] -= 1
        elif self._direction == "v":
            self._position[0] += 1
        elif self._direction == ">":
            self._position[1] += 1
        elif self._direction == "^":
            self._position[0] -= 1


    def can_move(self):
        if self._direction == "<" and self._structure[self._position[0]][self._position[1]-1] != "#":
            return True
        elif self._direction == ">" and self._structure[self._position[0]][self._position[1]+1] != "#":
            return True
        elif self._direction == "v" and self._structure[self._position[0]+1][self._position[1]] != "#":
            return True
        elif self._direction == "^" and self._structure[self._position[0]-1][self._position[1]] != "#":
            return True
        return False


    def move (self):
        i = 0
        while i < self._num_steps:
            if self.is_wall_on_right() and self.can_move():
                self.do_move()
                i += 1
                if not self.is_wall_on_right() and i < self._num_steps:
                    self.turn_right()
                    self.do_move()
                    i += 1
            elif self.is_corner():
                self.turn_left()
            

if __name__ == "__main__":
    structure = []
    num_steps = int(input())
    for line in sys.stdin:
        structure.append(line.split())
    maze1 = Maze(structure, num_steps)
    maze1.move()
    print(maze1)
