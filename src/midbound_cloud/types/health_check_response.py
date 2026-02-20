# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HealthCheckResponse"]


class HealthCheckResponse(BaseModel):
    status: Literal["ok", "degraded", "unhealthy"]
    """Service health status"""

    timestamp: datetime
    """Current server timestamp (ISO)"""

    version: str
    """API version"""
