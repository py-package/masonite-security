"""A SecurityProvider Service Provider."""

from masonite.packages import PackageProvider
from ..Security import Security
from ..middlewares.SecurityMiddleware import SecurityMiddleware


class SecurityProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (self.root("security").name("security").config("config/security.py", publish=True))

    def register(self):
        super().register()
        self.application.bind("security", Security(application=self.application))
        self.application.make("middleware").add({"protect": [SecurityMiddleware]})

    def boot(self):
        """Boots services required by the container."""
        pass
