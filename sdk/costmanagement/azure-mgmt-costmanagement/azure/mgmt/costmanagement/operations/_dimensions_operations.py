# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    scope: str,
    *,
    filter: Optional[str] = None,
    expand: Optional[str] = None,
    skiptoken: Optional[str] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.CostManagement/dimensions")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
    if skiptoken is not None:
        _params["$skiptoken"] = _SERIALIZER.query("skiptoken", skiptoken, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", maximum=1000, minimum=1)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_by_external_cloud_provider_type_request(
    external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
    external_cloud_provider_id: str,
    *,
    filter: Optional[str] = None,
    expand: Optional[str] = None,
    skiptoken: Optional[str] = None,
    top: Optional[int] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2022-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/dimensions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "externalCloudProviderType": _SERIALIZER.url(
            "external_cloud_provider_type", external_cloud_provider_type, "str"
        ),
        "externalCloudProviderId": _SERIALIZER.url("external_cloud_provider_id", external_cloud_provider_id, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
    if skiptoken is not None:
        _params["$skiptoken"] = _SERIALIZER.query("skiptoken", skiptoken, "str")
    if top is not None:
        _params["$top"] = _SERIALIZER.query("top", top, "int", maximum=1000, minimum=1)

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class DimensionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.costmanagement.CostManagementClient`'s
        :attr:`dimensions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        scope: str,
        filter: Optional[str] = None,
        expand: Optional[str] = None,
        skiptoken: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.Dimension"]:
        """Lists the dimensions by the defined scope.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param scope: The scope associated with dimension operations. This includes
         '/subscriptions/{subscriptionId}/' for subscription scope,
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}'
         for Department scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}'
         for EnrollmentAccount scope,
         '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group
         scope,
         '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}'
         for billingProfile scope,
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}'
         for invoiceSection scope, and
         'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}'
         specific for partners. Required.
        :type scope: str
        :param filter: May be used to filter dimensions by properties/category, properties/usageStart,
         properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'. Default value is
         None.
        :type filter: str
        :param expand: May be used to expand the properties/data within a dimension category. By
         default, data is not included when listing dimensions. Default value is None.
        :type expand: str
        :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skiptoken parameter that specifies a starting point to use for subsequent calls. Default
         value is None.
        :type skiptoken: str
        :param top: May be used to limit the number of results to the most recent N dimension data.
         Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Dimension or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.costmanagement.models.Dimension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.DimensionsListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    scope=scope,
                    filter=filter,
                    expand=expand,
                    skiptoken=skiptoken,
                    top=top,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DimensionsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200, 204]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{scope}/providers/Microsoft.CostManagement/dimensions"}

    @distributed_trace
    def by_external_cloud_provider_type(
        self,
        external_cloud_provider_type: Union[str, _models.ExternalCloudProviderType],
        external_cloud_provider_id: str,
        filter: Optional[str] = None,
        expand: Optional[str] = None,
        skiptoken: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> Iterable["_models.Dimension"]:
        """Lists the dimensions by the external cloud provider type.

        .. seealso::
           - https://docs.microsoft.com/en-us/rest/api/costmanagement/

        :param external_cloud_provider_type: The external cloud provider type associated with
         dimension/query operations. This includes 'externalSubscriptions' for linked account and
         'externalBillingAccounts' for consolidated account. Known values are: "externalSubscriptions"
         and "externalBillingAccounts". Required.
        :type external_cloud_provider_type: str or
         ~azure.mgmt.costmanagement.models.ExternalCloudProviderType
        :param external_cloud_provider_id: This can be '{externalSubscriptionId}' for linked account or
         '{externalBillingAccountId}' for consolidated account used with dimension/query operations.
         Required.
        :type external_cloud_provider_id: str
        :param filter: May be used to filter dimensions by properties/category, properties/usageStart,
         properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'. Default value is
         None.
        :type filter: str
        :param expand: May be used to expand the properties/data within a dimension category. By
         default, data is not included when listing dimensions. Default value is None.
        :type expand: str
        :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If
         a previous response contains a nextLink element, the value of the nextLink element will include
         a skiptoken parameter that specifies a starting point to use for subsequent calls. Default
         value is None.
        :type skiptoken: str
        :param top: May be used to limit the number of results to the most recent N dimension data.
         Default value is None.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Dimension or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.costmanagement.models.Dimension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.DimensionsListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_by_external_cloud_provider_type_request(
                    external_cloud_provider_type=external_cloud_provider_type,
                    external_cloud_provider_id=external_cloud_provider_id,
                    filter=filter,
                    expand=expand,
                    skiptoken=skiptoken,
                    top=top,
                    api_version=api_version,
                    template_url=self.by_external_cloud_provider_type.metadata["url"],
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
            deserialized = self._deserialize("DimensionsListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    by_external_cloud_provider_type.metadata = {
        "url": "/providers/Microsoft.CostManagement/{externalCloudProviderType}/{externalCloudProviderId}/dimensions"
    }
