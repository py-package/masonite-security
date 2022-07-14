from ipaddress import ip_address
from .BaseProtector import BaseProtector
import re
import socket

BOTS = (
    # Bot signature string, bot verification regex
    ("baiduspider", re.compile(r".*crawl\.baidu\.(com|jp)$")),
    ("googlebot", re.compile(r".*(google|googlebot)\.com$")),
    ("bingbot", re.compile(r".*search\.msn\.com$")),
    ("slurp", re.compile(r".*crawl\.yahoo\.net$")),
    ("yandexbot", re.compile(r".*yandex\.(ru|com|net)$")),
    ("msnbot", re.compile(r".*msn\.com$")),
    ("duckduckbot", re.compile(r".*duckduckgo\.com$")),
    ("sogou", re.compile(r".*sogou\.com$")),
)


class BotProtector(BaseProtector):
    def __init__(self, application, request):
        super().__init__(application, request)

    def block_fake_bot(self):
        if self.security_config.get("block_bot", True) is False:
            return self

        matched_signatures = [
            signature for signature in BOTS if signature[0].lower() in self.user_agent
        ]
        if len(matched_signatures) == 1:
            bot_sig_string, bot_verification_regex = matched_signatures[0]
            client_ip = self.request.ip()

            if not client_ip:
                raise Exception("IP spoofing detected.")

            if not self.ipaddress_is_private(ip=client_ip):
                try:
                    bot_reverse_lookup = self.reverse_lookup(client_ip)
                except socket.herror as e:
                    if e.errno == 1:
                        raise Exception("IP spoofing detected.")
                else:
                    is_fake_bot = bot_verification_regex.match(bot_reverse_lookup) is None
                    if is_fake_bot:
                        raise Exception("IP spoofing detected.")
        return self

    def block_bot(self):
        if self.security_config.get("block_bot", True) is False:
            return self

        bots = self.security_config.get("blocked_bots", [])
        for bot in bots:
            if bot in self.user_agent:
                raise Exception("SPAM bot detected.")
        return self

    def ipaddress_is_private(self, ip):
        return ip_address(address=ip).is_private

    def reverse_lookup(self, ip_address):
        return socket.gethostbyaddr(ip_address)[0]
