import json
from collections import Counter
from typing import List, Tuple
from memory_profiler import profile  # Importa memory-profiler

@profile
def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Procesa un archivo de tweets y devuelve las 10 menciones (@usuario) más comunes
    que aparecen en el contenido de los tweets.

    Args:
        file_path (str): Ruta al archivo JSON que contiene los tweets.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene 
        un nombre de usuario mencionado y su frecuencia (como entero).
    """
    user_counter = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    tweet = json.loads(line.strip())
                    content = tweet.get('content', '')
                    # Contar menciones (@usuario)
                    mentions = [word[1:] for word in content.split() if word.startswith('@')]
                    user_counter.update(mentions)
                except json.JSONDecodeError:
                    print(f"Error de decodificación JSON en la línea {line_number}: {line.strip()}")
                except Exception as e:
                    print(f"Error procesando la línea {line_number}: {e}")
    
    except Exception as e:
        print("Error al leer el archivo:", e)

    # Devolver los 10 usuarios más mencionados
    return user_counter.most_common(10)
