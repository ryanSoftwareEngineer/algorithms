'''
https://leetcode.com/problems/design-snake-game/

Design a Snake game that is played on a device with screen size height x width. Play the game online if you are not familiar with the game.

The snake is initially positioned at the top left corner (0, 0) with a length of 1 unit.

You are given an array food where food[i] = (ri, ci) is the row and column position of a piece of food that the snake can eat. When a snake eats a piece of food, its length and the game's score both increase by 1.

Each piece of food appears one by one on the screen, meaning the second piece of food will not appear until the snake eats the first piece of food.

When a piece of food appears on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

The game is over if the snake goes out of bounds (hits a wall) or if its head occupies a space that its body occupies after moving (i.e. a snake of length 4 cannot run into itself).

Implement the SnakeGame class:

SnakeGame(int width, int height, int[][] food) Initializes the object with a screen of size height x width and the positions of the food.
int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1.
'''


# my strategy was to use a linkedlist to represent the snake (could have also used queue)
# when the snake moved without eating we would pop the tail end of the linkedlist and
# add the new position to the head. If we were eating food then we just add a new head in front
# i used a set() to keep track of the snakes body ( the snakes body are the linkedlist nodes)




class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class Snake:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        newnode = Node((0, 0))
        self.head.next = newnode
        self.tail.prev = newnode
        newnode.next = self.tail
        newnode.prev = self.head
        self.body = set()
        self.body.add((0, 0))

    def swaptail(self, newlocation):
        t = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail.prev.next.next
        t.next = self.head.next
        t.prev = self.head
        t.next.prev = t
        self.head.next = t
        self.body.remove(t.val)
        t.val = newlocation
        self.body.add(newlocation)

    def eatfood(self, newlocation):
        newhead = Node(newlocation)
        newhead.next = self.head.next
        newhead.prev = self.head
        self.head.next = newhead
        newhead.next.prev = newhead
        self.body.add(newlocation)


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):

        self.snake = Snake()

        self.foods = {}
        i = 0
        for f in food:
            self.foods[i] = (f[0], f[1])
            i += 1
        self.foodcounter = 0
        self.board = [[0] * width] * height
        self.movemap = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        self.disablemap = {
            'R': 'L',
            'L': 'R',
            'U': 'D',
            'D': 'U',
        }
        self.disabled = None

    def move(self, direction: str) -> int:

        # the question is not clear how it wants to handle invalid entries... for example if the snake is moving left
        # and you try to immediately do a 180 and turn right... that input is invalid or blocked.
        # the testcase seems to treat it differently though... so to make it pass I had to comment out the below line
        # but imo the testcase is invalid not this line.

        # if direction == self.disabled:
        #     return 0
        self.disabled = self.disablemap[direction]
        head = self.snake.head.next
        newlocation = (head.val[0] + self.movemap[direction][0], head.val[1] + self.movemap[direction][1])
        print(newlocation, self.foods[self.foodcounter])
        if newlocation[0] < 0 or newlocation[0] >= len(self.board):
            return -1
        if newlocation[1] < 0 or newlocation[1] >= len(self.board[0]):
            return -1
        if newlocation in self.snake.body:
            if newlocation != self.snake.tail.prev.val or (
                    newlocation in self.foods and self.foods[newlocation] == self.foodcounter):
                return -1
        if self.foodcounter < len(self.foods) and newlocation == self.foods[self.foodcounter]:
            self.snake.eatfood(newlocation)
            self.foodcounter += 1
        else:
            self.snake.swaptail(newlocation)
        return len(self.snake.body) - 1

