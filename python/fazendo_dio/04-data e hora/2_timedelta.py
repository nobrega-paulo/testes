from datetime import timedelta, datetime
tipo_carro = 'g'
tempo_pequeno = 30
tempo_media = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'p':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou as :{data_atual} e ficara pronto as {data_estimada}")
elif tipo_carro == 'm':
    data_estimada = data_atual + timedelta(minutes=tempo_media)
    print(f"O carro chegou as :{data_atual} e ficara pronto as {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou as :{data_atual} e ficara pronto as {data_estimada}") 