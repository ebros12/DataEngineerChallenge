from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict, Counter  # Asegúrate de importar Counter aquí
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
    
    # Estructuras de datos para contar tweets por fecha y usuario
    date_user_count = defaultdict(Counter)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                tweet = json.loads(line)
                tweet_date_str = tweet['date']
                tweet_date = datetime.fromisoformat(tweet_date_str).date()
                tweet_user = tweet['user']['username']
                
                # Contar tweets por fecha y usuario
                date_user_count[tweet_date][tweet_user] += 1

        # Obtener los 10 fechas con más tweets y el usuario más activo en cada fecha
        results = []
        for date, user_counter in date_user_count.items():
            # Encontrar el usuario más activo de la fecha
            top_user = user_counter.most_common(1)[0][0]  # Obtener el usuario más activo
            results.append((date, top_user))
        
        # Ordenar los resultados por la cantidad de tweets por fecha
        results.sort(key=lambda x: date_user_count[x[0]][x[1]], reverse=True)
        return results[:10]
    
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []
