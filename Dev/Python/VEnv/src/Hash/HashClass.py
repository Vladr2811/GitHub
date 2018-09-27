import hashlib
import uuid


class HashClass:

	def hash_pass(password):
		salt = uuid.uuid4().hex
		return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ":" + salt

	def check_pass(hash_password,inputPassword):
		password,salt = hash_password.split(':')
		return password == hashlib.sha512(salt.encode() + inputPassword.encode()).hexdigest()

