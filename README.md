# marz-py-backuper
Простой бот для бэкапа панели Marzban

<h1>Настройка бота</h1>
<h3>Подготовка</h3>
Первым делом обновление пакетов (на всякий случай) и подготовка:

<b>1. <code>apt update && apt upgrade -y</code>
2. <code>apt install git python3 python3-pip -y</code>

<h3>Скачиваем бота:</h3>

3. <code>git clone https://github.com/Winchester-Dean/marz-py-backuper</code>

<h3>Переходим в директорию бота и скачиваем необходимые компоненты:</h3>
4. <code>cd marz-py-backuper</code>

Так же обязательно переходим в виртуальное окружение:
5. <code>python3 -m venv dean</code>
6. <code>source dean/bin/activate</code>
7. <code>pip3 install -r requirements.txt</code>

<h3>Теперь нужно редактировать env файл под ваши данные:<h3>
8. <code>nano .env</code>

Редактировать нужно переменные bot_token, admin_id, backup_interval. Токен бота берем у @BotFather. admin_id указываем свой айди, его можно взять у бота @getmyid_bot. backup_interval задается в минутах, если нужно создавать бэкапы каждый час, нужно указать значение 60.

<h3>После изменения сохраняем файл (CTRL + X) и запускаем бота в фоне:<h3>
9. <code>nohup python3 main.py &</code>
