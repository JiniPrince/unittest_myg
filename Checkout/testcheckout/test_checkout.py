from Checkout.checkout.checkout import checkout_process
def test_successful_checkout():
    # simulate a successful checkout process with valid shipping and payment information
    shipping_address = "Hanna cottage,chirayinkeezhu tvm"
    payment_info = "Visa 1234-5678-9012-3456"
    expected_order_summary = "Your order has been placed. Shipping to: {}\nPayment method: {}".format(shipping_address, payment_info)

    # call the checkout_process function with the test data
    actual_order_summary = checkout_process(shipping_address, payment_info)

    # assert that the actual order summary matches the expected order summary
    assert actual_order_summary == expected_order_summary

def test_invalid_shipping_address():
    # simulate a checkout process with an invalid shipping address
    shipping_address = ""
    payment_info = "Visa 1234-5678-9012-3456"
    expected_error_message = "Please enter a valid shipping address"

    # call the checkout_process function with the test data
    actual_error_message = checkout_process(shipping_address, payment_info)

    # assert that the actual error message matches the expected error message
    assert actual_error_message == expected_error_message
