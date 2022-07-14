from masonite.configuration import config


class BaseProtector:
    def __init__(self, application, request) -> None:
        self.application = application
        self.request = request
        self.security_config = config("security")
        self.user_agent = request.environ.get("HTTP_USER_AGENT", "").lower()
        self.blocked = False
        self.cache = application.make("cache").store()

    def ip(self):
        return self.request.ip() or "127.0.0.1"

    def block(self):
        pass
