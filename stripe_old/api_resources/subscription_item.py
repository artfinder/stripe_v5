# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old.api_resources.abstract import CreateableAPIResource
from stripe_old.api_resources.abstract import DeletableAPIResource
from stripe_old.api_resources.abstract import ListableAPIResource
from stripe_old.api_resources.abstract import UpdateableAPIResource
from stripe_old.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods("usage_record", operations=["create"])
@nested_resource_class_methods(
    "usage_record_summary",
    operations=["list"],
    resource_plural="usage_record_summaries",
)
class SubscriptionItem(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Subscription items allow you to create customer subscriptions with more than
    one plan, making it easy to represent complex billing relationships.
    """

    OBJECT_NAME = "subscription_item"
