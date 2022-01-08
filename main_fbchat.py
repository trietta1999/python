# -*- coding: UTF-8 -*-
import streamlit as st
import sys

sys.path.append("fbchat_lib")
from fbchat_lib import Client

# Subclass fbchat.Client and override required methods
class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		st.write(message_object.text)

		# If you're not the author, echo
		if author_id != self.uid:
			message_object.text = "Đã nhận 🎉"
			self.send(message_object, thread_id=thread_id, thread_type=thread_type)
		
client = EchoBot(email="ttbotpython@gmail.com", password="Triet@2312", code="91720553")
client.listen()
