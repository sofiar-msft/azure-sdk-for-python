# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class CatalogSyncState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The synchronization state of the catalog."""

    SUCCEEDED = "Succeeded"
    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    CANCELED = "Canceled"


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason why the given name is not available."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DomainJoinType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Active Directory join type."""

    HYBRID_AZURE_AD_JOIN = "HybridAzureADJoin"
    AZURE_AD_JOIN = "AzureADJoin"


class EnvironmentTypeEnableStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the environment type is either enabled or disabled."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class HealthCheckStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health check status values."""

    UNKNOWN = "Unknown"
    PENDING = "Pending"
    RUNNING = "Running"
    PASSED = "Passed"
    WARNING = "Warning"
    FAILED = "Failed"


class HealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health status indicating whether a pool is available to create Dev Boxes."""

    UNKNOWN = "Unknown"
    PENDING = "Pending"
    HEALTHY = "Healthy"
    WARNING = "Warning"
    UNHEALTHY = "Unhealthy"


class HibernateSupport(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether hibernate is enabled/disabled."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ImageValidationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Image validation status."""

    UNKNOWN = "Unknown"
    PENDING = "Pending"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    TIMED_OUT = "TimedOut"


class LicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """License Types."""

    WINDOWS_CLIENT = "Windows_Client"


class LocalAdminStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LocalAdminStatus."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    CREATING = "Creating"
    CREATED = "Created"
    UPDATING = "Updating"
    UPDATED = "Updated"
    DELETING = "Deleting"
    DELETED = "Deleted"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    MOVING_RESOURCES = "MovingResources"
    TRANSIENT_FAILURE = "TransientFailure"
    ROLLOUT_IN_PROGRESS = "RolloutInProgress"
    STORAGE_PROVISIONING_FAILED = "StorageProvisioningFailed"


class ScheduledFrequency(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The frequency of task execution."""

    DAILY = "Daily"


class ScheduledType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The supported types for a scheduled task."""

    STOP_DEV_BOX = "StopDevBox"


class ScheduleEnableStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Schedule enable or disable status. Indicates whether the schedule applied to is either enabled
    or disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class StopOnDisconnectEnableStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Stop on disconnect enable or disable status. Indicates whether stop on disconnect to is either
    enabled or disabled.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class UsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The unit details."""

    COUNT = "Count"
