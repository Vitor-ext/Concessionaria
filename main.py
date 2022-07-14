### Autor: Vitor de Jesus ###
### Projeto: Exemplos de Class, Objetos e Metodos ###
### Data: 13/07/2022 ###

class Carro:
    def __init__(self, categoria, marca, modelo, potencia, combustivel, ano, seguranca, valor):
        self.categoria = categoria
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.combustivel = combustivel
        self.ano = ano
        self.seguranca = seguranca
        self.valor = valor
    pass


print("\nBem vindo !",
      "\nQual Nivel de Carro Deseja:",
      "\n[1] Simples",
      "\n[2] Intermediario",
      "\n[3] Alto Nivel",
      )

var = int(input("\nDigite o numero "))

#while True
if var == 1:
    Palio = Carro('Simples', 'Fiat', 'Fire', '1.0', 'Gasolina', '2008', 'ABS', '20000')
    print ("Seu Novo Carro é um Palio:", Palio.categoria, Palio.marca, Palio.modelo, Palio.potencia, Palio.combustivel, Palio.ano, Palio.seguranca, Palio.valor )

if var == 2:
    IX35 = Carro('Intermediario', 'Hyundai', 'GL', '2.0', 'Flex', '2015', 'ABS + airbag', '80000')
    print ("Seu Novo Carro é um IX35:", IX35.categoria, IX35.marca, IX35.modelo, IX35.potencia, IX35.combustivel, IX35.ano, IX35.seguranca, IX35.valor )

if var == 3:
    X1 = Carro('Alto_Nivel', 'BMW', 'BMW01', '2.5', 'Flex', '2020', 'ABS + airbag', '100000')
    print ("Seu Novo Carro é um X1:", X1.categoria, X1.marca, X1.modelo, X1.potencia, X1.combustivel, X1.ano, X1.seguranca, X1.valor )

if (var !=1) and (var !=2) and (var!=3):
    print ("Opção selecionada é invalida")
