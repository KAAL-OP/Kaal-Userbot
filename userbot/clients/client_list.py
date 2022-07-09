
from base64 import b64decode
import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, KAAL2, KAAL3, KAAL4, KAAL5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if KAAL2 is not None:
            id2 = await KAAL2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if KAAL3 is not None:
            id3 = await KAAL3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if KAAL4 is not None:
            id4 = await KAAL4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if KAAL5 is not None:
            id5 = await KAAL5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("ODQ0NDMyMjIw").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        KAAL_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        KAAL_USER = client.first_name
    kaal_mention = f"[{KAAL_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, KAAL_USER, kaal_mention
