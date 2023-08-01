# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.costmanagement import CostManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-costmanagement
# USAGE
    python dismiss_resource_group_alerts.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = CostManagementClient(
        credential=DefaultAzureCredential(),
    )

    response = client.alerts.dismiss(
        scope="subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/ScreenSharingTest-peer",
        alert_id="22222222-2222-2222-2222-222222222222",
        parameters={"properties": {"status": "Dismissed"}},
    )
    print(response)


# x-ms-original-file: specification/cost-management/resource-manager/Microsoft.CostManagement/stable/2022-10-01/examples/DismissResourceGroupAlerts.json
if __name__ == "__main__":
    main()
