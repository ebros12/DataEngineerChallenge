from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter
from memory_profiler import profile

""" Importaciones necesarias """

@profile
def q1_memory(file_path: str, block_size: int = 1024) -> List[Tuple[datetime.date, str]]:
    
    """ 
    Procesa un archivo de tweets y devuelve las 10 fechas con más tweets,
    junto con el usuario más activo en cada una de esas fechas.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.
        block_size (int): Tamaño del bloque de líneas a leer.

    Returns:
        List[Tuple[datetime.date, str]]: Lista de tuplas donde cada tupla contiene 
        una fecha y el nombre de usuario que más tweets tiene en esa fecha.
    """
    
    date_user_count = {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            while True:
                # Lee un bloque de líneas
                lines = [f.readline() for _ in range(block_size)]
                if not lines:  # Salir si no hay más líneas
                    break
                for line in lines:
                    tweet = json.loads(line)  # Convierte la línea JSON a un objeto Python
                    tweet_date_str = tweet['date']  # Extrae la fecha del tweet
                    tweet_date = datetime.fromisoformat(tweet_date_str).date()  # Convierte la cadena de fecha a un objeto date
                    tweet_user = tweet['user']['username']  # Extrae el nombre de usuario
                    
                    # Filtra aquí si es necesario
                    if tweet_date and tweet_user:  # Filtra solo si hay fecha y usuario
                        if tweet_date not in date_user_count:
                            date_user_count[tweet_date] = Counter()
                        date_user_count[tweet_date][tweet_user] += 1  # Incrementa el conteo de tweets para el usuario

        results = []
        for date, users in date_user_count.items():
            top_user = users.most_common(1)[0][0]  # Encuentra el usuario con más tweets en la fecha
            results.append((date, top_user))

        # Ordena los resultados por la cantidad de tweets en orden descendente y devuelve las 10 primeras
        results.sort(key=lambda x: date_user_count[x[0]][x[1]], reverse=True)
        return results[:10]

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []
