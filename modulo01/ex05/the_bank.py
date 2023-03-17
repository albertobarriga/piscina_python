class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name

		if not hasattr(self, "value"):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")

		if not isinstance(self.name, str)
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount
	
	def is_corrupted(self):
		args = list(self.__dict__.keys())
		if not len(args) % 2 == 0:
			return(True)
		
		if "name" not in args \
			or "id" not in args \
			or "value" not in args:
			return (True)
		
		for arg in args:
			if arg[0] == "b":
				return(True)
			if not arg.startswith("zip") or not arg.startswith("addr"):
				return(True)
		return (False)

class Bank(object):
		"""The bank"""
	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
			@return   True if success, False if an error occured
		"""
		# test if new_account is an Account() instance and if # it can be appended to the attribute accounts
		if not isinstance(new_account, Account):
			return(False)
		self.accounts.append(new_account)

	def get_account(self, name):
		if isinstance(name, int):
			for account in self.account:
				if account.id == name:
					return (account)
		if isinstance(name, str):
			for account in self.account:
				if account.name == name:
					return (account)

	def transfer(self, origin, dest, amount: float):
		"""" Perform the fund transfer
			@origin:  str(name) of the first account
			@dest:    str(name) of the destination account
			@amount:  float(amount) amount to transfer
			@return   True if success, False if an error occured
		"""
		origin_account = self.get_account(origin)
		dest_account = self.get_account(dest)
		if not isinstance(origin_account, Account) or not isinstance(dest_account, Account):
			return (False)
		elif not origin_account.is_corrupted() and not dest_account.is_corrupted():
			return (False)
		value = origin_account.value
		if value < amount or value < 0:
			return (False)
		origin_account.value -= amount
		dest_account.value.transfer(amount)
		return (True)
			
		
	def fix_account(self, name):
		""" fix account associated to name if corrupted
			@name:   str(name) of the account
			@return  True if success, False if an error occured
		"""
		# ... Your code ...