
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano
    def fazer_chamada(self, destinatario, parametro):
        self.destinatario = destinatario
        self.parametro = parametro

        
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    def custo_chamada(self, tempo):
        self.tempo = tempo
        tempo =  float(tempo) * 0.10
        return tempo
    def deduzir_saldo(self, custo_reais, saldo_atual, ligando_para):
        self.saldo_atual = saldo_atual
        self.custo_reais = custo_reais
        self.ligando_para = ligando_para
        if custo_reais > saldo_atual:
            return "Saldo insuficiente para fazer a chamada."
        else:
            soma = saldo_atual - custo_reais
            return f"Chamada para {ligando_para} realizada com sucesso. Saldo: ${soma}0"


nome = input()
numero = input()
saldo_inicial = float(input())

destinatario = input()
duracao = int(input())

planos = Plano(saldo_inicial)

custo = planos.custo_chamada(duracao)

resultado = planos.deduzir_saldo(custo, saldo_inicial, destinatario)

print(resultado)
