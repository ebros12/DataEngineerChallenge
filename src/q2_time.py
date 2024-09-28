import json
from collections import Counter
from typing import List, Tuple
import time
import emoji  # Importa la librería emoji

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    """ Utilizando el counter """
    
    start_time = time.time()  # Iniciar temporizador
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
