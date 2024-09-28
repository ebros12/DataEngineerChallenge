import cProfile
from q1_memory import q1_memory
from q1_time import q1_time

if __name__ == '__main__':
    file_path = "src/farmers-protest-tweets-2021-2-4.json"
    
    print("Resultados de q1_memory:")
    cProfile.run(f'q1_memory("{file_path}")')
    
    print("\nResultados de q1_time:")
    cProfile.run(f'q1_time("{file_path}")')
