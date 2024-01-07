#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64, logging
from cryptography.fernet import Fernet

''' Core '''
from fast_food.core.settings import Settings
from fast_food.core.translations import TR_CRYPT_ENCODE, TR_CRYPT_DECODE

''' Internal Logs '''
def log():
	return logging.getLogger(__name__) #.info() .debug() .warning() .error()

#SECRET_KEY = "X7Sab6LFWwjEv1UYlWZAEDZ1M6V04hk8"

class Crypt():
	def __init__(self, SECRET_KEY = Settings().SECRET_KEY):
		self.key = self.generate_key(SECRET_KEY)
		self.cipher_suite = Fernet(self.key)

	#@staticmethod
	def generate_key(self, KEY):
		return base64.urlsafe_b64encode(KEY.encode())

	def encode(self, password):
		log().info(TR_CRYPT_ENCODE)
		encrypted_password = self.cipher_suite.encrypt(password.encode())
		return encrypted_password.decode()

	def decode(self, encoded_password):
		log().info(TR_CRYPT_DECODE)
		decrypted_password = self.cipher_suite.decrypt(encoded_password.encode())
		return decrypted_password.decode()
