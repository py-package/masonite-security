"""SecurityLog Model."""
from masoniteorm.models import Model


class SecurityLog(Model):
    """SecurityLog Model."""
    
    __table__ = "security_logs"

    __fillable__ = ["user_id", "ip", "url", "method", "user_agent", "referrer"]
