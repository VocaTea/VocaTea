__version__ = (1441)
import os
import logging
from .. import loader, utils
import random
import time
import datetime
from telethon import functions
from telethon.tl.custom import Message

logger = logging.getLogger("Hentai")

@loader.tds
class Hentai(loader.Module):
    """Hentai roulet"""
    strings = {
        "name": "Hentai",
        "search": "<emoji document_id=5368580099182435492>👁</emoji> loading your Hentai..."
    }
    
    async def nsfwcmd(self, message: Message):
         """-> to get your nsfw arts"""
         await message.edit(self.strings("search"))
         time.sleep(0.5)
         chat = "spin_nsfw"
         result = await message.client(
             functions.messages.GetHistoryRequest(
                 peer=chat,
                 offset_id=0,
                 offset_date=datetime.datetime.now(),
                 add_offset=random.choice(range(1, 770, 2)),
                 limit=1,
                 max_id=0,
                 min_id=0,
                 hash=0,
             ),
         )
         await message.delete()
         await message.client.send_file(
             message.to_id, 
             result.messages[0].media, 
             reply_to=getattr(message, "reply_to_msg_id", None),
             )