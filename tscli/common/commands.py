# Copyright 2017, 2018 Red Hat, Inc.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import click
from tscli.restapi import ConsumeAPIs
from tscli.textoutput import TextOutputAPIs


@click.command()
@click.option(
    '--server-url', envvar='TRANSTATS_SERVER', help="Transtats Server URL"
)
@click.option("--server", is_flag=True, help="Server version.")
@click.option(
    '--json', is_flag=True, envvar='JSON_OUTPUT', help="Print in JSON format")
@click.pass_obj
def version(app_context, server_url, server, json):
    """Display the current version."""
    if json:
        version_dict = {"client": "Transtats client %s" % app_context.version}
        if server:
            response = ConsumeAPIs(server_url or app_context.server_url).server_version
            if isinstance(response, dict):
                version_dict.update(response)
        app_context.print_r(version_dict)
    else:
        print("Transtats client : {0}".format(app_context.version))
        if server:
            TextOutputAPIs(
                server_url or app_context.server_url
            ).server_version
