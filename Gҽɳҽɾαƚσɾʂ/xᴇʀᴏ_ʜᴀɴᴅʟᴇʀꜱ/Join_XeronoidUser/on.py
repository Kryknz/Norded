"""
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••| 
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝

                          GNU GENERAL PUBLIC LICENSE
                            Version 3, 29 June 2007
                            
        Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
            Everyone is permitted to 𝗰𝗼𝗽𝘆 𝗮𝗻𝗱 𝗱𝗶𝘀𝘁𝗿𝗶𝗯𝘂𝘁𝗲 verbatim copies
                of this license document, 𝗯𝘂𝘁 𝗰𝗵𝗮𝗻𝗴𝗶𝗻𝗴 𝗶𝘁 𝗶𝘀 𝗻𝗼𝘁 𝗮𝗹𝗹𝗼𝘄𝗲𝗱.
                        ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝,
                        Telegram Music player userbot 
                has been licensed under GNU General Public License
            𝐂𝐨𝐩𝐲𝐫𝐢𝐠𝐡𝐭 (𝐂) 𝟐𝟎𝟐𝟏 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗦𝗼𝘂𝗹 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝗟𝗮𝗯 | 𝗛𝘆𝗽𝗲𝗩𝗼𝗶𝗱𝘀
⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝         |           ⇜⊷°•♪   🦋Ӽɛʀօռօɨɖ🦋   ♪•°⊶⇝
|•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••|        
"""
from ᴘᴜʀɢᴇ_ᴍᴇᴄʜᴀɴɪꜱᴍ import * 
from ᴍᴜꜱɪᴄ_ᴄᴏɴᴛᴇɴᴛ import *
from xᴇʀᴏꜰɪʟᴇᴛꜱ import *
from ʟɪʙʀᴀʀʏ import *
from ʜᴏᴍᴇ import *


@Client.on_message(
filters.group
& filters.chat(CHAT_ID)
& ~filters.edited
& ~filters.via_bot
& Known_User
& filters.command("on", prefixes="/"))
async def join_group_call(client, m: Message):
    Xero_Voixe = XePlay.Xero_Voixe
    if not Xero_Voixe:
        XePlay.Xero_Voixe = GroupCallFactory(client).get_file_group_call()
        XePlay.Xero_Voixe.add_handler(
        Xero_Server_Stats,
        GroupCallFileAction.NETWORK_STATUS_CHANGED)
        XePlay.Xero_Voixe.add_handler(
        playout_ended_handler,
        GroupCallFileAction.PLAYOUT_ENDED)
        await XePlay.Xero_Voixe.start(m.chat.id)
        await m.delete()
        
        
        
        
    if Xero_Voixe and Xero_Voixe.is_connected:
        "First Log this event using the userbot"
        Xero_Voixe = XePlay.Xero_Voixe
        chat_id = int("-100" + str(Xero_Voixe.full_chat.id))
        chat = await client.get_chat(chat_id)        
        await client.send_animation(
            animation=xerolink,
            duration=10,
            chat_id=LOGGER_ID,
            caption=f"{XEXO}🎧 Userbot has already joined group voice chat in **{chat.title}**"
        )
        
        
        "Now Send the joined info to the requested group"
        await m.reply_animation(
            animation=xerolink,
            caption=f"{XEXO}🎧 Userbot has already joined group voice chat in **{chat.title}**"
        )
        
        