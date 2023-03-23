# livechat.py

class WhatsAppChatRedirect:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def redirect_chat_to_whatsapp(self, customer_name):
        message = f"Hi {customer_name}, thanks for chatting with us! We've redirected your chat to WhatsApp. Please check your WhatsApp messages for further assistance."
        # Code to redirect the chat session to a WhatsApp chat goes here
        return message
