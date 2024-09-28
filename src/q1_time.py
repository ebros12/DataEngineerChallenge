from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
from time import time

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Cuenta el número de menciones de usuarios por fecha y devuelve 
    los 10 usuarios más mencionados por cada fecha.
    
    Parameters:
    file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
    List[Tuple[datetime.date, str]]: Lista de tuplas con las fechas y 
    los usuarios más mencionados.
    """
    start_time = time()
    date_user_count = defaultdict(lambda: defaultdict(int))

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    tweet = json.loads(line)
                    tweet_date_str = tweet['date']
                    tweet_date = datetime.fromisoformat(tweet_date_str).date()
                    tweet_user = tweet['user']['username']
                    date_user_count[tweet_date][tweet_user] += 1
                except json.JSONDecodeError:
                    print(f"Error de decodificación JSON en la línea {line_number}: {line.strip()}")
                except KeyError as e:
                    print(f"Campo faltante en la línea {line_number}: {e}")
                except Exception as e:
                    print(f"Error procesando la línea {line_number}: {e}")

        # Recopilar resultados
        results = [
            (date, max(users, key=users.get))
            for date, users in date_user_count.items()
        ]

        # Ordenar los resultados por la cantidad de menciones
        results.sort(key=lambda x: date_user_count[x[0]][x[1]], reverse=True)
        end_time = time()
        print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
        return results[:10]

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []
