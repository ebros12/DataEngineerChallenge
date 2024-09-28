import json
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:

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
    return top_users
