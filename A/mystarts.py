from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st,buttons=[[Button.url("OWNER", url="t.me/can_you_silent_please")]])

    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("OWNER", url="t.me/can_you_silent_please")]])
    
