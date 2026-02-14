from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `midbound_cloud.resources` module.

    This is used so that we can lazily import `midbound_cloud.resources` only when
    needed *and* so that users can just import `midbound_cloud` and reference `midbound_cloud.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("midbound_cloud.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
