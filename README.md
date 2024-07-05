# Запуск
1. Сделать порт 6000 доступным
- В Firefox:
  - В адресную строку вбиваем about:config
  - В открывшемся окне печатаем ```network.security.ports.banned.override```
  - Выбираем тип "Строка"
  - Нажимаем на плюсик
  - Вводим 6000
2. Запускаем Docker 
3. В терминале вводим ```docker pull semyonf1l1pp0v/test_task:v1.0```
4. После ожидания вводим ```docker run -d -p 6000:6000 semyonf1l1pp0v/test_task:v1.0```

