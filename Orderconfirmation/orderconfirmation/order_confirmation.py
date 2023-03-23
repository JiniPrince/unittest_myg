def send_order_confirmation_email(user_email, order_details):

    # construct email message
    message = "Thank you for your order! Here are your order details:\n\n{}\n\nPlease let us know if you have any questions or concerns.".format(order_details)

    # send email to user
    # (in a real implementation, this would use a library like smtplib to actually send the email)
    print("Sending order confirmation email to {}...".format(user_email))
    print("Email message:\n\n{}\n".format(message))

    # return success message
    return message
