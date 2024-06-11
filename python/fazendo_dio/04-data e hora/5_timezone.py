from datetime import datetime, timezone, timedelta

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data2_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_oslo)
print(data2_sao_paulo)