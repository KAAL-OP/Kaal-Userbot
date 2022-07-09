

import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from telethon import version

from userbot import BOT_TOKEN
from userbot import BOT_VER as ubotversion
from userbot import BOTLOG_CHATID, LOGS, LOOP, bot
from userbot.clients import kaal_userbot_on, multikaal
from userbot.core.git import git
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, autopilot

try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"userbot.modules.{module_name}")
    client = multikaal()
    total = 5 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
    LOGS.info(f"Python Version - {python_version()}")
    LOGS.info(f"Telethon Version - {version.__version__}")
    LOGS.info(f"PyTgCalls Version - {pytgcalls.__version__}")
    LOGS.info(f"Kaal-Userbot Version - {ubotversion} [🔥 userbot is on fire! 🔥]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOOP.run_until_complete(kaal_userbot_on())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
