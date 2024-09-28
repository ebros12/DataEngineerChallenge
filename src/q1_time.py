from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict
from time import time

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    start_time = time()
    date_user_count = defaultdict(lambda: defaultdict(int))

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                tweet = json.loads(line)
                tweet_date_str = tweet['date']
                tweet_date = datetime.fromisoformat(tweet_date_str).date()
                tweet_user = tweet['user']['username']
                date_user_count[tweet_date][tweet_user] += 1

        results = []
        for date, users in date_user_count.items():
            top_user = max(users, key=users.get)
            results.append((date, top_user))

        results.sort(key=lambda x: date_user_count[x[0]][x[1]], reverse=True)
        end_time = time()
        print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos")
        return results[:10]

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []
