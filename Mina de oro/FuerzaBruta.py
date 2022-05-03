class FuerzaBruta:
    
    def __init__(self, goldMine, row, column):
        self.goldMine = goldMine
        self.row = row
        self.column = column
    
    def collectGold(self, goldMine, i, j):
    
        # condicion base
        if ((i < 0) or (i == self.row) or (j == self.column)):  
            return 0
    
        # llamada recursiva para arriba adelante
        rightUpperDiagonal = self.collectGold(goldMine, i - 1, j + 1)
    
        # llamada recursiva para adelante
        right = self.collectGold(goldMine, i, j + 1)
    
        # llamada recursiva para abajo adelante
        rightLowerDiagonal = self.collectGold(goldMine, i + 1, j + 1)
    
        # Regresa el valor maximo de las 3 llamadas
        return  goldMine[i][j] + max(max(rightUpperDiagonal, rightLowerDiagonal), right)  
    
    
    def getMaxGold(self):
    
        maxGold = 0
    
        for i in range(self.row):
    
            # Llamada recursiva inicial para cada posible inicio
            goldCollected = self.collectGold(self.goldMine, i, 0)
            maxGold = max(maxGold, goldCollected)
    
        return maxGold