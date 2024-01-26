# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.appplatform import AppPlatformManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appplatform
# USAGE
    python api_portal_custom_domains_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AppPlatformManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.api_portal_custom_domains.begin_create_or_update(
        resource_group_name="myResourceGroup",
        service_name="myservice",
        api_portal_name="default",
        domain_name="myDomainName",
        api_portal_custom_domain_resource={"properties": {"thumbprint": "*"}},
    ).result()
    print(response)


# x-ms-original-file: specification/appplatform/resource-manager/Microsoft.AppPlatform/stable/2023-12-01/examples/ApiPortalCustomDomains_CreateOrUpdate.json
if __name__ == "__main__":
    main()
