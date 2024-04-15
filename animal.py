class Animal:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor

    def emitir_som(self):
        pass

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Cor: {self.cor}")


class Cachorro(Animal):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade, cor)
        self.raca = raca

    def emitir_som(self):
        return 'Au Au'

    def pedir_para_brincar(self):
        return f"{self.nome} está pedindo para brincar."


cachorro1 = Cachorro("Beto", 4, "Marrom", "Labrador")
cachorro1.info()
print(cachorro1.emitir_som())
print(cachorro1.pedir_para_brincar())


class Gato(Animal):
    def __init__(self, nome, idade, cor, pelagem):
        super().__init__(nome, idade, cor)
        self.pelagem = pelagem

    @property
    def emitir_som(self):
        return 'Miau'

    def pedir_carinho(self):
        return f"{self.nome} está pedindo carinho."


Gato1 = Gato("princes", 4, "cinza", "lisa")
print(f"{Gato1.nome}: {Gato1.emitir_som}")
print(Gato1.pedir_carinho())

