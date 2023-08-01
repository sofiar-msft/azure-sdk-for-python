# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.apimanagement import ApiManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apimanagement
# USAGE
    python api_management_create_backend_service_fabric.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApiManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.backend.create_or_update(
        resource_group_name="rg1",
        service_name="apimService1",
        backend_id="sfbackend",
        parameters={
            "properties": {
                "description": "Service Fabric Test App 1",
                "properties": {
                    "serviceFabricCluster": {
                        "clientCertificateId": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.ApiManagement/service/apimService1/certificates/cert1",
                        "managementEndpoints": ["https://somecluster.com"],
                        "maxPartitionResolutionRetries": 5,
                        "serverX509Names": [
                            {"issuerCertificateThumbprint": "IssuerCertificateThumbprint1", "name": "ServerCommonName1"}
                        ],
                    }
                },
                "protocol": "http",
                "url": "fabric:/mytestapp/mytestservice",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/apimanagement/resource-manager/Microsoft.ApiManagement/stable/2022-08-01/examples/ApiManagementCreateBackendServiceFabric.json
if __name__ == "__main__":
    main()
