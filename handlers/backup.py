import asyncio
import datetime
import shutil
import os
import zipfile
import logging

from aiogram.types import Message, FSInputFile
from aiogram.filters.command import Command
from dispatcher import dp, bot
from config_reader import config

logging.basicConfig(level = logging.INFO)

admin_id = config.admin_id

async def create_backup():
    if not os.path.exists("root"):
        os.makedirs("root")

    try:
        shutil.copytree(
            "/opt/marzban/",
            os.path.join("root", 'opt'),
            dirs_exist_ok=True
        )
        shutil.copytree(
            "/var/lib/marzban",
            os.path.join("root", 'var'),
            dirs_exist_ok=True
        )
    except Exception as error:
        logging.error(error)
        return False
    
    try:
        with zipfile.ZipFile(
            "backup.zip", 'w', zipfile.ZIP_DEFLATED
        ) as zipf:
            for root, _, files in os.walk("root"):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(
                        file_path,
                        os.path.relpath(
                            file_path, "root"
                        )
                    )
    except Exception as error:
        logging.error(error)
        return False

    try:
        shutil.rmtree("root")
    except Exception as error:
        logging.error(error)
        return False
    
    return True, None

async def send_backup():
    now = datetime.datetime.now()
    backup_time = now.strftime("%d-%m-%Y %H-%M")
    comment = f"<b>Резервная копия от {backup_time}\n\nCreated by stix_r.t.me\nhttps://github.com/Winchester-Dean/marz-py-backuper</b>"

    try:
        backup_file = FSInputFile("backup.zip")
        await bot.send_document(
            admin_id,
            document = backup_file,
            caption = comment
        )
    except Exception as error:
        logging.error(f"Ошибка при отправке файла: {e}")
        await bot.send_message(
            admin_id,
            f"Произошла ошибка при отправке файла: {e}"
        )
    finally:
        try:
            os.remove("backup.zip")
        except Exception as e:
            logging.warning(f"Ошибка при удалении архива: {e}")

async def create_and_send():
    result, error_message = await create_backup()

    if result:
        await send_backup()
    else:
        await bot.send_message(
            admin_id,
            f"Произошла ошибка при создании резервной копии: {error_message}"
        )

async def scheduled_backups():
    while True:
        logging.info(
            f"Ожидание {config.backup_interval} минут до следующего резервного копирования"
        )

        await asyncio.sleep(
            config.backup_interval * 60
        )

        logging.info(
            "Начинаем запланированное резервное копирование"
        )
        
        if admin_id:
            await create_and_send()
        else:
            logging.error("Error")

@dp.message(Command("backup"))
async def backup(msg: Message):
    await create_and_send()
    await scheduled_backups()
