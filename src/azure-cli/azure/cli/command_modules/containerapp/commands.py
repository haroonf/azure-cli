# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azure.cli.command_modules.containerapp._client_factory import cf_containerapp


def load_command_table(self, _):

    containerapp_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.appcontainers.operations#ContainerAppsOperations.{}',
        client_factory=cf_containerapp)


    with self.command_group('containerapp', containerapp_sdk, client_factory=cf_containerapp) as g:
        g.custom_command('create', 'create_containerapp')
        g.command('delete', 'delete')
        g.custom_command('list', 'list_containerapp')
        g.show_command('show', 'get')
        g.generic_update_command('update', setter_name='update', custom_func_name='update_containerapp')


