# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import ManagedNetworkFabricMgmtClientConfiguration
from .operations import (
    AccessControlListsOperations,
    ExternalNetworksOperations,
    InternalNetworksOperations,
    InternetGatewayRulesOperations,
    InternetGatewaysOperations,
    IpCommunitiesOperations,
    IpExtendedCommunitiesOperations,
    IpPrefixesOperations,
    L2IsolationDomainsOperations,
    L3IsolationDomainsOperations,
    NeighborGroupsOperations,
    NetworkDeviceSkusOperations,
    NetworkDevicesOperations,
    NetworkFabricControllersOperations,
    NetworkFabricSkusOperations,
    NetworkFabricsOperations,
    NetworkInterfacesOperations,
    NetworkPacketBrokersOperations,
    NetworkRacksOperations,
    NetworkTapRulesOperations,
    NetworkTapsOperations,
    NetworkToNetworkInterconnectsOperations,
    Operations,
    RoutePoliciesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ManagedNetworkFabricMgmtClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Self service experience for Azure Network Fabric API.

    :ivar access_control_lists: AccessControlListsOperations operations
    :vartype access_control_lists:
     azure.mgmt.managednetworkfabric.aio.operations.AccessControlListsOperations
    :ivar internet_gateways: InternetGatewaysOperations operations
    :vartype internet_gateways:
     azure.mgmt.managednetworkfabric.aio.operations.InternetGatewaysOperations
    :ivar internet_gateway_rules: InternetGatewayRulesOperations operations
    :vartype internet_gateway_rules:
     azure.mgmt.managednetworkfabric.aio.operations.InternetGatewayRulesOperations
    :ivar ip_communities: IpCommunitiesOperations operations
    :vartype ip_communities: azure.mgmt.managednetworkfabric.aio.operations.IpCommunitiesOperations
    :ivar ip_extended_communities: IpExtendedCommunitiesOperations operations
    :vartype ip_extended_communities:
     azure.mgmt.managednetworkfabric.aio.operations.IpExtendedCommunitiesOperations
    :ivar ip_prefixes: IpPrefixesOperations operations
    :vartype ip_prefixes: azure.mgmt.managednetworkfabric.aio.operations.IpPrefixesOperations
    :ivar l2_isolation_domains: L2IsolationDomainsOperations operations
    :vartype l2_isolation_domains:
     azure.mgmt.managednetworkfabric.aio.operations.L2IsolationDomainsOperations
    :ivar l3_isolation_domains: L3IsolationDomainsOperations operations
    :vartype l3_isolation_domains:
     azure.mgmt.managednetworkfabric.aio.operations.L3IsolationDomainsOperations
    :ivar internal_networks: InternalNetworksOperations operations
    :vartype internal_networks:
     azure.mgmt.managednetworkfabric.aio.operations.InternalNetworksOperations
    :ivar external_networks: ExternalNetworksOperations operations
    :vartype external_networks:
     azure.mgmt.managednetworkfabric.aio.operations.ExternalNetworksOperations
    :ivar neighbor_groups: NeighborGroupsOperations operations
    :vartype neighbor_groups:
     azure.mgmt.managednetworkfabric.aio.operations.NeighborGroupsOperations
    :ivar network_device_skus: NetworkDeviceSkusOperations operations
    :vartype network_device_skus:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkDeviceSkusOperations
    :ivar network_devices: NetworkDevicesOperations operations
    :vartype network_devices:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkDevicesOperations
    :ivar network_interfaces: NetworkInterfacesOperations operations
    :vartype network_interfaces:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkInterfacesOperations
    :ivar network_fabric_controllers: NetworkFabricControllersOperations operations
    :vartype network_fabric_controllers:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkFabricControllersOperations
    :ivar network_fabric_skus: NetworkFabricSkusOperations operations
    :vartype network_fabric_skus:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkFabricSkusOperations
    :ivar network_fabrics: NetworkFabricsOperations operations
    :vartype network_fabrics:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkFabricsOperations
    :ivar network_to_network_interconnects: NetworkToNetworkInterconnectsOperations operations
    :vartype network_to_network_interconnects:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkToNetworkInterconnectsOperations
    :ivar network_packet_brokers: NetworkPacketBrokersOperations operations
    :vartype network_packet_brokers:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkPacketBrokersOperations
    :ivar network_racks: NetworkRacksOperations operations
    :vartype network_racks: azure.mgmt.managednetworkfabric.aio.operations.NetworkRacksOperations
    :ivar network_tap_rules: NetworkTapRulesOperations operations
    :vartype network_tap_rules:
     azure.mgmt.managednetworkfabric.aio.operations.NetworkTapRulesOperations
    :ivar network_taps: NetworkTapsOperations operations
    :vartype network_taps: azure.mgmt.managednetworkfabric.aio.operations.NetworkTapsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.managednetworkfabric.aio.operations.Operations
    :ivar route_policies: RoutePoliciesOperations operations
    :vartype route_policies: azure.mgmt.managednetworkfabric.aio.operations.RoutePoliciesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-06-15". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ManagedNetworkFabricMgmtClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.access_control_lists = AccessControlListsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.internet_gateways = InternetGatewaysOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.internet_gateway_rules = InternetGatewayRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.ip_communities = IpCommunitiesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.ip_extended_communities = IpExtendedCommunitiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.ip_prefixes = IpPrefixesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.l2_isolation_domains = L2IsolationDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.l3_isolation_domains = L3IsolationDomainsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.internal_networks = InternalNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.external_networks = ExternalNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.neighbor_groups = NeighborGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_device_skus = NetworkDeviceSkusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_devices = NetworkDevicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_interfaces = NetworkInterfacesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_fabric_controllers = NetworkFabricControllersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_fabric_skus = NetworkFabricSkusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_fabrics = NetworkFabricsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_to_network_interconnects = NetworkToNetworkInterconnectsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_packet_brokers = NetworkPacketBrokersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_racks = NetworkRacksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_tap_rules = NetworkTapRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_taps = NetworkTapsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.route_policies = RoutePoliciesOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ManagedNetworkFabricMgmtClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
