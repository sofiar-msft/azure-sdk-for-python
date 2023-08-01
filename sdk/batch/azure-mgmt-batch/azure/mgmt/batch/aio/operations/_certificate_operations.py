# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._certificate_operations import (
    build_cancel_deletion_request,
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_batch_account_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CertificateOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.batch.aio.BatchManagementClient`'s
        :attr:`certificate` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_batch_account(
        self,
        resource_group_name: str,
        account_name: str,
        maxresults: Optional[int] = None,
        select: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.Certificate"]:
        """Lists all of the certificates in the specified account.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param maxresults: The maximum number of items to return in the response. Default value is
         None.
        :type maxresults: int
        :param select: Comma separated list of properties that should be returned. e.g.
         "properties/provisioningState". Only top level properties under properties/ are valid for
         selection. Default value is None.
        :type select: str
        :param filter: OData filter expression. Valid properties for filtering are
         "properties/provisioningState", "properties/provisioningStateTransitionTime", "name". Default
         value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Certificate or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.batch.models.Certificate]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ListCertificatesResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_batch_account_request(
                    resource_group_name=resource_group_name,
                    account_name=account_name,
                    subscription_id=self._config.subscription_id,
                    maxresults=maxresults,
                    select=select,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_batch_account.metadata["url"],
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
            deserialized = self._deserialize("ListCertificatesResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_batch_account.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates"
    }

    @overload
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        certificate_name: str,
        parameters: _models.CertificateCreateOrUpdateParameters,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Creates a new certificate inside the specified account.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :param parameters: Additional parameters for certificate creation. Required.
        :type parameters: ~azure.mgmt.batch.models.CertificateCreateOrUpdateParameters
        :param if_match: The entity state (ETag) version of the certificate to update. A value of "*"
         can be used to apply the operation only if the certificate already exists. If omitted, this
         operation will always be applied. Default value is None.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new certificate to be created, but to prevent
         updating an existing certificate. Other values will be ignored. Default value is None.
        :type if_none_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        certificate_name: str,
        parameters: IO,
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Creates a new certificate inside the specified account.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :param parameters: Additional parameters for certificate creation. Required.
        :type parameters: IO
        :param if_match: The entity state (ETag) version of the certificate to update. A value of "*"
         can be used to apply the operation only if the certificate already exists. If omitted, this
         operation will always be applied. Default value is None.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new certificate to be created, but to prevent
         updating an existing certificate. Other values will be ignored. Default value is None.
        :type if_none_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        account_name: str,
        certificate_name: str,
        parameters: Union[_models.CertificateCreateOrUpdateParameters, IO],
        if_match: Optional[str] = None,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Certificate:
        """Creates a new certificate inside the specified account.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :param parameters: Additional parameters for certificate creation. Is either a
         CertificateCreateOrUpdateParameters type or a IO type. Required.
        :type parameters: ~azure.mgmt.batch.models.CertificateCreateOrUpdateParameters or IO
        :param if_match: The entity state (ETag) version of the certificate to update. A value of "*"
         can be used to apply the operation only if the certificate already exists. If omitted, this
         operation will always be applied. Default value is None.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new certificate to be created, but to prevent
         updating an existing certificate. Other values will be ignored. Default value is None.
        :type if_none_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "CertificateCreateOrUpdateParameters")

        request = build_create_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            if_none_match=if_none_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("Certificate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}"
    }

    @overload
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        certificate_name: str,
        parameters: _models.CertificateCreateOrUpdateParameters,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Updates the properties of an existing certificate.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :param parameters: Certificate entity to update. Required.
        :type parameters: ~azure.mgmt.batch.models.CertificateCreateOrUpdateParameters
        :param if_match: The entity state (ETag) version of the certificate to update. This value can
         be omitted or set to "*" to apply the operation unconditionally. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        certificate_name: str,
        parameters: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.Certificate:
        """Updates the properties of an existing certificate.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :param parameters: Certificate entity to update. Required.
        :type parameters: IO
        :param if_match: The entity state (ETag) version of the certificate to update. This value can
         be omitted or set to "*" to apply the operation unconditionally. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        account_name: str,
        certificate_name: str,
        parameters: Union[_models.CertificateCreateOrUpdateParameters, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.Certificate:
        """Updates the properties of an existing certificate.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :param parameters: Certificate entity to update. Is either a
         CertificateCreateOrUpdateParameters type or a IO type. Required.
        :type parameters: ~azure.mgmt.batch.models.CertificateCreateOrUpdateParameters or IO
        :param if_match: The entity state (ETag) version of the certificate to update. This value can
         be omitted or set to "*" to apply the operation unconditionally. Default value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "CertificateCreateOrUpdateParameters")

        request = build_update_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
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
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("Certificate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}"
    }

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, account_name: str, certificate_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
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

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))
            response_headers["Retry-After"] = self._deserialize("int", response.headers.get("Retry-After"))

        if cls:
            return cls(pipeline_response, None, response_headers)

    _delete_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}"
    }

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, account_name: str, certificate_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes the specified certificate.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                account_name=account_name,
                certificate_name=certificate_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}"
    }

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, account_name: str, certificate_name: str, **kwargs: Any
    ) -> _models.Certificate:
        """Gets information about the specified certificate.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            certificate_name=certificate_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("Certificate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}"
    }

    @distributed_trace_async
    async def cancel_deletion(
        self, resource_group_name: str, account_name: str, certificate_name: str, **kwargs: Any
    ) -> _models.Certificate:
        """Cancels a failed deletion of a certificate from the specified account.

        If you try to delete a certificate that is being used by a pool or compute node, the status of
        the certificate changes to deleteFailed. If you decide that you want to continue using the
        certificate, you can use this operation to set the status of the certificate back to active. If
        you intend to delete the certificate, you do not need to run this operation after the deletion
        failed. You must make sure that the certificate is not being used by any resources, and then
        you can try again to delete the certificate.

        Warning: This operation is deprecated and will be removed after February, 2024. Please use the
        `Azure KeyVault Extension
        <https://learn.microsoft.com/azure/batch/batch-certificate-migration-guide>`_ instead.

        :param resource_group_name: The name of the resource group that contains the Batch account.
         Required.
        :type resource_group_name: str
        :param account_name: The name of the Batch account. Required.
        :type account_name: str
        :param certificate_name: The identifier for the certificate. This must be made up of algorithm
         and thumbprint separated by a dash, and must match the certificate data in the request. For
         example SHA1-a3d1c5. Required.
        :type certificate_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Certificate or the result of cls(response)
        :rtype: ~azure.mgmt.batch.models.Certificate
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Certificate] = kwargs.pop("cls", None)

        request = build_cancel_deletion_request(
            resource_group_name=resource_group_name,
            account_name=account_name,
            certificate_name=certificate_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.cancel_deletion.metadata["url"],
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        response_headers = {}
        response_headers["ETag"] = self._deserialize("str", response.headers.get("ETag"))

        deserialized = self._deserialize("Certificate", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    cancel_deletion.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Batch/batchAccounts/{accountName}/certificates/{certificateName}/cancelDelete"
    }
