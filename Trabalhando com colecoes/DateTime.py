from datetime import datetime, timedelta, timezone

# Data e hora atual (local)
agora = datetime.now()
print("Data e hora local:", agora.strftime("%d/%m/%Y %H:%M:%S"))

# Data e hora UTC
agora_utc = datetime.utcnow()
print("Data e hora UTC:", agora_utc.strftime("%d/%m/%Y %H:%M:%S"))

# Criando fuso horário manualmente (ex: São Paulo = UTC-3)
fuso_utc_menos_3 = timezone(timedelta(hours=-3))
agora_sp = datetime.now(fuso_utc_menos_3)
print("Data e hora com fuso horário UTC-3 (São Paulo):", agora_sp.strftime("%d/%m/%Y %H:%M:%S"))

# Adicionando 1 dia à data atual
amanha = agora + timedelta(days=1)
print("Data de amanhã:", amanha.strftime("%d/%m/%Y %H:%M:%S"))

# Subtraindo 2 horas
duas_horas_atras = agora - timedelta(hours=2)
print("Duas horas atrás:", duas_horas_atras.strftime("%d/%m/%Y %H:%M:%S"))
