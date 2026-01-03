#!/bin/bash

# Цвета для терминала
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo "--- Сборка и запуск системы ---"
rm -rf results && mkdir -p results

sudo docker build -t my-ecu-test .
sudo docker run --name test_run my-ecu-test

# Сохраняем результат выполнения контейнера (0 - успех, 1 - провал)
RESULT=$?

echo "--- Копирование артефактов ---"
sudo docker cp test_run:/app/test_report.txt ./results/ 2>/dev/null
sudo docker cp test_run:/app/ecu_chart.png ./results/ 2>/dev/null
sudo docker rm test_run

# Финальный вердикт с цветовой индикацией
echo -e "\n======================================="
if [ $RESULT -eq 0 ]; then
    echo -e "${GREEN}СТАТУС РЕЛИЗА: ОДОБРЕНО (PASS)${NC}"
    echo "ПО готово к прошивке в автомобиль."
else
    echo -e "${RED}СТАТУС РЕЛИЗА: ОТКЛОНЕНО (FAIL)${NC}"
    echo "Критическая ошибка безопасности! См. отчет в /results."
fi
echo -e "=======================================\n"