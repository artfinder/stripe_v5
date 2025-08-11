# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old.api_resources.abstract import CreateableAPIResource
from stripe_old.api_resources.abstract import ListableAPIResource
from stripe_old.api_resources.abstract import UpdateableAPIResource


class Configuration(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    A portal configuration describes the functionality and behavior of a portal session.
    """

    OBJECT_NAME = "billing_portal.configuration"
