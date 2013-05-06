#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2013 Rackspace

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os
import pyrax


def create_server(server_name, image_id, flavor_id):
    """ Create a Cloud Server using server_name, image_id, and flavor

    Assumes image_id and flavor_id are valid.

    Returns the ID of the server in the event further processing is needed.

    """
    creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
    pyrax.set_credential_file(creds_file)
    cs = pyrax.cloudservers

    server = cs.servers.create(server_name, image_id, flavor)

    return server.id
