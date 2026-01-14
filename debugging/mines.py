#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.total_cells = width * height
        self.num_mines = mines

    def print_board(self, reveal=False):
        clear_screen()
        print('    ' + ' '.join(f"{i:<1}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:<2} ", end=' ') 
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True 
        
        if (y * self.width + x) in self.mines:
            return False 
        
        if self.revealed[y][x]:
            return True 
            
        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        hidden_count = sum(row.count(False) for row in self.revealed)
        return hidden_count == self.num_mines

    def play(self):
        while True:
            self.print_board()
            if self.check_win():
                print("Congratulations! You've cleared the field!")
                break
            try:
                x = int(input("Enter x (column): "))
                y = int(input("Enter y (row): "))
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()