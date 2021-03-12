'''On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
'''


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir = 0
        row, col = 0, 0
        for i in instructions:
            if i is "G":
                row, col = self.move_robot(row, col, dir)
            if i is "L":
                dir += 1
                dir %= 4
            elif i is "R":
                dir -= 1
                dir %= 4
        if dir == 0:
            return row == 0 and col == 0
        return True

    def move_robot(self, row, col, dir):
        if dir == 0:
            row += 1
        elif dir == 1:
            col -= 1
        elif dir == 2:
            row -= 1
        else:
            col += 1
        return row, col


class Solution2:
    def isRobotBounded1(self, instructions: str) -> bool:
        if len(instructions) < 2:
            return False
        counter = 0
        row = col = direction = 0
        visited = set()
        for _ in range(8):
            row, col, direction, visited = self.move_robot(row, col, instructions, visited, direction)
            if len(visited) == 0:
                return True
        return False

    def move_robot(self, row, col, s, visited, direction):
        for i in s:
            if i is "L":
                direction -= 1
                if direction < 0:
                    direction = 3
            if i is "R":
                direction += 1
                if direction > 3:
                    direction = 0
            if i is "G":
                if direction is 0:
                    row += 1
                    visited = self.handle_visit(row, col, visited)
                elif direction is 1:
                    col += 1
                    visited = self.handle_visit(row, col, visited)
                elif direction is 2:
                    row -= 1
                    visited = self.handle_visit(row, col, visited)
                elif direction is 3:
                    col -= 1
                    visited = self.handle_visit(row, col, visited)
        return row, col, direction, visited

    def handle_visit(self, row, col, visited):
        if (row, col) in visited:
            visited.remove((row, col))
        else:
            visited.add((row, col))
        return visited