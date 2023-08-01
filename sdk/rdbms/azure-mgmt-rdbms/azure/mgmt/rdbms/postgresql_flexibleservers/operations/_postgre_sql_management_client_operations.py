# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import PostgreSQLManagementClientMixinABC, _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_check_migration_name_availability_request(
    subscription_id: str, resource_group_name: str, target_db_server_name: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{targetDbServerName}/checkMigrationNameAvailability",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id",
            subscription_id,
            "str",
            pattern=r"([a-z0-9]){8,8}[-]([a-z0-9]){4,4}[-]([a-z0-9]){4,4}[-]([a-z0-9]){4,4}[-]([a-z0-9]){12,12}",
        ),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", pattern=r"^[-a-z0-9A-Z._()]+[^.]$"
        ),
        "targetDbServerName": _SERIALIZER.url(
            "target_db_server_name", target_db_server_name, "str", pattern=r"([-a-z0-9]){3,63}"
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class PostgreSQLManagementClientOperationsMixin(PostgreSQLManagementClientMixinABC):
    @overload
    def check_migration_name_availability(
        self,
        subscription_id: str,
        resource_group_name: str,
        target_db_server_name: str,
        parameters: _models.MigrationNameAvailabilityResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.MigrationNameAvailabilityResource:
        """Check migration name validity and availability.

        This method checks whether a proposed migration name is valid and available.

        :param subscription_id: The subscription ID of the target database server. Required.
        :type subscription_id: str
        :param resource_group_name: The resource group name of the target database server. Required.
        :type resource_group_name: str
        :param target_db_server_name: The name of the target database server. Required.
        :type target_db_server_name: str
        :param parameters: The required parameters for checking if a migration name is available.
         Required.
        :type parameters:
         ~azure.mgmt.rdbms.postgresql_flexibleservers.models.MigrationNameAvailabilityResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MigrationNameAvailabilityResource or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.postgresql_flexibleservers.models.MigrationNameAvailabilityResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_migration_name_availability(
        self,
        subscription_id: str,
        resource_group_name: str,
        target_db_server_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.MigrationNameAvailabilityResource:
        """Check migration name validity and availability.

        This method checks whether a proposed migration name is valid and available.

        :param subscription_id: The subscription ID of the target database server. Required.
        :type subscription_id: str
        :param resource_group_name: The resource group name of the target database server. Required.
        :type resource_group_name: str
        :param target_db_server_name: The name of the target database server. Required.
        :type target_db_server_name: str
        :param parameters: The required parameters for checking if a migration name is available.
         Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MigrationNameAvailabilityResource or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.postgresql_flexibleservers.models.MigrationNameAvailabilityResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_migration_name_availability(
        self,
        subscription_id: str,
        resource_group_name: str,
        target_db_server_name: str,
        parameters: Union[_models.MigrationNameAvailabilityResource, IO],
        **kwargs: Any
    ) -> _models.MigrationNameAvailabilityResource:
        """Check migration name validity and availability.

        This method checks whether a proposed migration name is valid and available.

        :param subscription_id: The subscription ID of the target database server. Required.
        :type subscription_id: str
        :param resource_group_name: The resource group name of the target database server. Required.
        :type resource_group_name: str
        :param target_db_server_name: The name of the target database server. Required.
        :type target_db_server_name: str
        :param parameters: The required parameters for checking if a migration name is available. Is
         either a MigrationNameAvailabilityResource type or a IO type. Required.
        :type parameters:
         ~azure.mgmt.rdbms.postgresql_flexibleservers.models.MigrationNameAvailabilityResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MigrationNameAvailabilityResource or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.postgresql_flexibleservers.models.MigrationNameAvailabilityResource
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
        cls: ClsType[_models.MigrationNameAvailabilityResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "MigrationNameAvailabilityResource")

        request = build_check_migration_name_availability_request(
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            target_db_server_name=target_db_server_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_migration_name_availability.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("MigrationNameAvailabilityResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_migration_name_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{targetDbServerName}/checkMigrationNameAvailability"
    }
