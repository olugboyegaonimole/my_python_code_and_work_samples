print("hello")

import random

snakePos = [100,50]
snakePos[0] +=10


snakeBody = [[100,50], [90,50], [80,50]]
print(snakeBody)

snakeBody.insert(0, list(snakePos))
print(snakeBody)

snakeBody.pop()
print(snakeBody)