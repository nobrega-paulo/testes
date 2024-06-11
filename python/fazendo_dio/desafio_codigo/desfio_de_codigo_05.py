#class PlanoTelefone:
#    def __init__(self, nome, saldo):#
#        self.nome = nome
#        self.saldo = saldo
#    def __str__(self):#
#        if self.nome < 10:
#            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
#        elif saldo_inicial >= 50:
#            return "Parabéns! Continue aproveitando seu plano sem preocupações."
#        else:
#            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
 
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())
def calcular_saldo(saldo):
    if saldo < 10:
        return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
    elif saldo_inicial >= 50:
        return "Parabéns! Continue aproveitando seu plano sem preocupações."
    else:
        return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
mensagem_usuario = calcular_saldo(saldo_inicial)

print(mensagem_usuario)