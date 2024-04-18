class pessoa:
    def __init__(self, nome, idade, peso, altura, genero):
        self.genero = genero
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.ocupado = False

    def falar(self, mensagem):
        if self.ocupado:
            print(f"{self.nome} no momento não pode falar")
        else:
            print(f"{self.nome} pergunta:{mensagem}")

    def comer(self, alimento):
        if not self.ocupado:
            print(f"{self.nome}, esta comendo um(a) {alimento}")
            self.ocupado = True
        else:
            print(f"{self.nome} no momento nao poderar comer")

    def andar(self, metros):
        if not self.ocupado:
            print(f"{self.nome} vai andar {metros} metros")
            self.ocupado = True
        else:
            print(f"{self.nome} no momento não podera andar, pois esta ocupado")

    def dormir(self, horas):
        if not self.ocupado:
            print(f"{self.nome} vai dormir as {horas} horas")
            self.ocupado = True
        else:
            print(f"{self.nome} no momento não posso dormir")


pessoa1 = pessoa("alesandra", 34, 65, 1.5, "feminino")
pessoa1.falar("Olá,como você está?")
pessoa1.comer("salada")
pessoa1.andar(30)
pessoa1.dormir(8)
pessoa2 = pessoa("andre", 12, 45, 1.6, "masculino")
pessoa2.falar("Olá, como vc esta?")
pessoa2.comer("hanburquer")
pessoa2.andar(40)
pessoa2.dormir(9)
