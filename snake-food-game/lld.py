# Snake Food Game

# 1. We have a game board (N*N)
# 2. We have a snake, moves up down, left and right and eats food
# 3. we have different kinds of food items
# 4. We have a human player controlling snake

# Game complete
# 1. Snake collides with itself
# 2. Score is displayed

class Food:
    def __init__(self, name, position, points):
        self.name = name
        self.position = position
        self.points = points

class Player:
    def __init__(self, name):
        self.name = name

class FoodFactory:
    def create_food(self, food_type):
        if food_type == "apple":
            return Food("apple", 1)
        if food_type == "poisnous":
            return Food("poisnous", -1)
        else:
            raise ValueError("Unknown food type")

class PlayerFactory:
    def create_player(self, player_type, name):
        if player_type == "human":
            return Player(name)
        elif player_type == "ai":
            return Player("AI Player")
        else:
            raise ValueError("Unknown player type")
        
from abc import ABC, abstractmethod
class PlayerStrategy:
    @abstractmethod
    def move(ABC):
        pass

class HumanPlayerStrategy(PlayerStrategy):
    def __init__(self, player):
        self.player = player

    def move(self, current_pos):
        input_ = input("Provide input as W, A, S, D")
        row, col = current_pos
        match input_:
            case 'W':
                return row + 1, col
            case 'A':
                return row, col - 1 
            case 'S':
                return row - 1, col
            case 'D':
                return row, col + 1
            
from collections import deque 
class Snake:
    def __init__(self, pos):
        self.snake = deque()
        self.snake.append(pos)
        self.snake_set = set()
        self.snake_set.add(pos)


class Board:
    def __init__(self, size):
        self.board = [['' for _ in range(size)] for _ in range(size)]

class BoardGame:
    def play():
        pass


class SnakeGame(BoardGame):
    def __init__(self, food, size):
        self.board = Board(size)
        self.size = size
        self.snake = Snake((0,0))
        self.player = PlayerFactory.create_player("human", "Rachit")
        self.food = food

    def play(self):
        while True:
            row, col = HumanPlayerStrategy(self.player).move(self.snake[len(self.snake)])


            #validation - boundary collision
            if min(row, col) < 0 or row >= self.size or col >= self.size:
                print("score : ", self.player.points)
                break

            #validation - self collision
            if (row, col) in self.snake.snake_set:
                #collision detected
                print("score : ", self.player.points)
                break

            if (row, col) == self.food[0]:
                top_food = self.food.popleft()
                self.snake.snake.append(top_food)
                self.snake.snake_set.add(top_food)
                self.player.points += 1
            else:
                self.snake.snake.append((row, col))
                self.snake.snake_set.add((row, col))
                val = self.snake.snake.popleft()
                self.snake.snake_set.remove(val)

            if self.food():
                break





            



#main():

food1 = FoodFactory("apple")
food2 = FoodFactory("apple")
SnakeGame([food1, food2]).play()