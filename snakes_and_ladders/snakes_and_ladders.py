import random

JUMP = { 4:16, 12:33, 18:22, 21: 3, 24: 7, 26:37, 35: 9, 42:61,
        49:51, 50:11, 53:15, 55:74, 60:23, 75:44, 82:98, 85:95,
        88:92, 89:48, 93:25, 97:65, 99:58}
FIRST, LAST = 1, 100

def run_game():
    position = FIRST
    num_moves = 0
    while position < LAST:
        num_moves += 1
        dice_throw = random.randint(1, 6)
        position += dice_throw
        print('%d: dice(%d) -> %d' % (num_moves, dice_throw, position))
        if position in JUMP:
            position = JUMP[position]
            print('%d: jump -> %d' % (num_moves, position))
    print('game over')
    
def run_games(num_games):
    random.seed()
    for n in range(0, num_games):
        run_game()

if __name__ == "__main__":
    run_games(1)
