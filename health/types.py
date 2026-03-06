from enum import StrEnum
from dataclasses import dataclass
from typing import Optional

class ServiceName(StrEnum):
    DATABASE = "db"
    STORAGE = "storage"
    BOT = "bot"

class HealthStatus(StrEnum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    TIMEOUT = "timeout"

@dataclass
class CheckResult:
    status: HealthStatus
    error: Optional[str] = None
    latency: float = 0.0
