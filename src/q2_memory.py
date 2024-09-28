from collections import Counter
from typing import List, Tuple
import json
import emoji  # Importa la librería emoji

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
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

    """ Utilizando el counter """

    try:
        # Lectura línea por línea para optimizar el uso de memoria
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

    # Devolver los 10 emojis más comunes
    return emoji_counter.most_common(10)
