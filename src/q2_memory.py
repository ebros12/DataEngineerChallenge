import json
import emoji
from collections import Counter
from typing import List, Tuple
from memory_profiler import profile
import re

# Compilar una expresión regular para detectar emojis
EMOJI_PATTERN = re.compile('|'.join(re.escape(e) for e in emoji.EMOJI_DATA.keys()))

@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Procesa un archivo de tweets y devuelve los 10 emojis más comunes
    junto con su frecuencia.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene 
        un emoji (como cadena de texto) y el número total de veces que 
        aparece en los tweets.
    """
    emoji_counter = Counter()  # Usar Counter para el conteo

    try:
        # Lectura línea por línea para optimizar el uso de memoria
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:  # Ignorar líneas vacías
                    continue

                try:
                    tweet = json.loads(line)  # Convertir la línea a JSON
                    content = tweet.get('content', '')  # Obtener el contenido del tweet

                    # Encontrar y contar emojis directamente
                    emojis_found = EMOJI_PATTERN.findall(content)
                    emoji_counter.update(emojis_found)  # Actualiza el contador

                except json.JSONDecodeError:
                    continue  # Ignorar errores de decodificación
                except Exception as e:
                    continue  # Ignorar otros errores
                
                # Mensaje de depuración cada 10,000 líneas
                if line_number % 10000 == 0:
                    print(f"Líneas procesadas: {line_number}")

    except Exception as e:
        print("Error al leer el archivo:", e)

    # Obtener los 10 emojis más comunes
    top_emojis = emoji_counter.most_common(10)
    return top_emojis


