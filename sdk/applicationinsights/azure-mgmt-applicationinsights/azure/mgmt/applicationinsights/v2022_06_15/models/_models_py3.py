# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class HeaderField(_serialization.Model):
    """A header to add to the WebTest.

    :ivar header_field_name: The name of the header.
    :vartype header_field_name: str
    :ivar header_field_value: The value of the header.
    :vartype header_field_value: str
    """

    _attribute_map = {
        "header_field_name": {"key": "key", "type": "str"},
        "header_field_value": {"key": "value", "type": "str"},
    }

    def __init__(
        self, *, header_field_name: Optional[str] = None, header_field_value: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword header_field_name: The name of the header.
        :paramtype header_field_name: str
        :keyword header_field_value: The value of the header.
        :paramtype header_field_value: str
        """
        super().__init__(**kwargs)
        self.header_field_name = header_field_name
        self.header_field_value = header_field_value


class TagsResource(_serialization.Model):
    """A container holding only the Tags for a resource, allowing the user to update the tags on a
    WebTest instance.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.tags = tags


class WebtestsResource(_serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class WebTest(WebtestsResource):  # pylint: disable=too-many-instance-attributes
    """An Application Insights WebTest definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar kind: The kind of WebTest that this web test watches. Choices are ping, multistep and
     standard. Known values are: "ping", "multistep", and "standard".
    :vartype kind: str or ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestKind
    :ivar synthetic_monitor_id: Unique ID of this WebTest. This is typically the same value as the
     Name field.
    :vartype synthetic_monitor_id: str
    :ivar web_test_name: User defined name if this WebTest.
    :vartype web_test_name: str
    :ivar description: User defined description for this WebTest.
    :vartype description: str
    :ivar enabled: Is the test actively being monitored.
    :vartype enabled: bool
    :ivar frequency: Interval in seconds between test runs for this WebTest. Default value is 300.
    :vartype frequency: int
    :ivar timeout: Seconds until this WebTest will timeout and fail. Default value is 30.
    :vartype timeout: int
    :ivar web_test_kind: The kind of web test this is, valid choices are ping, multistep and
     standard. Known values are: "ping", "multistep", and "standard".
    :vartype web_test_kind: str or ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestKind
    :ivar retry_enabled: Allow for retries should this WebTest fail.
    :vartype retry_enabled: bool
    :ivar locations: A list of where to physically run the tests from to give global coverage for
     accessibility of your application.
    :vartype locations: list[~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestGeolocation]
    :ivar configuration: An XML configuration specification for a WebTest.
    :vartype configuration:
     ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesConfiguration
    :ivar provisioning_state: Current state of this component, whether or not is has been
     provisioned within the resource group it is defined. Users cannot change this value but are
     able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed.
    :vartype provisioning_state: str
    :ivar request: The collection of request properties.
    :vartype request: ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesRequest
    :ivar validation_rules: The collection of validation rule properties.
    :vartype validation_rules:
     ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesValidationRules
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "kind": {"key": "kind", "type": "str"},
        "synthetic_monitor_id": {"key": "properties.SyntheticMonitorId", "type": "str"},
        "web_test_name": {"key": "properties.Name", "type": "str"},
        "description": {"key": "properties.Description", "type": "str"},
        "enabled": {"key": "properties.Enabled", "type": "bool"},
        "frequency": {"key": "properties.Frequency", "type": "int"},
        "timeout": {"key": "properties.Timeout", "type": "int"},
        "web_test_kind": {"key": "properties.Kind", "type": "str"},
        "retry_enabled": {"key": "properties.RetryEnabled", "type": "bool"},
        "locations": {"key": "properties.Locations", "type": "[WebTestGeolocation]"},
        "configuration": {"key": "properties.Configuration", "type": "WebTestPropertiesConfiguration"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "request": {"key": "properties.Request", "type": "WebTestPropertiesRequest"},
        "validation_rules": {"key": "properties.ValidationRules", "type": "WebTestPropertiesValidationRules"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        kind: Optional[Union[str, "_models.WebTestKind"]] = None,
        synthetic_monitor_id: Optional[str] = None,
        web_test_name: Optional[str] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        frequency: int = 300,
        timeout: int = 30,
        web_test_kind: Optional[Union[str, "_models.WebTestKind"]] = None,
        retry_enabled: Optional[bool] = None,
        locations: Optional[List["_models.WebTestGeolocation"]] = None,
        configuration: Optional["_models.WebTestPropertiesConfiguration"] = None,
        request: Optional["_models.WebTestPropertiesRequest"] = None,
        validation_rules: Optional["_models.WebTestPropertiesValidationRules"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword kind: The kind of WebTest that this web test watches. Choices are ping, multistep and
         standard. Known values are: "ping", "multistep", and "standard".
        :paramtype kind: str or ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestKind
        :keyword synthetic_monitor_id: Unique ID of this WebTest. This is typically the same value as
         the Name field.
        :paramtype synthetic_monitor_id: str
        :keyword web_test_name: User defined name if this WebTest.
        :paramtype web_test_name: str
        :keyword description: User defined description for this WebTest.
        :paramtype description: str
        :keyword enabled: Is the test actively being monitored.
        :paramtype enabled: bool
        :keyword frequency: Interval in seconds between test runs for this WebTest. Default value is
         300.
        :paramtype frequency: int
        :keyword timeout: Seconds until this WebTest will timeout and fail. Default value is 30.
        :paramtype timeout: int
        :keyword web_test_kind: The kind of web test this is, valid choices are ping, multistep and
         standard. Known values are: "ping", "multistep", and "standard".
        :paramtype web_test_kind: str or ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestKind
        :keyword retry_enabled: Allow for retries should this WebTest fail.
        :paramtype retry_enabled: bool
        :keyword locations: A list of where to physically run the tests from to give global coverage
         for accessibility of your application.
        :paramtype locations:
         list[~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestGeolocation]
        :keyword configuration: An XML configuration specification for a WebTest.
        :paramtype configuration:
         ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesConfiguration
        :keyword request: The collection of request properties.
        :paramtype request: ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesRequest
        :keyword validation_rules: The collection of validation rule properties.
        :paramtype validation_rules:
         ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesValidationRules
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.kind = kind
        self.synthetic_monitor_id = synthetic_monitor_id
        self.web_test_name = web_test_name
        self.description = description
        self.enabled = enabled
        self.frequency = frequency
        self.timeout = timeout
        self.web_test_kind = web_test_kind
        self.retry_enabled = retry_enabled
        self.locations = locations
        self.configuration = configuration
        self.provisioning_state = None
        self.request = request
        self.validation_rules = validation_rules


class WebTestGeolocation(_serialization.Model):
    """Geo-physical location to run a WebTest from. You must specify one or more locations for the
    test to run from.

    :ivar location: Location ID for the WebTest to run from.
    :vartype location: str
    """

    _attribute_map = {
        "location": {"key": "Id", "type": "str"},
    }

    def __init__(self, *, location: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword location: Location ID for the WebTest to run from.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.location = location


class WebTestListResult(_serialization.Model):
    """A list of 0 or more Application Insights WebTest definitions.

    All required parameters must be populated in order to send to Azure.

    :ivar value: Set of Application Insights WebTest definitions. Required.
    :vartype value: list[~azure.mgmt.applicationinsights.v2022_06_15.models.WebTest]
    :ivar next_link: The link to get the next part of the returned list of WebTest, should the
     return set be too large for a single request. May be null.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[WebTest]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: List["_models.WebTest"], next_link: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value: Set of Application Insights WebTest definitions. Required.
        :paramtype value: list[~azure.mgmt.applicationinsights.v2022_06_15.models.WebTest]
        :keyword next_link: The link to get the next part of the returned list of WebTest, should the
         return set be too large for a single request. May be null.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class WebTestPropertiesConfiguration(_serialization.Model):
    """An XML configuration specification for a WebTest.

    :ivar web_test: The XML specification of a WebTest to run against an application.
    :vartype web_test: str
    """

    _attribute_map = {
        "web_test": {"key": "WebTest", "type": "str"},
    }

    def __init__(self, *, web_test: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword web_test: The XML specification of a WebTest to run against an application.
        :paramtype web_test: str
        """
        super().__init__(**kwargs)
        self.web_test = web_test


class WebTestPropertiesRequest(_serialization.Model):
    """The collection of request properties.

    :ivar request_url: Url location to test.
    :vartype request_url: str
    :ivar headers: List of headers and their values to add to the WebTest call.
    :vartype headers: list[~azure.mgmt.applicationinsights.v2022_06_15.models.HeaderField]
    :ivar http_verb: Http verb to use for this web test.
    :vartype http_verb: str
    :ivar request_body: Base64 encoded string body to send with this web test.
    :vartype request_body: str
    :ivar parse_dependent_requests: Parse Dependent request for this WebTest.
    :vartype parse_dependent_requests: bool
    :ivar follow_redirects: Follow redirects for this web test.
    :vartype follow_redirects: bool
    """

    _attribute_map = {
        "request_url": {"key": "RequestUrl", "type": "str"},
        "headers": {"key": "Headers", "type": "[HeaderField]"},
        "http_verb": {"key": "HttpVerb", "type": "str"},
        "request_body": {"key": "RequestBody", "type": "str"},
        "parse_dependent_requests": {"key": "ParseDependentRequests", "type": "bool"},
        "follow_redirects": {"key": "FollowRedirects", "type": "bool"},
    }

    def __init__(
        self,
        *,
        request_url: Optional[str] = None,
        headers: Optional[List["_models.HeaderField"]] = None,
        http_verb: Optional[str] = None,
        request_body: Optional[str] = None,
        parse_dependent_requests: Optional[bool] = None,
        follow_redirects: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword request_url: Url location to test.
        :paramtype request_url: str
        :keyword headers: List of headers and their values to add to the WebTest call.
        :paramtype headers: list[~azure.mgmt.applicationinsights.v2022_06_15.models.HeaderField]
        :keyword http_verb: Http verb to use for this web test.
        :paramtype http_verb: str
        :keyword request_body: Base64 encoded string body to send with this web test.
        :paramtype request_body: str
        :keyword parse_dependent_requests: Parse Dependent request for this WebTest.
        :paramtype parse_dependent_requests: bool
        :keyword follow_redirects: Follow redirects for this web test.
        :paramtype follow_redirects: bool
        """
        super().__init__(**kwargs)
        self.request_url = request_url
        self.headers = headers
        self.http_verb = http_verb
        self.request_body = request_body
        self.parse_dependent_requests = parse_dependent_requests
        self.follow_redirects = follow_redirects


class WebTestPropertiesValidationRules(_serialization.Model):
    """The collection of validation rule properties.

    :ivar content_validation: The collection of content validation properties.
    :vartype content_validation:
     ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesValidationRulesContentValidation
    :ivar ssl_check: Checks to see if the SSL cert is still valid.
    :vartype ssl_check: bool
    :ivar ssl_cert_remaining_lifetime_check: A number of days to check still remain before the the
     existing SSL cert expires.  Value must be positive and the SSLCheck must be set to true.
    :vartype ssl_cert_remaining_lifetime_check: int
    :ivar expected_http_status_code: Validate that the WebTest returns the http status code
     provided.
    :vartype expected_http_status_code: int
    :ivar ignore_http_status_code: When set, validation will ignore the status code.
    :vartype ignore_http_status_code: bool
    """

    _attribute_map = {
        "content_validation": {"key": "ContentValidation", "type": "WebTestPropertiesValidationRulesContentValidation"},
        "ssl_check": {"key": "SSLCheck", "type": "bool"},
        "ssl_cert_remaining_lifetime_check": {"key": "SSLCertRemainingLifetimeCheck", "type": "int"},
        "expected_http_status_code": {"key": "ExpectedHttpStatusCode", "type": "int"},
        "ignore_http_status_code": {"key": "IgnoreHttpStatusCode", "type": "bool"},
    }

    def __init__(
        self,
        *,
        content_validation: Optional["_models.WebTestPropertiesValidationRulesContentValidation"] = None,
        ssl_check: Optional[bool] = None,
        ssl_cert_remaining_lifetime_check: Optional[int] = None,
        expected_http_status_code: Optional[int] = None,
        ignore_http_status_code: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword content_validation: The collection of content validation properties.
        :paramtype content_validation:
         ~azure.mgmt.applicationinsights.v2022_06_15.models.WebTestPropertiesValidationRulesContentValidation
        :keyword ssl_check: Checks to see if the SSL cert is still valid.
        :paramtype ssl_check: bool
        :keyword ssl_cert_remaining_lifetime_check: A number of days to check still remain before the
         the existing SSL cert expires.  Value must be positive and the SSLCheck must be set to true.
        :paramtype ssl_cert_remaining_lifetime_check: int
        :keyword expected_http_status_code: Validate that the WebTest returns the http status code
         provided.
        :paramtype expected_http_status_code: int
        :keyword ignore_http_status_code: When set, validation will ignore the status code.
        :paramtype ignore_http_status_code: bool
        """
        super().__init__(**kwargs)
        self.content_validation = content_validation
        self.ssl_check = ssl_check
        self.ssl_cert_remaining_lifetime_check = ssl_cert_remaining_lifetime_check
        self.expected_http_status_code = expected_http_status_code
        self.ignore_http_status_code = ignore_http_status_code


class WebTestPropertiesValidationRulesContentValidation(_serialization.Model):
    """The collection of content validation properties.

    :ivar content_match: Content to look for in the return of the WebTest.  Must not be null or
     empty.
    :vartype content_match: str
    :ivar ignore_case: When set, this value makes the ContentMatch validation case insensitive.
    :vartype ignore_case: bool
    :ivar pass_if_text_found: When true, validation will pass if there is a match for the
     ContentMatch string.  If false, validation will fail if there is a match.
    :vartype pass_if_text_found: bool
    """

    _attribute_map = {
        "content_match": {"key": "ContentMatch", "type": "str"},
        "ignore_case": {"key": "IgnoreCase", "type": "bool"},
        "pass_if_text_found": {"key": "PassIfTextFound", "type": "bool"},
    }

    def __init__(
        self,
        *,
        content_match: Optional[str] = None,
        ignore_case: Optional[bool] = None,
        pass_if_text_found: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword content_match: Content to look for in the return of the WebTest.  Must not be null or
         empty.
        :paramtype content_match: str
        :keyword ignore_case: When set, this value makes the ContentMatch validation case insensitive.
        :paramtype ignore_case: bool
        :keyword pass_if_text_found: When true, validation will pass if there is a match for the
         ContentMatch string.  If false, validation will fail if there is a match.
        :paramtype pass_if_text_found: bool
        """
        super().__init__(**kwargs)
        self.content_match = content_match
        self.ignore_case = ignore_case
        self.pass_if_text_found = pass_if_text_found
