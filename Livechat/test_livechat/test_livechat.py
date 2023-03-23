# test_livechat.py

import pytest
from Livechat.livechat.livechat import WhatsAppChatRedirect
@pytest.fixture
def whatsapp_chat_redirect():
    return WhatsAppChatRedirect('12345')

def test_redirect_chat_to_whatsapp(whatsapp_chat_redirect):
    customer_name = 'John Doe'
    message = whatsapp_chat_redirect.redirect_chat_to_whatsapp(customer_name)
    assert message == f"Hi {customer_name}, thanks for chatting with us! We've redirected your chat to WhatsApp. Please check your WhatsApp messages for further assistance."
