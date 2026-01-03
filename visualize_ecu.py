import matplotlib.pyplot as plt
import pandas as pd
import os
import time

def analyze_ecu_data():
    # Подождем секунду, чтобы файл точно записался на диск
    time.sleep(1)
    
    if not os.path.exists("test_report.txt"):
        print("ОШИБКА: Файл test_report.txt не найден внутри контейнера!")
        return
# ... (дальше остальной код без изменений)

def analyze_ecu_data():
    data = []
    # Читаем файл, который создал ecu_test.py
    try:
        with open("test_report.txt", "r") as f:
            for line in f:
                if "Давление=" in line:
                    # Извлекаем числовое значение давления
                    val = int(line.split("Давление=")[1].split("%")[0])
                    data.append(val)
        
        # Создаем таблицу Pandas
        df = pd.DataFrame(data, columns=['Pressure'])
        
        # Вычисляем инженерные метрики
        stats = {
            "Среднее": df['Pressure'].mean(),
            "Максимум": df['Pressure'].max(),
            "Сбои (>100%)": len(df[df['Pressure'] > 100])
        }

        # Печатаем аналитику в консоль Docker
        print("\n=== ИНЖЕНЕРНЫЙ ОТЧЕТ vECU ===")
        for key, value in stats.items():
            print(f"{key}: {value:.2f}")
        print("============================\n")

        # Строим график
        plt.figure(figsize=(12, 6))
        plt.plot(df['Pressure'], color='blue', linewidth=2, label='Тормозное давление')
        plt.axhline(y=100, color='red', linestyle='--', label='Предел безопасности')
        plt.fill_between(range(len(df)), df['Pressure'], 100, where=(df['Pressure'] > 100), color='red', alpha=0.3)
        plt.title(f"Анализ 50 тестов тормозной системы\n(Сбоев: {stats['Сбои (>100%)']})")
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.savefig("ecu_chart.png")
        
    except Exception as e:
        print(f"Ошибка аналитики: {e}")

if __name__ == "__main__":
    analyze_ecu_data()