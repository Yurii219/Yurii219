FROM python:3.10-slim

# Установка библиотек
RUN apt-get update && apt-get install -y \
    && pip install matplotlib pandas

WORKDIR /app

# Копируем все наши файлы в контейнер
COPY . .

# Главная команда: запускает ТЕСТ, потом ГРАФИК, потом ПРОВЕРКУ
CMD ["sh", "-c", "python3 ecu_test.py && python3 visualize_ecu.py && python3 final_gate.py"]