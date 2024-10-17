"""

    lado: int
    cor: str

"""

class Quadrado:
    def __init__(self, lado: int, cor: str):
        self.lado = lado
        self.cor = cor
    
    def area(self):
        area = self.lado * self.lado
        return area
    
    def perimetro(self):
        perimetro=self.lado
        pass
    
    def mudar_cor(self):
        pass