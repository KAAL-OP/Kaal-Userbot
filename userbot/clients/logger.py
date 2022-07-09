

import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import KAAL2, KAAL3, KAAL4, KAAL5, bot, branch, tgbot
from userbot.utils import checking

MSG_ON = """
🔥 **kaal-Userbot is on fire**
━━
➠ **Userbot Version*-1.0**
**support group - @kaalxsupport **
━━
"""


async def kaal_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        KAALage_call=True,
    )
    try:
        if bot and tgbot:
            KaalUBOT = await tgbot.get_me()
            BOT_USERNAME = KaalUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            KaalUBOT = await tgbot.get_me()
            BOT_USERNAME = KaalUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAAL2:
            await checking(KAAL2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAAL2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAAL3:
            await checking(KAAL3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAAL3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAAL4:
            await checking(KAAL4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAAL4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if KAAL5:
            await checking(KAAL5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await KAAL5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
