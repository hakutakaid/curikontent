import os
from .. import bot as Drone
from telethon import events, Button

from A.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'


@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "𝐊𝐢𝐫𝐢𝐦 𝐋𝐢𝐧𝐤 𝐘𝐚𝐧𝐠 𝐈𝐧𝐠𝐢𝐧 𝐀𝐧𝐝𝐚 𝐂𝐮𝐫𝐢\n"
    await start_srb(event, text)
    
