from .protectors.DatabaseProtector import DatabaseProtector

from .protectors.IPProtector import IPProtector
from .protectors.BotProtector import BotProtector


class Security:
    def __init__(self, application) -> None:
        self.app = application

    def secure(self, request):
        try:
            (
                # bot protection
                BotProtector(self.app, request)
                .block_fake_bot()
                .block_bot()
                .block()
            )

            (
                # ip protection
                IPProtector(self.app, request)
                .block_ip()
                .throttle()
            )

            (
                # database protection
                DatabaseProtector(self.app, request)
            )
        except Exception as e:
            return self.app.make("response").status(403).json({"message": str(e)})

        return request
