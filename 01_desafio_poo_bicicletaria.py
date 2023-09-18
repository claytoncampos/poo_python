class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("brumm")

    def correr(self):
        print("Vrummm")

    def parar(self):
        print("parando")
        print("parada")

#    def __str__(self) -> str:
#        return f"Bicileta: {self.cor}, {self.ano}, {self.modelo}, {self.valor}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    
b1 = Bicicleta("preta","caloi",2000,222)
b1.buzinar()
b1.correr()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo,b1.valor, b1.ano)

print(b1)