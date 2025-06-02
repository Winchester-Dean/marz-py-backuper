# marz-py-backuper

Простой бот для резервного копирования панели Marzban.

## Настройка бота

### Подготовка

Сначала обновите пакеты (на всякий случай) и подготовьте среду:

1.  <pre><code>apt update && apt upgrade -y</code></pre>
2.  <pre><code>apt install git python3 python3-pip -y</code></pre>

### Скачиваем бота:

3.  <pre><code>git clone https://github.com/Winchester-Dean/marz-py-backuper</code></pre>

### Переходим в директорию бота и скачиваем необходимые компоненты:

4.  <pre><code>cd marz-py-backuper</code></pre>

Обязательно перейдите в виртуальное окружение:

5.  <pre><code>python3 -m venv dean</code></pre>
6.  <pre><code>source dean/bin/activate</code></pre>
7.  <pre><code>pip3 install -r requirements.txt</code></pre>

### Редактируем .env файл:

8.  <pre><code>nano .env</code></pre>

Вам нужно отредактировать переменные `bot_token`, `admin_id`, и `backup_interval`.

*   `bot_token`: Получите токен бота у [@BotFather](https://t.me/BotFather) в Telegram.
*   `admin_id`: Укажите свой ID. Его можно узнать у бота [@getmyid_bot](https://t.me/getmyid_bot) в Telegram.
*   `backup_interval`: Задается в минутах. Если нужно создавать резервные копии каждый час, укажите значение `60`.

### Запускаем бота в фоне:

9.  <pre><code>nohup python3 main.py &</code></pre>
