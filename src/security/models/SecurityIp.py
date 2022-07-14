"""SecurityIP Model."""
from masoniteorm.models import Model


class SecurityIp(Model):
    """SecurityIP Model."""
    
    __table__ = "security_ips"

    __fillable__ = ["ip", "blocked"]
