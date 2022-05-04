class FuerzaBruta:
    
    def __init__(self, goldMine, row, column):
        self.goldMine = goldMine
        self.row = row
        self.column = column
    
    def collectGold(self, goldMine, i, j):
    
        camino = []
        # condicion base
        if ((i < 0) or (i == self.row) or (j == self.column)):  
            return 0, []
    
        # llamada recursiva para arriba adelante
        rightUpperDiagonal, camino1 = self.collectGold(goldMine, i - 1, j + 1)
    
        # llamada recursiva para adelante
        right, camino2 = self.collectGold(goldMine, i, j + 1)
    
        # llamada recursiva para abajo adelante
        rightLowerDiagonal, camino3 = self.collectGold(goldMine, i + 1, j + 1)
    
        # Administra los caminos y el oro para sacar el mas optimo
        totalMaxGold = goldMine[i][j]
        camino.append([i,j])
        maxGold = max(max(rightUpperDiagonal, rightLowerDiagonal), right)
        
        if maxGold == rightUpperDiagonal:
            totalMaxGold += rightUpperDiagonal
            camino += (camino1)
        elif maxGold == rightLowerDiagonal:
            totalMaxGold += rightLowerDiagonal
            camino += (camino3)
        else:
            totalMaxGold += right
            camino += (camino2)
        # Regresa el valor maximo de las 3 llamadas junto al camino transitado
        return totalMaxGold, camino
    
    def getMaxGold(self):
        caminoOptimo = []
        maxGold = 0
    
        for i in range(self.row):
    
            # Llamada recursiva inicial para cada posible inicio
            goldCollected, camino = self.collectGold(self.goldMine, i, 0)
            maxGold = max(maxGold, goldCollected)
            if maxGold == goldCollected:
                caminoOptimo = camino
        return maxGold, caminoOptimo