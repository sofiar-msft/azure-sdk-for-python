# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Optional, TYPE_CHECKING, Union

from azure.communication.phonenumbers._generated import models
from azure.communication.phonenumbers._generated import _serialization

class PurchasedPhoneNumber(_serialization.Model):  # pylint: disable=too-many-instance-attributes
    """Represents a purchased phone number.

    All required parameters must be populated in order to send to server.

    :ivar id: The id of the phone number, e.g. 11234567890. Required.
    :vartype id: str
    :ivar phone_number: String of the E.164 format of the phone number, e.g. +11234567890.
     Required.
    :vartype phone_number: str
    :ivar country_code: The ISO 3166-2 code of the phone number's country, e.g. US. Required.
    :vartype country_code: str
    :ivar phone_number_type: The phone number's type, e.g. geographic, tollFree. Required. Known
     values are: "geographic" and "tollFree".
    :vartype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
    :ivar capabilities: Capabilities of a phone number. Required.
    :vartype capabilities:
     ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
    :ivar assignment_type: The assignment type of the phone number. A phone number can be assigned
     to a person, or to an application. Required. Known values are: "person" and "application".
    :vartype assignment_type: str or
     ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
    :ivar purchase_date: The date and time that the phone number was purchased. Required.
    :vartype purchase_date: ~datetime.datetime
    :ivar cost: The incurred cost for a single phone number. Required.
    :vartype cost: ~azure.communication.phonenumbers.models.PhoneNumberCost
    :ivar operator_id: Id of the operator that provided the number.
    :vartype operator_id: str
    :ivar operator_name: Name of the operator that provided the number.
    :vartype operator_name: str
    :ivar phone_number_source: Source of the number, e.g. Cloud or OperatorConnect. Known values
     are: "cloud" and "operatorConnect".
    :vartype phone_number_source: str or ~azure.communication.phonenumbers.models.PhoneNumberSource
    """

    _validation = {
        "id": {"required": True},
        "phone_number": {"required": True},
        "country_code": {"required": True},
        "phone_number_type": {"required": True},
        "capabilities": {"required": True},
        "assignment_type": {"required": True},
        "purchase_date": {"required": True},
        "cost": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "phone_number": {"key": "phoneNumber", "type": "str"},
        "country_code": {"key": "countryCode", "type": "str"},
        "phone_number_type": {"key": "phoneNumberType", "type": "str"},
        "capabilities": {"key": "capabilities", "type": "PhoneNumberCapabilities"},
        "assignment_type": {"key": "assignmentType", "type": "str"},
        "purchase_date": {"key": "purchaseDate", "type": "iso-8601"},
        "cost": {"key": "cost", "type": "PhoneNumberCost"},
        "operator_id": {"key": "operatorId", "type": "str"},
        "operator_name": {"key": "operatorName", "type": "str"},
        "phone_number_source": {"key": "phoneNumberSource", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        phone_number: str,
        country_code: str,
        phone_number_type: Union[str, "models.PhoneNumberType"],
        capabilities: "PhoneNumberCapabilities",
        assignment_type: Union[str, "models.PhoneNumberAssignmentType"],
        purchase_date: datetime.datetime,
        cost: "models.PhoneNumberCost",
        operator_id: Optional[str] = None,
        operator_name: Optional[str] = None,
        phone_number_source: Optional[Union[str, "models.PhoneNumberSource"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: The id of the phone number, e.g. 11234567890. Required.
        :paramtype id: str
        :keyword phone_number: String of the E.164 format of the phone number, e.g. +11234567890.
         Required.
        :paramtype phone_number: str
        :keyword country_code: The ISO 3166-2 code of the phone number's country, e.g. US. Required.
        :paramtype country_code: str
        :keyword phone_number_type: The phone number's type, e.g. geographic, tollFree. Required. Known
         values are: "geographic" and "tollFree".
        :paramtype phone_number_type: str or ~azure.communication.phonenumbers.models.PhoneNumberType
        :keyword capabilities: Capabilities of a phone number. Required.
        :paramtype capabilities:
         ~azure.communication.phonenumbers.models.PhoneNumberCapabilities
        :keyword assignment_type: The assignment type of the phone number. A phone number can be
         assigned to a person, or to an application. Required. Known values are: "person" and
         "application".
        :paramtype assignment_type: str or
         ~azure.communication.phonenumbers.models.PhoneNumberAssignmentType
        :keyword purchase_date: The date and time that the phone number was purchased. Required.
        :paramtype purchase_date: ~datetime.datetime
        :keyword cost: The incurred cost for a single phone number. Required.
        :paramtype cost: ~azure.communication.phonenumbers.models.PhoneNumberCost
        :keyword operator_id: Id of the operator that provided the number.
        :paramtype operator_id: str
        :keyword operator_name: Name of the operator that provided the number.
        :paramtype operator_name: str
        :keyword phone_number_source: Source of the number, e.g. Cloud or OperatorConnect. Known values
         are: "cloud" and "operatorConnect".
        :paramtype phone_number_source: str or
         ~azure.communication.phonenumbers.models.PhoneNumberSource
        """
        super().__init__(**kwargs)
        self.id = id
        self.phone_number = phone_number
        self.country_code = country_code
        self.phone_number_type = phone_number_type
        self.capabilities = capabilities
        self.assignment_type = assignment_type
        self.purchase_date = purchase_date
        self.cost = cost
        self.operator_id = operator_id
        self.operator_name = operator_name
        self.phone_number_source = phone_number_source


class PhoneNumberCapabilities(_serialization.Model):
    """Capabilities of a phone number.

    All required parameters must be populated in order to send to server.

    :ivar calling: Capability value for calling. Required. Known values are: "none", "inbound",
     "outbound", and "inbound+outbound".
    :vartype calling: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
    :ivar sms: Capability value for SMS. Required. Known values are: "none", "inbound", "outbound",
     and "inbound+outbound".
    :vartype sms: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
    :ivar ten_dlc_campaign_brief_id: Ten DLC campaign brief id attached to the number.
    :vartype ten_dlc_campaign_brief_id: str
    """

    _validation = {
        "calling": {"required": True},
        "sms": {"required": True},
    }

    _attribute_map = {
        "calling": {"key": "calling", "type": "str"},
        "sms": {"key": "sms", "type": "str"},
        "ten_dlc_campaign_brief_id": {"key": "tenDLCCampaignBriefId", "type": "str"},
    }

    def __init__(
        self,
        *,
        calling: Union[str, "models.PhoneNumberCapabilityType"],
        sms: Union[str, "models.PhoneNumberCapabilityType"],
        ten_dlc_campaign_brief_id: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword calling: Capability value for calling. Required. Known values are: "none", "inbound",
         "outbound", and "inbound+outbound".
        :paramtype calling: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
        :keyword sms: Capability value for SMS. Required. Known values are: "none", "inbound",
         "outbound", and "inbound+outbound".
        :paramtype sms: str or ~azure.communication.phonenumbers.models.PhoneNumberCapabilityType
        :keyword ten_dlc_campaign_brief_id: Ten DLC campaign brief id attached to the number.
        :paramtype ten_dlc_campaign_brief_id: str
        """
        super().__init__(**kwargs)
        self.calling = calling
        self.sms = sms
        self.ten_dlc_campaign_brief_id = ten_dlc_campaign_brief_id