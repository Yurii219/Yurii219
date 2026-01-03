import pandas as pd
import sys
import os

def check_safety():
    print("\n=== ПРОВЕРКА СТАНДАРТОВ БЕЗОПАСНОСТИ ===")
    
    if not os.path.exists("test_report.txt"):
        print("ОШИБКА: Отчет не найден!")
        sys.exit(1)

    # Читаем данные через Pandas
    data = []
    with open("test_report.txt", "r") as f:
        for line in f:
            if "Давление=" in line:
                val = int(line.split("Давление=")[1].split("%")[0])
                data.append(val)
    
    df = pd.DataFrame(data, columns=['Pressure'])
    max_val = df['Pressure'].max()
    failures = len(df[df['Pressure'] > 120]) # Порог опасности

    print(f"Максимальное зафиксированное давление: {max_val}%")
    
    if failures == 0:
        print("РЕЗУЛЬТАТ: [ PASS ] - Система стабильна.")
        sys.exit(0) # Код успеха для Docker
    else:
        print(f"РЕЗУЛЬТАТ: [ FAIL ] - Обнаружено {failures} опасных скачков!")
        print("ВНИМАНИЕ: Требуется доработка алгоритма торможения.")
        sys.exit(1) # Код ошибки

if __name__ == "__main__":
    check_safety()