"""Security Settings"""

"""
|--------------------------------------------------------------------------
| Masonite Security
|--------------------------------------------------------------------------
|
"""

BLOCK_IP = True
BLOCK_BOT = True
THROTTLE_REQUESTS = True

MAX_REQUESTS = 20  # requests per IP address per minute (default: 20)
IP_BLOCK_DURATION = 60  # seconds (default: 60)

# list of IP addresses to block (default: [])
BLOCKED_IPS = []

# list of Bot Agents to block
BLOCKED_BOTS = [
    "AhrefsBot",
    "Alexibot",
    "Baiduspider",
    "BlackWidow",
    "BLEXBot",
    "dotbot",
    "Jetbot",
    "MJ12bot",
    "Nutch",
    "rogerbot",
    "SemrushBot",
    "SemrushBot-SA",
    "Standford",
    "SurveyBot",
    "WebVac",
    "serpstatbot",
]
