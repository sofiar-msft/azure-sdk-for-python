# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._operations import build_changes_get_request, build_changes_list_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ChangesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.resource.changes.v2022_05_01.aio.ChangesClient`'s
        :attr:`changes` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        resource_provider_namespace: str,
        resource_type: str,
        resource_name: str,
        top: int = 100,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ChangeResourceResult"]:
        """Obtains a list of change resources from the past 14 days for the target resource.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_provider_namespace: The name of the resource provider namespace. Required.
        :type resource_provider_namespace: str
        :param resource_type: The name of the resource type. Required.
        :type resource_type: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param top: (Optional) Set the maximum number of results per response. Default value is 100.
        :type top: int
        :param skip_token: (Optional) The page-continuation token. Default value is None.
        :type skip_token: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ChangeResourceResult or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.resource.changes.v2022_05_01.models.ChangeResourceResult]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-05-01"))
        cls: ClsType[_models.ChangeResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_changes_list_request(
                    resource_group_name=resource_group_name,
                    resource_provider_namespace=resource_provider_namespace,
                    resource_type=resource_type,
                    resource_name=resource_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    skip_token=skip_token,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("ChangeResourceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Resources/changes"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        resource_provider_namespace: str,
        resource_type: str,
        resource_name: str,
        change_resource_id: str,
        **kwargs: Any
    ) -> _models.ChangeResourceResult:
        """Obtains the specified change resource for the target resource.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_provider_namespace: The name of the resource provider namespace. Required.
        :type resource_provider_namespace: str
        :param resource_type: The name of the resource type. Required.
        :type resource_type: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param change_resource_id: The ID of the change resource. Required.
        :type change_resource_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ChangeResourceResult or the result of cls(response)
        :rtype: ~azure.mgmt.resource.changes.v2022_05_01.models.ChangeResourceResult
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-05-01"))
        cls: ClsType[_models.ChangeResourceResult] = kwargs.pop("cls", None)

        request = build_changes_get_request(
            resource_group_name=resource_group_name,
            resource_provider_namespace=resource_provider_namespace,
            resource_type=resource_type,
            resource_name=resource_name,
            change_resource_id=change_resource_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ChangeResourceResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}/providers/Microsoft.Resources/changes/{changeResourceId}"
    }
