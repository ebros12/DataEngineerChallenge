import json
from collections import Counter
from typing import List, Tuple
import time
import cProfile
import pstats

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Procesa un archivo de tweets y devuelve las 10 palabras más comunes
    que aparecen en el contenido de los tweets.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene 
        una palabra (como cadena de texto) y su frecuencia (como entero).
    """

    user_counter = Counter()
    start_time = time.time()  # Iniciar temporizador

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    tweet = json.loads(line.strip())
                    content = tweet.get('content', '')
                    # Contar menciones (@)
                    mentions = [word[1:] for word in content.split() if word.startswith('@')]
                    user_counter.update(mentions)
                except json.JSONDecodeError:
                    continue  # Ignorar líneas que no se pueden decodificar
                except Exception as e:
                    print(f"Error procesando la línea: {e}")

    except Exception as e:
        print("Error al leer el archivo:", e)

    top_users = user_counter.most_common(10)
    elapsed_time = time.time() - start_time  # Calcular tiempo transcurrido
    print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")
    return top_users

def main(file_path: str):
    # Usar cProfile para medir el rendimiento de la función
    profiler = cProfile.Profile()
    profiler.enable()  # Habilitar el profiler
    
    result = q3_time(file_path)  # Llamar a la función que quieres perfilar
    
    profiler.disable()  # Deshabilitar el profiler

    # Imprimir las estadísticas de rendimiento
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')  # Ordenar por tiempo acumulativo
    stats.print_stats()  # Imprimir estadísticas

    return result

