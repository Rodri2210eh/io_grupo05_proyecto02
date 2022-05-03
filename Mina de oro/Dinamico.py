
class Dinamico:
    
    def __init__(self, goldMine, row, column):
        self.goldMine = goldMine
        self.row = row
        self.column = column
    
    def collectGold(self, gold, i, j, register):
        
        # Base condition.
        if ((i < 0) or (i == self.row) or (j == self.column)):
            return 0
    
        if(register[i][j] != -1):
            return register[i][j]
    
        # Right upper diagonal
        rightUpperDiagonal = self.collectGold(gold, i - 1, j + 1, register)
    
            # right
        right = self.collectGold(gold, i, j + 1, register)
    
        # Lower right diagonal
        rightLowerDiagonal = self.collectGold(gold, i + 1, j + 1, register)
    
        # Return the maximum and store the value
        register[i][j] = gold[i][j] + max(max(rightUpperDiagonal, rightLowerDiagonal), right)
        return register[i][j]
    
    
    def getMaxGold(self):
    
        maxGold = 0
        # Initialize the vector register
        register = [[-1 for i in range(self.column)]for j in range(self.row)]
        
        for i in range(self.row):
    
            # Recursive function call for  ith row.
            goldCollected = self.collectGold(self.goldMine, i, 0, register)
            maxGold = max(maxGold, goldCollected)
    
        return maxGold