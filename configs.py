# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("API_ID", "24490919"))
    API_HASH = os.environ.get("API_HASH", "d1b3b15126c47dd4cb491553ee1db910")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQF1s6cAoxZitr4Z_3Dcn3QsBeP81fETNQGxlUPUHhssgVCgysgMwrv8JqNLXuvlp1wB2Qw3bjPxzBIcWlTgfuVvrc7hf5Ez0TEH7i4POyU0fSq14QTjzBlDBhALJu779JyQRuySPYM7CYhYk1EgCs90G3X2GUS2dO-cdkqzxwEPP7VJtYvxz7Eei4PYTH2Kd9P7_BGiagf0JG4GIrwYPUDz7_np_8UVwGkii9X54zzXuD9nvDAXIjkiuOTLxZl6LcuGKcbobdPIsOYA1db0O4SkN1FvoO9Bu6yadGkhwM8bKF8FYAOA68NMpPFcu9D00gxjv0-NP96WACwUzziDSQeLeHGcgAAAAAF0xr8GAA")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-1001902376170").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-1001583228152").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
