#signin.py
def signin(first_name, last_name, phone, email, password, confirm_password):
    if len(first_name) > 0 and len(last_name) > 0 and len(phone) == 10 and "@" in email and password == confirm_password:

        return True
    else:
        return False





def send_otp(phone, otp):

    print(f"Sending OTP {otp} to {phone}...")
    # simulate waiting for the OTP to be verified within 5 seconds
    for i in range(5):
        entered_otp = input("Enter OTP: ")
        if entered_otp == otp:
            return True #"OTP verified successfully"
        else:
            print("Incorrect OTP. Please try again.")
    # if the OTP is not verified within 5 seconds, return an error message
    return "OTP verification timed out"
