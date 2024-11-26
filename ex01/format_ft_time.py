import time
from datetime import datetime, timezone

# Obtener el tiempo en segundos desde Epoch (1 de enero de 1970)
current_time = time.time()

# Imprimir en formato decimal completo
#.4f indica que se imprimirán 4 decimales
#.2e indica que se imprimirá en notación científica con 2 decimales
print(f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation")

# Formatear fecha y hora legibles usando objetos de fecha y hora con conocimiento de zona horaria
formatted_time = datetime.fromtimestamp(current_time, tz=timezone.utc).strftime('%b %d')
print(formatted_time)