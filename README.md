# marz-py-backuper

Простой бот для резервного копирования панели Marzban.

## Настройка бота

### Подготовка

Сначала обновите пакеты (на всякий случай) и подготовьте среду:

1.  `apt update && apt upgrade -y`
2.  `apt install git python3 python3-pip -y`

### Скачиваем бота:

3.  `git clone https://github.com/Winchester-Dean/marz-py-backuper`

### Переходим в директорию бота и скачиваем необходимые компоненты:

4.  `cd marz-py-backuper`

Обязательно перейдите в виртуальное окружение:

5.  `python3 -m venv dean`
6.  `source dean/bin/activate`
7.  `pip3 install -r requirements.txt`

### Редактируем .env файл:

8.  `nano .env`

Вам нужно отредактировать переменные `bot_token`, `admin_id`, и `backup_interval`.

*   `bot_token`: Получите токен бота у [@BotFather](https://t.me/BotFather) в Telegram.
*   `admin_id`: Укажите свой ID. Его можно узнать у бота [@getmyid_bot](https://t.me/getmyid_bot) в Telegram.
*   `backup_interval`: Задается в минутах. Если нужно создавать резервные копии каждый час, укажите значение `60`.

### Запускаем бота в фоне:

9.  `nohup python3 main.py &`
