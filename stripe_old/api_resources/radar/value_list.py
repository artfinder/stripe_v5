# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old.api_resources.abstract import CreateableAPIResource
from stripe_old.api_resources.abstract import DeletableAPIResource
from stripe_old.api_resources.abstract import ListableAPIResource
from stripe_old.api_resources.abstract import UpdateableAPIResource


class ValueList(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Value lists allow you to group values together which can then be referenced in rules.

    Related guide: [Default Stripe Lists](https://stripe.com/docs/radar/lists#managing-list-items).
    """

    OBJECT_NAME = "radar.value_list"
