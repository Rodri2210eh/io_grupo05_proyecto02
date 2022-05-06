
class Dinamico:
    
    def __init__(self, goldMine, row, column):
        self.goldMine = goldMine
        self.row = row
        self.column = column
    
    def collectGold(self, gold, i, j, register, caminosOptimos):
        '''
        Metodo auxiliar para recorrer la matriz por medio de recursividad y obtiene el camino y el maximo de oro por llamada
        registra el camino y los maximos de oro ya obtenidos con anterioridad, esto para evitar calcular nuevamente rutas o valores
        de manera innecesaria
        '''
        # Base condition.
        if ((i < 0) or (i == self.row) or (j == self.column)):
            currentPath = []
            return 0, currentPath
    
        if(register[i][j] != -1):
            return register[i][j], caminosOptimos[i][j]
    
        # Right upper diagonal
        rightUpperDiagonal, camino1 = self.collectGold(gold, i - 1, j + 1, register, caminosOptimos)
    
        # right
        right, camino2 = self.collectGold(gold, i, j + 1, register, caminosOptimos)
    
        # Lower right diagonal
        rightLowerDiagonal, camino3 = self.collectGold(gold, i + 1, j + 1, register, caminosOptimos)
    
        # Return the maximum and store the value
        actualGold = gold[i][j]
        currentPath = [[i, j]]
        
        maximoObtenido = max(max(rightUpperDiagonal, rightLowerDiagonal), right)
        if maximoObtenido == rightUpperDiagonal:
            register[i][j] = actualGold + rightUpperDiagonal
            if camino1 != []:
                caminosOptimos[i][j] = currentPath + camino1
            else:
                caminosOptimos[i][j] = currentPath
        elif maximoObtenido == rightLowerDiagonal:
            register[i][j] = actualGold + rightLowerDiagonal
            if camino3 != []:
                caminosOptimos[i][j] = currentPath + camino3
            else:
                caminosOptimos[i][j] = currentPath
        else:
            register[i][j] = actualGold + right
            if camino2 != []:
                caminosOptimos[i][j] = currentPath + camino2
            else:
                caminosOptimos[i][j] = currentPath
        return register[i][j], caminosOptimos[i][j]
    
    
    def getMaxGold(self):
        '''
        inicializa la matriz de registro de oro y la matriz de registro de caminos optimos
        recorre las filas obteniendo el maximo de oro
        regresa el maximo de oro y su camino
        '''
        maxGold = 0
        caminoAlOro = []
        # Initialize the vector register
        register = [[-1 for i in range(self.column)]for j in range(self.row)]
        CaminosOptimos = [[-1 for i in range(self.column)]for j in range(self.row)]
        for i in range(self.row):
            # Recursive function call for  ith row.
            goldCollected, caminoProbable = self.collectGold(self.goldMine, i, 0, register, CaminosOptimos)
            maxGold = max(maxGold, goldCollected)
            if maxGold == goldCollected:
                caminoAlOro = caminoProbable
        return maxGold, caminoAlOro