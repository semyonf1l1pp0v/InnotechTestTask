# Запуск образа
1. Сделать порт 6000 доступным
- В Firefox:
  - В адресную строку вбиваем about:config
  - В открывшемся окне печатаем `network.security.ports.banned.override`
  - Выбираем тип "Строка"
  - Нажимаем на плюсик
  - Вводим 6000
- В Google Chrome:
  - MacOS: В терминале вводим команду `open /Applications/Google\ Chrome.app --args --explicitly-allowed-ports=6000` (можно сохранить ее в Automator)
2. Запускаем Docker 
3. В терминале вводим `docker pull semyonf1l1pp0v/test_task:v1.0`
4. После ожидания вводим `docker run -d -p 6000:6000 semyonf1l1pp0v/test_task:v1.0`
5. Заходим в браузер, в адресную строку вбиваем `0.0.0.0:6000`
# Запуск проекта:
1. `git clone https://github.com/semyonf1l1pp0v/TestTask.git`
2. Устанавливаем зависимости с помощью `pip install -r requirements.txt`
3. Запускаем `uvicorn app.main:app --reload --port 6000` 

