import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", "12124605"))
    API_HASH = os.getenv("API_HASH", "5cf3577d85fd02286535ec2296934287")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5497795663:AAH1J6OQq_niE3E5u8tWijChjLQmLiA_z_M")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "postbot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1AZWarzoBu2WAcC8Fx3vGCicaImtybcc22UHdWvyA1Nfev7WLirE5hZDooAddwXK9MJ5dmppbNOKNEGPOsgXhOoO5lfWzixawvhvLcTbuSBC0n9O_rIk0e7vLtCcO1S--r2V9bFRt34vq0dGxf1oa15XXsGbCQluyMBqQGtleF2Sx02DVL1O48lGiGMf4nA5mtfpYH7YdsaDfwuSc5Lm6b6PgGRZbrXPg438Jtqv0T4aoy_oEayBdo0FkqFP0j4pdsMSRGuIkZLtmpZoMJj5x7xmE2zjj774ZIPej7xnhStp3zOPnVzUvPqRyKM3nG8R8MGm2-g1MewEz8Lt-x45Lbko6dgwe5uU=")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001697543381")) 
    BOT_USERNAME = os.getenv("BOT_USERNAME", "PostSearchBot")
    BOT_OWNER = int(os.getenv("BOT_OWNER", "1883570185"))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "cyniteoffcial")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "cynitebackup")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", """**Hᴇʏ {}, 

I ᴀᴍ Mᴏᴠɪᴇ Sᴇᴀʀᴄʜ Rᴏʙᴏᴛ 🔍.

I Wɪʟʟ Pʀᴏᴠɪᴅᴇ Eᴠᴇʀʏ Mᴏᴠɪᴇ Iɴ Mᴅɪsᴋ Lɪɴᴋ 🔗

Jᴜsᴛ Tʏᴘᴇ ᴀ Mᴏᴠɪᴇ Nᴀᴍᴇ 🎬**""" ) 
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/b57323ed245c34a374ac4.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", """ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕

ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ʏᴏᴜʀ ʟɪɴᴋꜱ.

ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ✅""" )
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001249072794")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://postbot:postbot@cluster0.ouwne8q.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001694679796"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 20))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "CyniteBackup")
    FORCE_SUB = os.getenv("FORCE_SUB", "False")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 180))
    MDISK_API = os.getenv("MDISK_API", "Qu7jX9V0Sn3q1JHdxjPp")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "31"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", """I ᴏɴʟʏ ꜱʜᴀʀᴇ ᴛʜᴇ ᴘᴏꜱᴛ ꜰʀᴏᴍ ᴘᴇᴏᴘʟᴇ'ꜱ ᴄʜᴀɴɴᴇʟ! 

ᴡʜᴏ ᴍᴀᴅᴇ ᴍᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ, 

i ɴᴏᴛ ꜱᴛᴏʀᴇ ᴀɴʏ ꜰɪʟᴇꜱ ᴏʀ ᴛᴇxᴛ ɪɴ  ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ.

ᴅᴍ ꜰᴏʀ ᴀɴʏ Qᴜᴇʀʏ @Cyniteofficial 🤖""" )
    ABOUT_WATCH_TEXT = """
ʜᴇʏ ʙᴜᴅᴅʏ, 

ᴍᴅɪsᴋ - ᴀɢᴀʀ ᴀᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴍᴅɪsᴋ ʟɪɴᴋ sᴇ ᴍᴏᴠɪᴇ ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴍᴅɪsᴋ ᴡᴀʟᴇ ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ 


ᴛᴇʀᴀ ʙᴏx - ᴀɢᴀʀ ᴀᴘᴘᴋᴏ ɴᴀʜɪ ᴘᴀᴛᴀ ᴋɪ ᴛᴇʀᴀʙᴏx sᴇ ᴍᴏᴠɪᴇs ᴋᴀɪsᴇ ᴅᴇᴋʜᴇ ᴛᴏ ɴɪᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴛᴇʀᴀ ʙᴏx ʙᴜᴛᴛᴏɴ ᴘᴀʀ ᴄʟɪᴄᴋ ᴋᴀʀᴇ

ʀᴇɢᴀʀᴅs - @PostSearchRobot"""
    ABOUT_MDISK_TEXT = """
𝗠𝗱𝗶𝘀𝗸 𝗸𝗶 𝗹𝗶𝗻𝗸𝘀 𝗢𝗽𝗲𝗻 𝗔𝗶𝘀𝗲 𝗞𝗮𝗿𝗲👇🔥
वीडियो प्ले करने में कोई प्रोब्लम अ रही हो तो Mx Player App डाउनलोड करले😊👍

1) 𝘔𝘥𝘪𝘴𝘬 𝘬𝘪 𝘭𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 1 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢. 💜

2) 𝘞𝘢𝘩𝘢 𝘱𝘢𝘳 4 𝘉𝘶𝘵𝘵𝘰𝘯 𝘏𝘰𝘨𝘢 𝘴𝘗𝘭𝘢𝘺 𝘞𝘪𝘵 𝘔𝘹 𝘗𝘭𝘢𝘺𝘦𝘳𝘴𝘈𝘯𝘥 𝘚𝘱 𝘗𝘭𝘢𝘺𝘦𝘳.😉

3) 𝘈𝘱𝘬𝘰 𝘔𝘹 𝘗𝘭𝘢𝘺𝘦𝘳 𝘗𝘢𝘳 𝘓𝘪𝘬𝘩𝘰 𝘏𝘶𝘦 𝘒𝘰 𝘊𝘩𝘰𝘰𝘴𝘦 𝘒𝘢𝘳𝘯𝘢 𝘏𝘢𝘪😍

4) 𝘐𝘴𝘬𝘦 𝘉𝘢𝘢𝘥 𝘈𝘨𝘢𝘳 𝘈𝘱𝘬𝘰 𝘖𝘯𝘭𝘪𝘯𝘦 𝘋𝘦𝘬𝘩𝘯𝘢 𝘏𝘢𝘪 𝘛𝘰 𝘞𝘢𝘵𝘤𝘩 𝘖𝘯𝘭𝘪𝘯𝘦 𝘗𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘦 💻

5) 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘒𝘢𝘳𝘯𝘦 𝘒𝘦 𝘓𝘪𝘺𝘦 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘉𝘶𝘵𝘵𝘰𝘯 𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘦 ⬇

6)𝘕𝘢𝘩𝘪 𝘛𝘰 𝘈𝘱𝘱 𝘕𝘪𝘤𝘩𝘦 𝘋𝘪𝘺𝘦 𝘎𝘢𝘺𝘦 Watch Video 𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘬𝘦 𝘗𝘶𝘳𝘢 𝘚𝘵𝘦𝘱 𝘓𝘪𝘷𝘦 𝘗𝘩𝘰𝘵𝘰 𝘔𝘦 𝘋𝘦𝘬𝘩 𝘚𝘬𝘢𝘵𝘦 𝘏𝘢𝘪😇"""
    ABOUT_TERABOX_TEXT = """
𝗧𝗲𝗿𝗮𝗕𝗼𝘅 𝗸𝗶 𝗹𝗶𝗻𝗸𝘀 𝗢𝗽𝗲𝗻 𝗔𝗶𝘀𝗲 𝗞𝗮𝗿𝗲👇🔥
वीडियो प्ले करने में कोई प्रोब्लम अ रही हो तो इक बार रजिस्ट्रेशन कर ले फिर आप बिना एड के विडियो अच्छे से चला पाएंगे थैंक्यू 😊👍

https://terabox.com/s/1QZGvLaoU_VMaSCDT2NNvOQ

1) 𝘛𝘦𝘳𝘢𝘣𝘰𝘹 𝘬𝘪 𝘭𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 𝘢𝘪𝘴𝘢 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢.

2) 𝘜𝘱𝘱𝘢𝘳 𝘴𝘪𝘥𝘦 𝘭𝘰𝘨𝘪𝘯/𝘙𝘦𝘨𝘪𝘴𝘵𝘳𝘢𝘵𝘪𝘰𝘯 𝘭𝘪𝘬𝘩𝘢 𝘩𝘰𝘨𝘢 𝘶𝘴𝘱𝘦 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘰.😉

3) 𝘗𝘩𝘪𝘳 𝘳𝘦𝘨𝘪𝘴𝘵𝘳𝘢𝘵𝘪𝘰𝘯 𝘬𝘢𝘳𝘰 𝘢𝘶𝘳 𝘭𝘪𝘧𝘦 𝘵𝘪𝘮𝘦 𝘧𝘳𝘦𝘦 𝘷𝘪𝘥𝘦𝘰𝘴 𝘣𝘪𝘯𝘢 𝘈𝘥𝘴 𝘬𝘦 𝘥𝘦𝘬𝘩𝘰😍

4) 𝘕𝘢𝘩𝘪 𝘛𝘰 𝘈𝘱𝘱 𝘕𝘪𝘤𝘩𝘦 𝘋𝘪𝘺𝘦 𝘎𝘢𝘺𝘦  𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘬𝘦 𝘗𝘶𝘳𝘢 𝘚𝘵𝘦𝘱 𝘓𝘪𝘷𝘦 𝘗𝘩𝘰𝘵𝘰 𝘔𝘦 𝘋𝘦𝘬𝘩 𝘚𝘬𝘢𝘵𝘦 𝘏𝘢𝘪😇"""

    ABOUT_MDISKLINK_TEXT = """
𝗠𝗱𝗶𝘀𝗸Link 𝗸𝗶 𝗹𝗶𝗻𝗸𝘀 𝗢𝗽𝗲𝗻 𝗔𝗶𝘀𝗲 𝗞𝗮𝗿𝗲👇🔥
वीडियो प्ले करने में कोई प्रोब्लम अ रही हो तो Mx Player App डाउनलोड करले😊👍

1) L𝘪𝘯𝘬 𝘱𝘦𝘳 𝘤𝘭𝘪𝘤𝘬 𝘬𝘢𝘳𝘦 𝘶𝘴𝘬𝘦 𝘣𝘢𝘢𝘥 1 𝘱𝘢𝘨𝘦 𝘬𝘩𝘶𝘭𝘦𝘨𝘢. 💜

2) 𝘞𝘢𝘩𝘢 𝘱𝘢𝘳 "Dual Tap Rapidly" par 1 bar click kare aur agar nahi khule to 1 baar aur click kare.😉

3) phir "I am not a robot" par click kare.😍

4) 𝘐𝘴𝘬𝘦 𝘉𝘢𝘢𝘥 ek page khulega waha 20 sec wait krne ke baad "Dual tap to go to link" pr 1 baar click kare. 💻

5) phir "Go to Link-Click Open" pr click kare.⬇️

6) phir mdisk ya terabox ka link khul jayega Enjoy Watching✌️

7) 𝘕𝘢𝘩𝘪 𝘛𝘰 𝘈𝘱𝘱 𝘕𝘪𝘤𝘩𝘦 𝘋𝘪𝘺𝘦 𝘎𝘢𝘺𝘦 Watch Video 𝘗𝘢𝘳 𝘊𝘭𝘪𝘤𝘬 𝘒𝘢𝘳𝘬𝘦 𝘗𝘶𝘳𝘢 𝘚𝘵𝘦𝘱 𝘓𝘪𝘷𝘦  𝘋𝘦𝘬𝘩 𝘚𝘢k𝘵𝘦 𝘏𝘢𝘪.😇"""

    ABOUT_SHAREUS_TEXT = """
😎 𝘚𝘩𝘢𝘳𝘦𝘶𝘴😎

हिंदी में :-😍

𝘞𝘢𝘵𝘤𝘩 𝘛𝘰𝘵𝘶𝘳𝘪𝘢𝘭 पर क्लिक करे उसमे मैंने 1 मिनट के वीडियो में दिखाया है कि दिए गए लिंक से मूवी कैसे डाउनलोड या प्ले करें। इस वीडियो को देखने के बाद आपको कभी कोई परेशानी नहीं होगी। आनंद लेना! 😇"""

    ABOUT_MDISKSHORTNER_TEXT = """
😎 𝘔𝘥𝘪𝘴𝘬𝘚𝘩𝘰𝘳𝘵𝘯𝘦𝘳 😎

हिंदी में :-😍

𝘞𝘢𝘵𝘤𝘩 𝘛𝘰𝘵𝘶𝘳𝘪𝘢𝘭 पर क्लिक करे उसमे मैंने 1 मिनट के वीडियो में दिखाया है कि दिए गए लिंक से मूवी कैसे डाउनलोड या प्ले करें। इस वीडियो को देखने के बाद आपको कभी कोई परेशानी नहीं होगी। आनंद लेना! 😇"""

    ABOUT_URLSOPEN_TEXT = """
😎 𝘚𝘩𝘰𝘳𝘵𝘶𝘳𝘭 😎

हिंदी में :-😍

𝘞𝘢𝘵𝘤𝘩 𝘛𝘰𝘵𝘶𝘳𝘪𝘢𝘭 पर क्लिक करे उसमे मैंने 1 मिनट के वीडियो में दिखाया है कि दिए गए लिंक से मूवी कैसे डाउनलोड या प्ले करें। इस वीडियो को देखने के बाद आपको कभी कोई परेशानी नहीं होगी। आनंद लेना! 😇"""

    ABOUT_DULINK_TEXT = """
😎 𝘋𝘶𝘓𝘪𝘯𝘬 😎

हिंदी में :-😍

𝘞𝘢𝘵𝘤𝘩 𝘛𝘰𝘵𝘶𝘳𝘪𝘢𝘭 पर क्लिक करे उसमे मैंने 1 मिनट के वीडियो में दिखाया है कि दिए गए लिंक से मूवी कैसे डाउनलोड या प्ले करें। इस वीडियो को देखने के बाद आपको कभी कोई परेशानी नहीं होगी। आनंद लेना! 😇"""

    ABOUT_INDIANSHORTNER_TEXT = """
😎 𝘐𝘯𝘥𝘪𝘢𝘯 𝘚𝘩𝘰𝘳𝘵𝘯𝘦𝘳 😎

हिंदी में :-😍

𝘞𝘢𝘵𝘤𝘩 𝘛𝘰𝘵𝘶𝘳𝘪𝘢𝘭 पर क्लिक करे उसमे मैंने 1 मिनट के वीडियो में दिखाया है कि दिए गए लिंक से मूवी कैसे डाउनलोड या प्ले करें। इस वीडियो को देखने के बाद आपको कभी कोई परेशानी नहीं होगी। आनंद लेना! 😇"""

    ABOUT_HELP_TEXT = """

🍓 RᴇQᴜɪʀᴇᴍᴇɴᴛ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ!

🍓 Sᴛᴇᴘ 1 - Aᴘᴋᴏ ᴇᴋ ɢʀᴏᴜᴘ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴍᴇᴍʙᴇʀꜱ ʙʜɪ ʜᴏ, ᴀᴜʀ ᴇᴋ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋɪ ᴊᴀʀᴜʀᴀᴛ ʜᴏɢɪ, ᴊɪꜱᴍᴇ ᴀᴘᴋᴇ ꜱᴀʀᴇ ᴘᴏꜱᴛ ʜᴏɴɢᴇ!

🍓 Sᴛᴇᴘ 2 - ʙᴏᴛ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴀᴜʀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴋᴀ ᴀᴅᴍɪɴ ʙᴀɴᴀɴᴀ ʜᴏɢᴀ.

🍓 Sᴛᴇᴘ 3 - ɢʀᴏᴜᴘ ᴍᴇ "/License" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ!

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ. 

🍓 Sᴛᴇᴘ 4 - ɢʀᴏᴜᴘ ᴍᴇ "/database - ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ɪᴅ" ᴛʏᴘᴇ ᴋᴀʀ ᴋᴇ ꜱᴇɴᴅ ᴋᴀʀɴᴀ ʜᴏɢᴀ.

ꜰɪʀ ʙᴏᴛ ᴋᴇ ᴏᴡɴᴇʀ ᴀᴘᴋᴀ ʏᴇ ʀᴇQᴜᴇꜱᴛ ʙʜɪ ᴀᴄᴄᴇᴘᴛ ᴋᴀʀ ʟᴇɴɢᴇ 

🍓 Sᴛᴇᴘ 5 - ᴀʙ ᴀᴘᴋᴏ ᴀᴘɴᴇ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴘᴏꜱᴛ ᴅᴀʟɴɪ ʜᴏɢɪ,

ᴊɪꜱꜱᴇ ᴋɪ ᴀɢᴀʀ ɢʀᴏᴜᴘ ᴍᴇ ᴋᴏɪ ᴜꜱᴇʀ ꜱᴇᴀʀᴄʜ ᴋᴀʀᴇ ᴛᴏ ʏᴇ ʙᴏᴛ ᴜɴ ᴜꜱᴇʀ ᴋᴇ Qᴜᴀʀʏ ᴋᴏ ꜱᴀᴍᴀᴊʜ ᴋᴇ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ꜱᴇ ᴘᴏꜱᴛ ᴜᴛʜᴀ ᴋᴇ ᴜɴʜᴇ ᴅᴇ ᴘᴀʏᴇ.

🍓 Nᴏᴛᴇ : Bᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴇ ᴄʜᴀɴɴᴇʟ ᴍᴇ ᴊᴏɪɴ ʜᴏɴᴇ ᴄʜᴀʜɪʏᴇ,

ᴀɢᴀʀ ʙᴏᴛ ᴀᴅᴍɪɴ ᴀᴘᴋᴀ ʀᴇQᴜᴇꜱᴛ ᴀᴄᴄᴇᴘᴛ ɴʜɪ ᴋᴀʀ ʀᴀʜᴇ ʜᴀɪɴ ᴛᴏ ᴜɴʜᴇ ᴘᴇʀꜱᴏɴᴀʟ ᴍꜱɢ ᴋᴀʀᴇɴ.

👉 @Cyniteofficial

"""

