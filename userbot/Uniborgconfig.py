import os
from telethon.tl.types import ChatBannedRights
ENV = bool(os.environ.get("ENV", False))
if ENV:
    import os
    class Config(object):
        LOGGER = True
        PM_DATA = os.environ.get("PM_DATA", "ENABLE")
       
else:
    class Config(object):
        DB_URI = None
       
