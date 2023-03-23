from Orderconfirmation.orderconfirmation.order_confirmation import send_order_confirmation_email
def test_order_confirmation_email():
    # simulate placing an order and receiving an order confirmation email
    user_email = "testuser@example.com"
    order_details = "Order #12345\n\nItem 1: Widget\nItem 2: Gizmo\nTotal: $10.99"

    # call the send_order_confirmation_email function with the test data
    actual_result = send_order_confirmation_email(user_email, order_details)

    # assert that the email was sent successfully
    expected_result = "Thank you for your order! Here are your order details:\n\n{}\n\nPlease let us know if you have any questions or concerns.".format(order_details)
    assert actual_result == expected_result
