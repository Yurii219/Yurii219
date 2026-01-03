import time
import random

def brake_system_test():
    # Создаем (или очищаем) файл отчета
    with open("test_report.txt", "w") as report:
        report.write("=== ОТЧЕТ О ТЕСТИРОВАНИИ vECU ===\n")
        report.write(f"Время запуска: {time.ctime()}\n")
        report.write("-" * 30 + "\n")

        # Прогоняем 20 тестов с расширенным диапазоном (ищем аномалии)
        for i in range(1, 51):
            pedal_pressure = random.randint(20, 90) # Имитируем и ошибки датчика
            
            # Логика принятия решения
            if pedal_pressure < 0 or pedal_pressure > 100:
                result = "ERROR: Некорректные данные датчика!"
            elif pedal_pressure > 80:
                result = "ACTION: Экстренное торможение (ABS Active)"
            elif pedal_pressure > 10:
                result = "ACTION: Торможение в штатном режиме"
            else:
                result = "IDLE: Тормоза не задействованы"

            # Формируем строку лога
            log_entry = f"Тест #{i:02}: Давление={pedal_pressure}% -> {result}\n"
            
            # Пишем и в консоль, и в файл
            print(log_entry.strip())
            report.write(log_entry)
            time.sleep(0.1) # Ускорили тест!

        report.write("-" * 30 + "\n")
        report.write("Тестирование завершено успешно.")

if __name__ == "__main__":
    brake_system_test()