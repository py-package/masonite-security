import pendulum
from .BaseProtector import BaseProtector


class IPProtector(BaseProtector):
    def key(self):
        return f"ip_blocker_{self.ip()}"

    def ip_info(self):
        if self.cache.has(self.key()):
            old = self.cache.get(self.key())
            self.cache.put(
                self.key(),
                {
                    "ip": self.ip(),
                    "blocked": old.get("blocked", False),
                    "counter": old.get("counter", 0) + 1,
                    "started_at": old.get("started_at", pendulum.now().timestamp()),
                },
            )
            return old
        else:
            data = {
                "ip": self.ip(),
                "counter": 1,
                "blocked": False,
                "started_at": pendulum.now().int_timestamp,
            }
            self.cache.put(self.key(), data)
            return data

    def block_ip(self):
        """Block IP address."""
        if self.security_config.get("block_ip", True) is False:
            return self

        ips = self.security_config.get("blocked_ips", [])
        if len(ips) > 0:
            if self.ip() in ips:
                raise Exception("IP address is blocked.")
        return self

    def throttle(self):
        """Throttle IP address."""
        if self.security_config.get("throttle_requests", True) is False:
            return self

        info = self.ip_info()
        gap = pendulum.now().int_timestamp - info["started_at"]
        block_duration = self.security_config.get("ip_block_duration", 60)

        if info["blocked"] is True:
            if gap <= block_duration:
                raise Exception("IP address is blocked.")
            else:
                self.cache.forget(self.key())
                return self

        if gap < block_duration:
            if info["counter"] > self.security_config.get("max_requests", 10):
                info["blocked"] = True
                self.cache.put(self.key(), info)
        else:
            self.cache.forget(self.key())

        return self

    def block(self):
        pass
