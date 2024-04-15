class conta_bancaria:
    def __init__(self, titular, saldo, limite, numero, status):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.numero = numero
        self.status = status
        self.senha = None

    def sacar(self, valor):
        senha = input("Digite sua senha para sacar: ")
        if senha == self.senha:
            if self.status == "ativo":
                if valor <= self.saldo:
                    self.saldo -= valor
                    print(f'Um saque de {valor} foi realizado. Seu novo saldo é: {self.saldo}')
                else:
                    print("Saldo insuficiente.")
            else:
                print("Essa conta está bloqueada. Não é possível sacar.")
        else:
            print("Senha incorreta. Operação cancelada.")

    def depositar(self, valor):
        senha = input("Digite sua senha para depositar: ")
        if senha == self.senha:
            if self.status == 'ativo':
                self.saldo += valor
                print(f'Depósito de {valor} realizado. Seu novo saldo é: {self.saldo}')
            else:
                print("Essa conta está bloqueada. Não é possível depositar.")
        else:
            print("Senha incorreta. Operação cancelada.")

    def bloquear(self):
        senha = input("Digite sua senha para bloquear a conta: ")
        if senha == self.senha:
            self.status = "bloqueado"
            print("A conta foi bloqueada.")
        else:
            print("Senha incorreta. Operação cancelada.")

    def desbloquear(self):
        senha = input("Digite a senha para desbloquear a conta: ")
        if senha == self.senha:
            self.status = "ativo"
            print("Conta desbloqueada.")
        else:
            print("Senha incorreta. Conta permanece bloqueada.")

    def definir_senha(self):
        senha = input("Digite uma senha para a conta: ")
        self.senha = senha
        print("Senha definida com sucesso.")

    def verificar(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)
        print("Limite:", self.limite)
        print("Número:", self.numero)
        print("Status:", self.status)

    def mudar_limite(self, novo_limite):
        senha = input("Digite sua senha para alterar o limite: ")
        if senha == self.senha:
            if self.status == "ativo":
                self.limite = novo_limite
                print("Limite alterado para", novo_limite)
            else:
                print("Conta bloqueada. Não é possível alterar o limite.")
        else:
            print("Senha incorreta. Operação cancelada.")

    def ver_limite(self):
        print("Limite da conta:", self.limite)


conta = conta_bancaria('nicolas', 1200, 700, 3456, 'ativo')
conta.verificar()
conta.definir_senha()
conta.bloquear()
conta.desbloquear()
conta.mudar_limite()
conta.ver_limite()
