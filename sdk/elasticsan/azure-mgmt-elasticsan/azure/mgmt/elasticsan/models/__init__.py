# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ElasticSan
from ._models_py3 import ElasticSanList
from ._models_py3 import ElasticSanProperties
from ._models_py3 import ElasticSanUpdate
from ._models_py3 import ElasticSanUpdateProperties
from ._models_py3 import EncryptionIdentity
from ._models_py3 import EncryptionProperties
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Identity
from ._models_py3 import IscsiTargetInfo
from ._models_py3 import KeyVaultProperties
from ._models_py3 import ManagedByInfo
from ._models_py3 import NetworkRuleSet
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionProperties
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkResourceProperties
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import SKUCapability
from ._models_py3 import Sku
from ._models_py3 import SkuInformation
from ._models_py3 import SkuInformationList
from ._models_py3 import SkuLocationInfo
from ._models_py3 import Snapshot
from ._models_py3 import SnapshotCreationData
from ._models_py3 import SnapshotList
from ._models_py3 import SnapshotProperties
from ._models_py3 import SourceCreationData
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import VirtualNetworkRule
from ._models_py3 import Volume
from ._models_py3 import VolumeGroup
from ._models_py3 import VolumeGroupList
from ._models_py3 import VolumeGroupProperties
from ._models_py3 import VolumeGroupUpdate
from ._models_py3 import VolumeGroupUpdateProperties
from ._models_py3 import VolumeList
from ._models_py3 import VolumeProperties
from ._models_py3 import VolumeUpdate
from ._models_py3 import VolumeUpdateProperties

from ._elastic_san_mgmt_client_enums import Action
from ._elastic_san_mgmt_client_enums import ActionType
from ._elastic_san_mgmt_client_enums import CreatedByType
from ._elastic_san_mgmt_client_enums import EncryptionType
from ._elastic_san_mgmt_client_enums import IdentityType
from ._elastic_san_mgmt_client_enums import OperationalStatus
from ._elastic_san_mgmt_client_enums import Origin
from ._elastic_san_mgmt_client_enums import PrivateEndpointServiceConnectionStatus
from ._elastic_san_mgmt_client_enums import ProvisioningStates
from ._elastic_san_mgmt_client_enums import PublicNetworkAccess
from ._elastic_san_mgmt_client_enums import SkuName
from ._elastic_san_mgmt_client_enums import SkuTier
from ._elastic_san_mgmt_client_enums import StorageTargetType
from ._elastic_san_mgmt_client_enums import VolumeCreateOption
from ._elastic_san_mgmt_client_enums import XMsDeleteSnapshots
from ._elastic_san_mgmt_client_enums import XMsForceDelete
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ElasticSan",
    "ElasticSanList",
    "ElasticSanProperties",
    "ElasticSanUpdate",
    "ElasticSanUpdateProperties",
    "EncryptionIdentity",
    "EncryptionProperties",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Identity",
    "IscsiTargetInfo",
    "KeyVaultProperties",
    "ManagedByInfo",
    "NetworkRuleSet",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointConnectionProperties",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkResourceProperties",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "Resource",
    "SKUCapability",
    "Sku",
    "SkuInformation",
    "SkuInformationList",
    "SkuLocationInfo",
    "Snapshot",
    "SnapshotCreationData",
    "SnapshotList",
    "SnapshotProperties",
    "SourceCreationData",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "VirtualNetworkRule",
    "Volume",
    "VolumeGroup",
    "VolumeGroupList",
    "VolumeGroupProperties",
    "VolumeGroupUpdate",
    "VolumeGroupUpdateProperties",
    "VolumeList",
    "VolumeProperties",
    "VolumeUpdate",
    "VolumeUpdateProperties",
    "Action",
    "ActionType",
    "CreatedByType",
    "EncryptionType",
    "IdentityType",
    "OperationalStatus",
    "Origin",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningStates",
    "PublicNetworkAccess",
    "SkuName",
    "SkuTier",
    "StorageTargetType",
    "VolumeCreateOption",
    "XMsDeleteSnapshots",
    "XMsForceDelete",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
