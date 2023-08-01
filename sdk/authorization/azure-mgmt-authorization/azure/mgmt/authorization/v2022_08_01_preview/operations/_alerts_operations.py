# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(scope: str, alert_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "alertId": _SERIALIZER.url("alert_id", alert_id, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(scope: str, alert_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "alertId": _SERIALIZER.url("alert_id", alert_id, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_for_scope_request(scope: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_refresh_request(scope: str, alert_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}/refresh"
    )
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "alertId": _SERIALIZER.url("alert_id", alert_id, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_refresh_all_request(scope: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-08-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/refresh")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class AlertsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.authorization.v2022_08_01_preview.AuthorizationManagementClient`'s
        :attr:`alerts` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def get(self, scope: str, alert_id: str, **kwargs: Any) -> _models.Alert:
        """Get the specified alert.

        :param scope: The scope of the alert. The scope can be any REST resource instance. For example,
         use '/providers/Microsoft.Subscription/subscriptions/{subscription-id}/' for a subscription,
         '/providers/Microsoft.Subscription/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}'
         for a resource group, and
         '/providers/Microsoft.Subscription/subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/providers/{resource-provider}/{resource-type}/{resource-name}'
         for a resource. Required.
        :type scope: str
        :param alert_id: The name of the alert to get. Required.
        :type alert_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Alert or the result of cls(response)
        :rtype: ~azure.mgmt.authorization.v2022_08_01_preview.models.Alert
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        cls: ClsType[_models.Alert] = kwargs.pop("cls", None)

        request = build_get_request(
            scope=scope,
            alert_id=alert_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Alert", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}"}

    @overload
    def update(  # pylint: disable=inconsistent-return-statements
        self,
        scope: str,
        alert_id: str,
        parameters: _models.Alert,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Update an alert.

        :param scope: The scope of the alert. Required.
        :type scope: str
        :param alert_id: The name of the alert to dismiss. Required.
        :type alert_id: str
        :param parameters: Parameters for the alert. Required.
        :type parameters: ~azure.mgmt.authorization.v2022_08_01_preview.models.Alert
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(  # pylint: disable=inconsistent-return-statements
        self, scope: str, alert_id: str, parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> None:
        """Update an alert.

        :param scope: The scope of the alert. Required.
        :type scope: str
        :param alert_id: The name of the alert to dismiss. Required.
        :type alert_id: str
        :param parameters: Parameters for the alert. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(  # pylint: disable=inconsistent-return-statements
        self, scope: str, alert_id: str, parameters: Union[_models.Alert, IO], **kwargs: Any
    ) -> None:
        """Update an alert.

        :param scope: The scope of the alert. Required.
        :type scope: str
        :param alert_id: The name of the alert to dismiss. Required.
        :type alert_id: str
        :param parameters: Parameters for the alert. Is either a Alert type or a IO type. Required.
        :type parameters: ~azure.mgmt.authorization.v2022_08_01_preview.models.Alert or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "Alert")

        request = build_update_request(
            scope=scope,
            alert_id=alert_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}"}

    @distributed_trace
    def list_for_scope(self, scope: str, **kwargs: Any) -> Iterable["_models.Alert"]:
        """Gets alerts for a resource scope.

        :param scope: The scope of the alert. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Alert or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.authorization.v2022_08_01_preview.models.Alert]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_for_scope_request(
                    scope=scope,
                    api_version=api_version,
                    template_url=self.list_for_scope.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AlertListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_for_scope.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts"}

    def _refresh_initial(self, scope: str, alert_id: str, **kwargs: Any) -> _models.AlertOperationResult:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertOperationResult] = kwargs.pop("cls", None)

        request = build_refresh_request(
            scope=scope,
            alert_id=alert_id,
            api_version=api_version,
            template_url=self._refresh_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        deserialized = self._deserialize("AlertOperationResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _refresh_initial.metadata = {
        "url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}/refresh"
    }

    @distributed_trace
    def begin_refresh(self, scope: str, alert_id: str, **kwargs: Any) -> LROPoller[_models.AlertOperationResult]:
        """Refresh an alert.

        :param scope: The scope of the alert. Required.
        :type scope: str
        :param alert_id: The name of the alert to refresh. Required.
        :type alert_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either AlertOperationResult or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.authorization.v2022_08_01_preview.models.AlertOperationResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertOperationResult] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._refresh_initial(
                scope=scope,
                alert_id=alert_id,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = self._deserialize("AlertOperationResult", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_refresh.metadata = {
        "url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/{alertId}/refresh"
    }

    def _refresh_all_initial(self, scope: str, **kwargs: Any) -> _models.AlertOperationResult:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertOperationResult] = kwargs.pop("cls", None)

        request = build_refresh_all_request(
            scope=scope,
            api_version=api_version,
            template_url=self._refresh_all_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        deserialized = self._deserialize("AlertOperationResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _refresh_all_initial.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/refresh"}

    @distributed_trace
    def begin_refresh_all(self, scope: str, **kwargs: Any) -> LROPoller[_models.AlertOperationResult]:
        """Refresh all alerts for a resource scope.

        :param scope: The scope of the alert. Required.
        :type scope: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either AlertOperationResult or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.authorization.v2022_08_01_preview.models.AlertOperationResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-08-01-preview")
        )
        cls: ClsType[_models.AlertOperationResult] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._refresh_all_initial(
                scope=scope, api_version=api_version, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

            deserialized = self._deserialize("AlertOperationResult", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, response_headers)
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_refresh_all.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleManagementAlerts/refresh"}
