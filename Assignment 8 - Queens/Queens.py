class Board:
    EMPTY = '*'
    QUEEN = 'Q'
    NEWLINE = '\n'
    SPACE = ' '
    
    def __init__(self, n, solution):
        self.n = n
        self.grid = {}
        for row in range(n):
            for col in range(n):
                if col == solution[row]:
                    self.grid[row,col] = self.QUEEN
                else:
                    self.grid[row,col] = self.EMPTY

    def __str__(self):
        string = ''
        for row in range(self.n):
            for col in range(self.n):
                string += self.grid[row,col] + self.SPACE
            string += self.NEWLINE
        return string


class QueensProblem():
    NEWLINE = '\n'
    SPACE = ' '
    
    def __init__(self, n):
        self.size = n
        self.solution = [None] * self.size
        self.solutions = []
        
    def __str__(self):
        string = ''
        for i, solution in enumerate(self.solutions):
            string += 'Solution #' + str(i+1)
            string += self.NEWLINE
            string += str(solution)
            string += self.NEWLINE
        return string
    
    def isValidPlace(self, row, col):
        for i in range(row):
            if ((self.solution[i] == col) or (abs(i-row) == abs(self.solution[i]-col))):
                return False
        return True

    def solve(self, x):
        for i in range(self.size):
            if self.isValidPlace(x, i):
                self.solution[x] = i
                if x == self.size - 1:
                    self.solutions.append(Board(self.size, self.solution))
                self.solve(x + 1)
            
def main():
    while True:
        try:
            n = int(input('Enter the size of the square board: '))
            if n < 4:
                raise Exception
            print()
            break
        except Exception:
            print('Invalid input.')
            
    game = QueensProblem(n)
    game.solve(0);
    print(game)
    
main()

    
