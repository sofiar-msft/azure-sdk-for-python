# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.cdn import CdnManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-cdn
# USAGE
    python routes_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CdnManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.routes.begin_update(
        resource_group_name="RG",
        profile_name="profile1",
        endpoint_name="endpoint1",
        route_name="route1",
        route_update_properties={
            "properties": {
                "cacheConfiguration": {
                    "compressionSettings": {
                        "contentTypesToCompress": ["text/html", "application/octet-stream"],
                        "isCompressionEnabled": True,
                    },
                    "queryStringCachingBehavior": "IgnoreQueryString",
                },
                "customDomains": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/RG/providers/Microsoft.Cdn/profiles/profile1/customDomains/domain1"
                    }
                ],
                "enabledState": "Enabled",
                "forwardingProtocol": "MatchRequest",
                "httpsRedirect": "Enabled",
                "linkToDefaultDomain": "Enabled",
                "originGroup": {
                    "id": "/subscriptions/subid/resourceGroups/RG/providers/Microsoft.Cdn/profiles/profile1/originGroups/originGroup1"
                },
                "originPath": None,
                "patternsToMatch": ["/*"],
                "ruleSets": [
                    {
                        "id": "/subscriptions/subid/resourceGroups/RG/providers/Microsoft.Cdn/profiles/profile1/ruleSets/ruleSet1"
                    }
                ],
                "supportedProtocols": ["Https", "Http"],
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/cdn/resource-manager/Microsoft.Cdn/stable/2024-02-01/examples/Routes_Update.json
if __name__ == "__main__":
    main()
