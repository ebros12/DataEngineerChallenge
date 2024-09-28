from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from memory_profiler import profile

@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Procesa un archivo de tweets y devuelve las 10 fechas con más tweets,
    junto con el usuario más activo en cada una de esas fechas.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[datetime.date, str]]: Lista de tuplas donde cada tupla contiene 
        una fecha y el nombre de usuario que más tweets tiene en esa fecha.
    """
    
    date_user_count = Counter()  # Usar Counter para contar usuarios por fecha
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                tweet = json.loads(line)
                tweet_date_str = tweet['date']
                tweet_date = datetime.fromisoformat(tweet_date_str).date()
                tweet_user = tweet['user']['username']
                
                # Se utiliza un tuple (fecha, usuario) para contar
                date_user_count[(tweet_date, tweet_user)] += 1
        
        # Agrupamos resultados por fecha y encontramos el usuario más activo
        results = []
        date_counter = Counter()  # Para contar tweets por fecha
        for (date, user), count in date_user_count.items():
            date_counter[date] += count  # Sumar el conteo de tweets por fecha
            if user not in [u for d, u in results if d == date]:  # Asegura que solo se agregue el usuario más activo
                results.append((date, user))

        # Encontrar el usuario más activo para cada fecha
        final_results = []
        for date in date_counter:
            top_user = max([(user, date_user_count[(date, user)]) for user in results if user[0] == date], key=lambda x: x[1])[0]
            final_results.append((date, top_user))
        
        # Ordenar los resultados y devolver las 10 primeras fechas
        final_results.sort(key=lambda x: date_counter[x[0]], reverse=True)
        return final_results[:10]
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []
