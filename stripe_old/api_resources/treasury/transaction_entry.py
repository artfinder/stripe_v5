# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old.api_resources.abstract import ListableAPIResource


class TransactionEntry(ListableAPIResource):
    """
    TransactionEntries represent individual units of money movements within a single [Transaction](https://stripe.com/docs/api#transactions).
    """

    OBJECT_NAME = "treasury.transaction_entry"

    @classmethod
    def class_url(cls):
        return "/v1/treasury/transaction_entries"
