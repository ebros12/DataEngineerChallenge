import json
from collections import Counter
from typing import List, Tuple
import time
import emoji  # Importa la librería emoji
import cProfile
import pstats

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Procesa un archivo de tweets y devuelve las 10 fechas con más tweets,
    junto con el conteo total de tweets en cada una de esas fechas.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene 
        una fecha (como cadena de texto) y el número total de tweets 
        registrados en esa fecha.
    """
    emoji_counter = Counter()

    # Iniciar temporizador
    start_time = time.time()
    
    try:
        # Lectura línea por línea para evitar cargar todo el archivo en memoria
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    tweet = json.loads(line.strip())  # Convertir la línea a JSON
                    content = tweet.get('content', '')  # Obtener el contenido del tweet
                    # Contar solo los emojis en el contenido del tweet
                    emoji_counter.update(c for c in content if emoji.is_emoji(c))
                except json.JSONDecodeError:
                    print(f"Error de decodificación JSON en la línea {line_number}: {line.strip()}")
                except Exception as e:
                    print(f"Error procesando la línea {line_number}: {e}")
    except Exception as e:
        print("Error al leer el archivo:", e)

    # Obtener los 10 emojis más comunes
    top_emojis = emoji_counter.most_common(10)
    elapsed_time = time.time() - start_time  # Calcular tiempo transcurrido

    print(f"Tiempo de ejecución: {elapsed_time:.2f} segundos")
    return top_emojis

def main(file_path: str):
    # Usar cProfile para medir el rendimiento de la función
    profiler = cProfile.Profile()
    profiler.enable()  # Habilitar el profiler
    
    result = q2_time(file_path)  # Llamar a la función que quieres perfilar
    
    profiler.disable()  # Deshabilitar el profiler

    # Imprimir las estadísticas de rendimiento
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative')  # Ordenar por tiempo acumulativo
    stats.print_stats()  # Imprimir estadísticas

    return result

if __name__ == "__main__":
    file_path = "ruta/al/archivo.json"  # Cambia esto a la ruta de tu archivo
    main(file_path)
