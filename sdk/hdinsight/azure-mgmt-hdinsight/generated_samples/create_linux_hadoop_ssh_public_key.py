# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.hdinsight import HDInsightManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hdinsight
# USAGE
    python create_linux_hadoop_ssh_public_key.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HDInsightManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.clusters.begin_create(
        resource_group_name="rg1",
        cluster_name="cluster1",
        parameters={
            "properties": {
                "clusterDefinition": {
                    "configurations": {
                        "gateway": {
                            "restAuthCredential.isEnabled": True,
                            "restAuthCredential.password": "**********",
                            "restAuthCredential.username": "admin",
                        }
                    },
                    "kind": "Hadoop",
                },
                "clusterVersion": "3.5",
                "computeProfile": {
                    "roles": [
                        {
                            "hardwareProfile": {"vmSize": "Standard_D3_V2"},
                            "minInstanceCount": 1,
                            "name": "headnode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {
                                    "sshProfile": {"publicKeys": [{"certificateData": "**********"}]},
                                    "username": "sshuser",
                                }
                            },
                            "targetInstanceCount": 2,
                        },
                        {
                            "hardwareProfile": {"vmSize": "Standard_D3_V2"},
                            "minInstanceCount": 1,
                            "name": "workernode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {"password": "**********", "username": "sshuser"}
                            },
                            "targetInstanceCount": 4,
                        },
                        {
                            "hardwareProfile": {"vmSize": "Small"},
                            "minInstanceCount": 1,
                            "name": "zookeepernode",
                            "osProfile": {
                                "linuxOperatingSystemProfile": {"password": "**********", "username": "sshuser"}
                            },
                            "targetInstanceCount": 3,
                        },
                    ]
                },
                "osType": "Linux",
                "storageProfile": {
                    "storageaccounts": [
                        {
                            "container": "containername",
                            "enableSecureChannel": True,
                            "isDefault": True,
                            "key": "storagekey",
                            "name": "mystorage.blob.core.windows.net",
                        }
                    ]
                },
                "tier": "Standard",
            },
            "tags": {"key1": "val1"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/hdinsight/resource-manager/Microsoft.HDInsight/preview/2023-04-15-preview/examples/CreateLinuxHadoopSshPublicKey.json
if __name__ == "__main__":
    main()
