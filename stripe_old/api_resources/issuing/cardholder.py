# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old.api_resources.abstract import CreateableAPIResource
from stripe_old.api_resources.abstract import ListableAPIResource
from stripe_old.api_resources.abstract import UpdateableAPIResource


class Cardholder(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.

    Related guide: [How to create a Cardholder](https://stripe.com/docs/issuing/cards#create-cardholder)
    """

    OBJECT_NAME = "issuing.cardholder"
