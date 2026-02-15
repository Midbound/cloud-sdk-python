# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "IdentityValidatedWebhookEvent",
    "Data",
    "DataAttribution",
    "DataSession",
    "DataSessionNetwork",
    "DataSessionNetworkAsn",
    "DataSessionNetworkBotManagement",
    "DataSessionScreen",
    "DataSessionUtm",
    "DataValidation",
    "DataValidationError",
]


class DataAttribution(BaseModel):
    pixel_id: str = FieldInfo(alias="pixelId")

    prid: Literal["jNNdd", "OMzN4"]

    session_id: str = FieldInfo(alias="sessionId")

    type: Literal["website"]

    vid: str


class DataSessionNetworkAsn(BaseModel):
    code: Optional[float] = None

    name: Optional[str] = None


class DataSessionNetworkBotManagement(BaseModel):
    corporate_proxy: Optional[bool] = FieldInfo(alias="corporateProxy", default=None)

    score: Optional[float] = None

    verified_bot: Optional[bool] = FieldInfo(alias="verifiedBot", default=None)

    verified_bot_category: Optional[str] = FieldInfo(alias="verifiedBotCategory", default=None)


class DataSessionNetwork(BaseModel):
    asn: DataSessionNetworkAsn

    bot_management: DataSessionNetworkBotManagement = FieldInfo(alias="botManagement")

    city: Optional[str] = None

    colo: Optional[str] = None

    continent: Optional[str] = None

    country: Optional[str] = None

    ip: Optional[str] = None

    is_eu: Optional[bool] = FieldInfo(alias="isEU", default=None)

    latitude: Optional[str] = None

    longitude: Optional[str] = None

    metro_code: Optional[str] = FieldInfo(alias="metroCode", default=None)

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    region: Optional[str] = None

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)


class DataSessionScreen(BaseModel):
    height: float

    width: float


class DataSessionUtm(BaseModel):
    campaign: Optional[str] = None

    content: Optional[str] = None

    medium: Optional[str] = None

    source: Optional[str] = None

    term: Optional[str] = None


class DataSession(BaseModel):
    created_at: float = FieldInfo(alias="createdAt")

    ended_at: Optional[float] = FieldInfo(alias="endedAt", default=None)

    fbclid: Optional[str] = None

    gclid: Optional[str] = None

    landing_page: str = FieldInfo(alias="landingPage")

    landing_title: Optional[str] = FieldInfo(alias="landingTitle", default=None)

    network: DataSessionNetwork

    pid: str

    referrer: Optional[str] = None

    screen: DataSessionScreen

    sid: str

    tenant: Optional[str] = None

    timezone: str

    user_agent: str = FieldInfo(alias="userAgent")

    utm: DataSessionUtm

    vid: str

    options: Optional[Dict[str, object]] = None


class DataValidationError(BaseModel):
    code: str

    message: str


class DataValidation(BaseModel):
    email: str

    error: Optional[DataValidationError] = None

    provider: str

    validity: Optional[Literal["valid", "invalid", "catch_all", "valid_catch_all"]] = None


class Data(BaseModel):
    attribution: DataAttribution

    session: Optional[DataSession] = None

    validations: List[DataValidation]


class IdentityValidatedWebhookEvent(BaseModel):
    data: Data

    timestamp: datetime
    """When the event was generated"""

    type: Literal["identity.validated"]
    """Event type identifier"""
