def checkout_process(shipping_address, payment_info):
    # validate shipping address
    if not shipping_address:
        return "Please enter a valid shipping address"

    # validate payment information
    if not payment_info:
        return "Please enter a valid payment method"

    # process order
    order_summary = "Your order has been placed. Shipping to: {}\nPayment method: {}".format(shipping_address, payment_info)
    return order_summary
