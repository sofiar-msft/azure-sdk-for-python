# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Literal, Optional

from azure.core.pipeline import policies

VERSION = "unknown"


class AzureDataLakeStorageRESTAPIConfiguration:  # pylint: disable=too-many-instance-attributes,name-too-long
    """Configuration for AzureDataLakeStorageRESTAPI.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param url: The URL of the service account, container, or blob that is the target of the
     desired operation. Required.
    :type url: str
    :param x_ms_lease_duration: The lease duration is required to acquire a lease, and specifies
     the duration of the lease in seconds.  The lease duration must be between 15 and 60 seconds or
     -1 for infinite lease. Default value is None.
    :type x_ms_lease_duration: int
    :keyword resource: The value must be "filesystem" for all filesystem operations. Default value
     is "filesystem". Note that overriding this default value may result in unsupported behavior.
    :paramtype resource: str
    :keyword version: Specifies the version of the operation to use for this request. Default value
     is "2023-05-03". Note that overriding this default value may result in unsupported behavior.
    :paramtype version: str
    """

    def __init__(self, url: str, x_ms_lease_duration: Optional[int] = None, **kwargs: Any) -> None:
        resource: Literal["filesystem"] = kwargs.pop("resource", "filesystem")
        version: Literal["2023-05-03"] = kwargs.pop("version", "2023-05-03")

        if url is None:
            raise ValueError("Parameter 'url' must not be None.")

        self.url = url
        self.x_ms_lease_duration = x_ms_lease_duration
        self.resource = resource
        self.version = version
        kwargs.setdefault("sdk_moniker", "azuredatalakestoragerestapi/{}".format(VERSION))
        self.polling_interval = kwargs.get("polling_interval", 30)
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or policies.HttpLoggingPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.AsyncRedirectPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.AsyncRetryPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
