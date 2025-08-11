# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe_old import util
from stripe_old.api_resources.abstract import APIResource
from stripe_old.api_resources.customer import Customer
from stripe_old.six.moves.urllib.parse import quote_plus


class CashBalance(APIResource):
    """
    A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """

    OBJECT_NAME = "cash_balance"

    def instance_url(self):
        customer = util.utf8(self.customer)
        base = Customer.class_url()
        cust_extn = quote_plus(customer)
        return "%s/%s/cash_balance" % (base, cust_extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a Customer Cash Balance without a Customer ID. "
            "Use Customer.retrieve_cash_balance('cus_123')"
        )
