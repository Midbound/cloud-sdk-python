# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest
import standardwebhooks

from midbound_cloud import MidboundCloud

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_unwrap(self, client: MidboundCloud) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"id":"evt_01KHEWZ09CQB36JZ5F7D3ZB9NE","created":1739571908123,"data":{"attribution":{"pixelId":"pixelId","prid":"jNNdd","sessionId":"sessionId","type":"website","vid":"vid"},"identity":{"demographics":{"firstName":"firstName","hasChildren":true,"isHomeowner":true,"isMarried":true,"lastName":"lastName"},"emails":[{"type":"personal","value":"value"}],"linkedinUrl":"linkedinUrl","location":{"city":"city","country":"country","state":"state"},"phones":["string"],"professional":{"companyName":"companyName","jobTitle":"jobTitle"}},"session":{"createdAt":0,"endedAt":0,"fbclid":"fbclid","gclid":"gclid","landingPage":"landingPage","landingTitle":"landingTitle","network":{"asn":{"code":0,"name":"name"},"botManagement":{"corporateProxy":true,"score":0,"verifiedBot":true,"verifiedBotCategory":"verifiedBotCategory"},"city":"city","colo":"colo","continent":"continent","country":"country","ip":"ip","isEU":true,"latitude":"latitude","longitude":"longitude","metroCode":"metroCode","postalCode":"postalCode","region":"region","regionCode":"regionCode"},"pid":"pid","referrer":"referrer","screen":{"height":0,"width":0},"sid":"sid","tenant":"tenant","timezone":"timezone","userAgent":"userAgent","utm":{"campaign":"campaign","content":"content","medium":"medium","source":"source","term":"term"},"vid":"vid","options":{"foo":"bar"}}},"type":"identity.resolved"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    def test_method_unwrap(self, client: MidboundCloud) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"id":"evt_01KHEWZ09CQB36JZ5F7D3ZB9NE","created":1739571908123,"data":{"attribution":{"pixelId":"pixelId","prid":"jNNdd","sessionId":"sessionId","type":"website","vid":"vid"},"identity":{"demographics":{"firstName":"firstName","hasChildren":true,"isHomeowner":true,"isMarried":true,"lastName":"lastName"},"emails":[{"type":"personal","value":"value"}],"linkedinUrl":"linkedinUrl","location":{"city":"city","country":"country","state":"state"},"phones":["string"],"professional":{"companyName":"companyName","jobTitle":"jobTitle"}},"session":{"createdAt":0,"endedAt":0,"fbclid":"fbclid","gclid":"gclid","landingPage":"landingPage","landingTitle":"landingTitle","network":{"asn":{"code":0,"name":"name"},"botManagement":{"corporateProxy":true,"score":0,"verifiedBot":true,"verifiedBotCategory":"verifiedBotCategory"},"city":"city","colo":"colo","continent":"continent","country":"country","ip":"ip","isEU":true,"latitude":"latitude","longitude":"longitude","metroCode":"metroCode","postalCode":"postalCode","region":"region","regionCode":"regionCode"},"pid":"pid","referrer":"referrer","screen":{"height":0,"width":0},"sid":"sid","tenant":"tenant","timezone":"timezone","userAgent":"userAgent","utm":{"campaign":"campaign","content":"content","medium":"medium","source":"source","term":"term"},"vid":"vid","options":{"foo":"bar"}}},"type":"identity.resolved"}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)
