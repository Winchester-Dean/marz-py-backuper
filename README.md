# marz-py-backuper
<b><p>Простой бот для бэкапа панели Marzban</p>

<h1>Настройка бота</h1>
<h3>Подготовка</h3>
<p>Первым делом обновление пакетов (на всякий случай) и подготовка:</p>
<p>1. <code>apt update && apt upgrade -y</code></p>
<p></p>2. <code>apt install git python3 python3-pip -y</code</b>
<h3>Скачиваем бота:</h3>
<p>3. <code>git clone https://github.com/Winchester-Dean/marz-py-backuper</code></p>
<p><h3>Переходим в директорию бота и скачиваем необходимые компоненты:</h3></p>
<p>4. <code>cd marz-py-backuper</code></p>
<p>Так же обязательно переходим в виртуальное окружение:</p>
<p>5. <code>python3 -m venv dean</code></p>
<p>6. <code>source dean/bin/activate</code></p>
<p>7. <code>pip3 install -r requirements.txt</code></p>
<h3>Теперь нужно редактировать env файл под ваши данные:<h3>
<p>8. <code>nano .env</code></p>
<p>Редактировать нужно переменные bot_token, admin_id, backup_interval. Токен бота берем у @BotFather. admin_id указываем свой айди, его можно взять у бота @getmyid_bot. backup_interval задается в минутах, если нужно создавать бэкапы каждый час, нужно указать значение 60.</p>
<h3>После изменения сохраняем файл (CTRL + X) и запускаем бота в фоне:<h3>
<p>9. <code>nohup python3 main.py &</code></p></b>
