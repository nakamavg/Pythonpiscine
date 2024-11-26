import time
from datetime import datetime, timezone

# Obtener el tiempo actual
current_time = time.time()
decimal_anotation = "{:,.4f}".format(current_time)
scientific_anotation = "{:.2e}".format(current_time)

# Imprimir los segundos desde el Epoch con 4 decimales y en notación científica
print(f"Seconds since January 1, 1970: {decimal_anotation} or {scientific_anotation} in scientific notation$")

# Formatear la fecha como "Nov 26" usando un objeto timezone-aware
formatted_date = datetime.fromtimestamp(current_time, tz=timezone.utc).strftime('%b %d')
print(formatted_date)
