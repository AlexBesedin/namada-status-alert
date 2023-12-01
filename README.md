# NAMADA NETWORK ALERT

Данная утилита парсит каждые 30 секунд данные с RPC тестовой сети NAMADA, включая текущую высоту блока, время когда был добыт последний блок, название тестовой сети и версия. Далее бот отправляет эти данные в сообщество телеграма. 

### Как запустить проект:
 ```sh
git clone git@github.com:AlexBesedin/namada-status-alert.git
cd namada-status-alert
```
Создать файл с переменными окружения .env

 ```sh
touch .env
```
Пример содержимого файла .env:
 ```sh
TELEGRAM_TOKEN=00000000000000000
CHAT_ID=-00000000000000
URL='url_адрес_rpc.com/status'
```
Соберите контейнер:
 ```sh
sudo docker-compose up -d --build
```
### АВТОР: 

- [Беседин Алексей](https://github.com/AlexBesedin)
- tg: @beszedin