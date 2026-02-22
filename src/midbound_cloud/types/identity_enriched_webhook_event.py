# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "IdentityEnrichedWebhookEvent",
    "Data",
    "DataAttribution",
    "DataEnrichment",
    "DataEnrichmentCompany",
    "DataEnrichmentCompanyAddress",
    "DataEnrichmentCompanyEstimatedRevenue",
    "DataEnrichmentCompanyFunding",
    "DataEnrichmentCompanyHeadcount",
    "DataEnrichmentCompanyHeadcountGrowth",
    "DataEnrichmentCompanyLinkedinFollowers",
    "DataEnrichmentCompanySeo",
    "DataEnrichmentCompanyTaxonomy",
    "DataEnrichmentCompanyWebTraffic",
    "DataEnrichmentCompanyWebTrafficTrafficSources",
    "DataEnrichmentPerson",
    "DataEnrichmentPersonEducation",
    "DataEnrichmentPersonEmployment",
    "DataEnrichmentPersonEmploymentCompany",
    "DataEnrichmentPersonEmploymentCompanyAddress",
    "DataEnrichmentPersonEmploymentCompanyEstimatedRevenue",
    "DataEnrichmentPersonEmploymentCompanyFunding",
    "DataEnrichmentPersonEmploymentCompanyHeadcount",
    "DataEnrichmentPersonEmploymentCompanyHeadcountGrowth",
    "DataEnrichmentPersonEmploymentCompanyLinkedinFollowers",
    "DataEnrichmentPersonEmploymentCompanySeo",
    "DataEnrichmentPersonEmploymentCompanyTaxonomy",
    "DataEnrichmentPersonEmploymentCompanyWebTraffic",
    "DataEnrichmentPersonEmploymentCompanyWebTrafficTrafficSources",
    "DataEnrichmentPersonExperience",
    "DataEnrichmentPersonExperienceCompany",
    "DataEnrichmentPersonExperienceCompanyAddress",
    "DataEnrichmentPersonLocation",
    "DataEnrichmentEmailValidation",
    "DataEnrichmentEmailValidationError",
    "DataQuery",
    "DataSession",
    "DataSessionNetwork",
    "DataSessionNetworkAsn",
    "DataSessionNetworkBotManagement",
    "DataSessionScreen",
    "DataSessionUtm",
]


class DataAttribution(BaseModel):
    pixel_id: str = FieldInfo(alias="pixelId")

    prid: Literal["jNNdd", "OMzN4"]

    session_id: str = FieldInfo(alias="sessionId")

    type: Literal["website"]

    vid: str


class DataEnrichmentCompanyAddress(BaseModel):
    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    locality: Optional[str] = None

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    region: Optional[str] = None


class DataEnrichmentCompanyEstimatedRevenue(BaseModel):
    currency: Optional[str] = None

    max: Optional[float] = None

    min: Optional[float] = None


class DataEnrichmentCompanyFunding(BaseModel):
    days_since_last_round: Optional[float] = FieldInfo(alias="daysSinceLastRound", default=None)

    investors: Optional[List[str]] = None

    last_round_amount_usd: Optional[float] = FieldInfo(alias="lastRoundAmountUsd", default=None)

    last_round_type: Optional[str] = FieldInfo(alias="lastRoundType", default=None)

    total_raised_usd: Optional[float] = FieldInfo(alias="totalRaisedUsd", default=None)


class DataEnrichmentCompanyHeadcountGrowth(BaseModel):
    mom: Optional[float] = None

    qoq: Optional[float] = None

    yoy: Optional[float] = None


class DataEnrichmentCompanyHeadcount(BaseModel):
    growth: Optional[DataEnrichmentCompanyHeadcountGrowth] = None

    total: Optional[float] = None


class DataEnrichmentCompanyLinkedinFollowers(BaseModel):
    count: Optional[float] = None

    mom_growth_percent: Optional[float] = FieldInfo(alias="momGrowthPercent", default=None)

    qoq_growth_percent: Optional[float] = FieldInfo(alias="qoqGrowthPercent", default=None)

    yoy_growth_percent: Optional[float] = FieldInfo(alias="yoyGrowthPercent", default=None)


class DataEnrichmentCompanySeo(BaseModel):
    average_ad_rank: Optional[float] = FieldInfo(alias="averageAdRank", default=None)

    average_organic_rank: Optional[float] = FieldInfo(alias="averageOrganicRank", default=None)

    monthly_ads_spend: Optional[float] = FieldInfo(alias="monthlyAdsSpend", default=None)

    monthly_organic_clicks: Optional[float] = FieldInfo(alias="monthlyOrganicClicks", default=None)

    monthly_organic_value: Optional[float] = FieldInfo(alias="monthlyOrganicValue", default=None)

    monthly_paid_clicks: Optional[float] = FieldInfo(alias="monthlyPaidClicks", default=None)

    total_organic_keywords: Optional[float] = FieldInfo(alias="totalOrganicKeywords", default=None)


class DataEnrichmentCompanyTaxonomy(BaseModel):
    linkedin_industry: Optional[str] = FieldInfo(alias="linkedinIndustry", default=None)

    linkedin_specialties: Optional[List[str]] = FieldInfo(alias="linkedinSpecialties", default=None)


class DataEnrichmentCompanyWebTrafficTrafficSources(BaseModel):
    direct_percent: Optional[float] = FieldInfo(alias="directPercent", default=None)

    paid_referral_percent: Optional[float] = FieldInfo(alias="paidReferralPercent", default=None)

    referral_percent: Optional[float] = FieldInfo(alias="referralPercent", default=None)

    search_percent: Optional[float] = FieldInfo(alias="searchPercent", default=None)

    social_percent: Optional[float] = FieldInfo(alias="socialPercent", default=None)


class DataEnrichmentCompanyWebTraffic(BaseModel):
    mom_growth_percent: Optional[float] = FieldInfo(alias="momGrowthPercent", default=None)

    monthly_visitors: Optional[float] = FieldInfo(alias="monthlyVisitors", default=None)

    qoq_growth_percent: Optional[float] = FieldInfo(alias="qoqGrowthPercent", default=None)

    traffic_sources: Optional[DataEnrichmentCompanyWebTrafficTrafficSources] = FieldInfo(
        alias="trafficSources", default=None
    )


class DataEnrichmentCompany(BaseModel):
    api_type: Literal["full"] = FieldInfo(alias="_type")

    enriched_at: str = FieldInfo(alias="enrichedAt")

    name: str

    provider: Literal["xK9mP", "qR7nL"]

    address: Optional[DataEnrichmentCompanyAddress] = None

    description: Optional[str] = None

    domain: Optional[str] = None

    employee_count: Optional[float] = FieldInfo(alias="employeeCount", default=None)

    estimated_revenue: Optional[DataEnrichmentCompanyEstimatedRevenue] = FieldInfo(
        alias="estimatedRevenue", default=None
    )

    founded_year: Optional[float] = FieldInfo(alias="foundedYear", default=None)

    funding: Optional[DataEnrichmentCompanyFunding] = None

    headcount: Optional[DataEnrichmentCompanyHeadcount] = None

    industry: Optional[str] = None

    linkedin_followers: Optional[DataEnrichmentCompanyLinkedinFollowers] = FieldInfo(
        alias="linkedinFollowers", default=None
    )

    linkedin_id: Optional[str] = FieldInfo(alias="linkedinId", default=None)

    linkedin_url: Optional[str] = FieldInfo(alias="linkedinUrl", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    seo: Optional[DataEnrichmentCompanySeo] = None

    specialties: Optional[List[str]] = None

    taxonomy: Optional[DataEnrichmentCompanyTaxonomy] = None

    website: Optional[str] = None

    web_traffic: Optional[DataEnrichmentCompanyWebTraffic] = FieldInfo(alias="webTraffic", default=None)


class DataEnrichmentPersonEducation(BaseModel):
    institute_name: str = FieldInfo(alias="instituteName")

    degree: Optional[str] = None

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    field_of_study: Optional[str] = FieldInfo(alias="fieldOfStudy", default=None)

    institute_linkedin_id: Optional[str] = FieldInfo(alias="instituteLinkedinId", default=None)

    institute_logo_url: Optional[str] = FieldInfo(alias="instituteLogoUrl", default=None)

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)


class DataEnrichmentPersonEmploymentCompanyAddress(BaseModel):
    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    locality: Optional[str] = None

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    region: Optional[str] = None


class DataEnrichmentPersonEmploymentCompanyEstimatedRevenue(BaseModel):
    currency: Optional[str] = None

    max: Optional[float] = None

    min: Optional[float] = None


class DataEnrichmentPersonEmploymentCompanyFunding(BaseModel):
    days_since_last_round: Optional[float] = FieldInfo(alias="daysSinceLastRound", default=None)

    investors: Optional[List[str]] = None

    last_round_amount_usd: Optional[float] = FieldInfo(alias="lastRoundAmountUsd", default=None)

    last_round_type: Optional[str] = FieldInfo(alias="lastRoundType", default=None)

    total_raised_usd: Optional[float] = FieldInfo(alias="totalRaisedUsd", default=None)


class DataEnrichmentPersonEmploymentCompanyHeadcountGrowth(BaseModel):
    mom: Optional[float] = None

    qoq: Optional[float] = None

    yoy: Optional[float] = None


class DataEnrichmentPersonEmploymentCompanyHeadcount(BaseModel):
    growth: Optional[DataEnrichmentPersonEmploymentCompanyHeadcountGrowth] = None

    total: Optional[float] = None


class DataEnrichmentPersonEmploymentCompanyLinkedinFollowers(BaseModel):
    count: Optional[float] = None

    mom_growth_percent: Optional[float] = FieldInfo(alias="momGrowthPercent", default=None)

    qoq_growth_percent: Optional[float] = FieldInfo(alias="qoqGrowthPercent", default=None)

    yoy_growth_percent: Optional[float] = FieldInfo(alias="yoyGrowthPercent", default=None)


class DataEnrichmentPersonEmploymentCompanySeo(BaseModel):
    average_ad_rank: Optional[float] = FieldInfo(alias="averageAdRank", default=None)

    average_organic_rank: Optional[float] = FieldInfo(alias="averageOrganicRank", default=None)

    monthly_ads_spend: Optional[float] = FieldInfo(alias="monthlyAdsSpend", default=None)

    monthly_organic_clicks: Optional[float] = FieldInfo(alias="monthlyOrganicClicks", default=None)

    monthly_organic_value: Optional[float] = FieldInfo(alias="monthlyOrganicValue", default=None)

    monthly_paid_clicks: Optional[float] = FieldInfo(alias="monthlyPaidClicks", default=None)

    total_organic_keywords: Optional[float] = FieldInfo(alias="totalOrganicKeywords", default=None)


class DataEnrichmentPersonEmploymentCompanyTaxonomy(BaseModel):
    linkedin_industry: Optional[str] = FieldInfo(alias="linkedinIndustry", default=None)

    linkedin_specialties: Optional[List[str]] = FieldInfo(alias="linkedinSpecialties", default=None)


class DataEnrichmentPersonEmploymentCompanyWebTrafficTrafficSources(BaseModel):
    direct_percent: Optional[float] = FieldInfo(alias="directPercent", default=None)

    paid_referral_percent: Optional[float] = FieldInfo(alias="paidReferralPercent", default=None)

    referral_percent: Optional[float] = FieldInfo(alias="referralPercent", default=None)

    search_percent: Optional[float] = FieldInfo(alias="searchPercent", default=None)

    social_percent: Optional[float] = FieldInfo(alias="socialPercent", default=None)


class DataEnrichmentPersonEmploymentCompanyWebTraffic(BaseModel):
    mom_growth_percent: Optional[float] = FieldInfo(alias="momGrowthPercent", default=None)

    monthly_visitors: Optional[float] = FieldInfo(alias="monthlyVisitors", default=None)

    qoq_growth_percent: Optional[float] = FieldInfo(alias="qoqGrowthPercent", default=None)

    traffic_sources: Optional[DataEnrichmentPersonEmploymentCompanyWebTrafficTrafficSources] = FieldInfo(
        alias="trafficSources", default=None
    )


class DataEnrichmentPersonEmploymentCompany(BaseModel):
    api_type: Literal["full"] = FieldInfo(alias="_type")

    enriched_at: str = FieldInfo(alias="enrichedAt")

    name: str

    provider: Literal["xK9mP", "qR7nL"]

    address: Optional[DataEnrichmentPersonEmploymentCompanyAddress] = None

    description: Optional[str] = None

    domain: Optional[str] = None

    employee_count: Optional[float] = FieldInfo(alias="employeeCount", default=None)

    estimated_revenue: Optional[DataEnrichmentPersonEmploymentCompanyEstimatedRevenue] = FieldInfo(
        alias="estimatedRevenue", default=None
    )

    founded_year: Optional[float] = FieldInfo(alias="foundedYear", default=None)

    funding: Optional[DataEnrichmentPersonEmploymentCompanyFunding] = None

    headcount: Optional[DataEnrichmentPersonEmploymentCompanyHeadcount] = None

    industry: Optional[str] = None

    linkedin_followers: Optional[DataEnrichmentPersonEmploymentCompanyLinkedinFollowers] = FieldInfo(
        alias="linkedinFollowers", default=None
    )

    linkedin_id: Optional[str] = FieldInfo(alias="linkedinId", default=None)

    linkedin_url: Optional[str] = FieldInfo(alias="linkedinUrl", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    seo: Optional[DataEnrichmentPersonEmploymentCompanySeo] = None

    specialties: Optional[List[str]] = None

    taxonomy: Optional[DataEnrichmentPersonEmploymentCompanyTaxonomy] = None

    website: Optional[str] = None

    web_traffic: Optional[DataEnrichmentPersonEmploymentCompanyWebTraffic] = FieldInfo(alias="webTraffic", default=None)


class DataEnrichmentPersonEmployment(BaseModel):
    company: DataEnrichmentPersonEmploymentCompany

    title: str

    description: Optional[str] = None

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    location: Optional[str] = None

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)


class DataEnrichmentPersonExperienceCompanyAddress(BaseModel):
    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    locality: Optional[str] = None

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    region: Optional[str] = None


class DataEnrichmentPersonExperienceCompany(BaseModel):
    api_type: Literal["basic"] = FieldInfo(alias="_type")

    name: str

    address: Optional[DataEnrichmentPersonExperienceCompanyAddress] = None

    description: Optional[str] = None

    domain: Optional[str] = None

    employee_count: Optional[float] = FieldInfo(alias="employeeCount", default=None)

    founded_year: Optional[float] = FieldInfo(alias="foundedYear", default=None)

    industry: Optional[str] = None

    linkedin_id: Optional[str] = FieldInfo(alias="linkedinId", default=None)

    linkedin_url: Optional[str] = FieldInfo(alias="linkedinUrl", default=None)

    logo_url: Optional[str] = FieldInfo(alias="logoUrl", default=None)

    website: Optional[str] = None


class DataEnrichmentPersonExperience(BaseModel):
    company: DataEnrichmentPersonExperienceCompany

    title: str

    description: Optional[str] = None

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    location: Optional[str] = None

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)


class DataEnrichmentPersonLocation(BaseModel):
    country: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    locality: Optional[str] = None

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)

    raw: Optional[str] = None

    region: Optional[str] = None


class DataEnrichmentPerson(BaseModel):
    enriched_at: str = FieldInfo(alias="enrichedAt")

    linkedin_url: str = FieldInfo(alias="linkedinUrl")

    provider: Literal["xK9mP", "qR7nL"]

    connections: Optional[float] = None

    education: Optional[List[DataEnrichmentPersonEducation]] = None

    email: Optional[str] = None

    employments: Optional[List[DataEnrichmentPersonEmployment]] = None

    experience: Optional[List[DataEnrichmentPersonExperience]] = None

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)

    headline: Optional[str] = None

    languages: Optional[List[str]] = None

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    linkedin_id: Optional[str] = FieldInfo(alias="linkedinId", default=None)

    location: Optional[DataEnrichmentPersonLocation] = None

    profile_picture_url: Optional[str] = FieldInfo(alias="profilePictureUrl", default=None)

    skills: Optional[List[str]] = None

    summary: Optional[str] = None


class DataEnrichmentEmailValidationError(BaseModel):
    code: str

    message: str


class DataEnrichmentEmailValidation(BaseModel):
    email: str

    error: Optional[DataEnrichmentEmailValidationError] = None

    provider: str

    validity: Optional[Literal["valid", "invalid", "catch_all", "valid_catch_all"]] = None


class DataEnrichment(BaseModel):
    companies: List[DataEnrichmentCompany]

    person: Optional[DataEnrichmentPerson] = None

    email_validations: Optional[List[DataEnrichmentEmailValidation]] = FieldInfo(alias="emailValidations", default=None)


class DataQuery(BaseModel):
    match: Literal["linkedinUrl"]

    type: Literal["person"]

    value: str


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


class Data(BaseModel):
    attribution: DataAttribution

    companies_enriched: float = FieldInfo(alias="companiesEnriched")

    enrichment: Optional[DataEnrichment] = None

    query: DataQuery

    session: Optional[DataSession] = None


class IdentityEnrichedWebhookEvent(BaseModel):
    id: str
    """Unique event identifier"""

    created: int
    """Unix timestamp (milliseconds) when the event was created"""

    data: Data

    type: Literal["identity.enriched"]
    """Event type identifier"""
