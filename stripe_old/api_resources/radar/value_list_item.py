# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old.api_resources.abstract import CreateableAPIResource
from stripe_old.api_resources.abstract import DeletableAPIResource
from stripe_old.api_resources.abstract import ListableAPIResource


class ValueListItem(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
):
    """
    Value list items allow you to add specific values to a given Radar value list, which can then be used in rules.

    Related guide: [Managing List Items](https://stripe.com/docs/radar/lists#managing-list-items).
    """

    OBJECT_NAME = "radar.value_list_item"
