# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .identity_enriched_webhook_event import IdentityEnrichedWebhookEvent
from .identity_resolved_webhook_event import IdentityResolvedWebhookEvent
from .identity_qualified_webhook_event import IdentityQualifiedWebhookEvent
from .identity_validated_webhook_event import IdentityValidatedWebhookEvent
from .identity_session_finalized_webhook_event import IdentitySessionFinalizedWebhookEvent

__all__ = ["UnwrapUnsafeWebhookEvent"]

UnwrapUnsafeWebhookEvent: TypeAlias = Annotated[
    Union[
        IdentityResolvedWebhookEvent,
        IdentityQualifiedWebhookEvent,
        IdentityEnrichedWebhookEvent,
        IdentityValidatedWebhookEvent,
        IdentitySessionFinalizedWebhookEvent,
    ],
    PropertyInfo(discriminator="type"),
]
