def recomendar_plano(valor_mensal):
        if valor_mensal <= 10:
            return "Plano Essencial Fibra-50Mbps"
        elif (valor_mensal > 10) and (valor_mensal <= 20):
            return "Plano Prata Fibra-100Mbps"
        else:
            return "Plano Premium Fibra-300Mbps"
print("Informe o consumo mensal de dados em GB: ")
consumo = float(input())

print(recomendar_plano(consumo))
