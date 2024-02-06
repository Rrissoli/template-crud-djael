from contextlib import nullcontext
import uuid
from xmlrpc.client import DateTime


class Category:
	def __init__(
			self,
			name,
			id = "",
			description = "",
			is_active = True,
			created_at =  DateTime(),
            updated_at = DateTime(),
            deleted_at = nullcontext,
	):
		self.id = id or uuid.uuid4()
		self.name = name
		self.description = description
		self.is_active = is_active
		self.created_at = created_at
		self.updated_at = updated_at
		self.deleted_at = deleted_at
	
	def __str__(self) -> str:
		return f"{self.id} - {self.name} -  {self.description} -  {self.is_active} - {self.created_at}"
	def __repr__(self) -> str:
		return f"<Category {self.id} - {self.name} -  {self.description} -  {self.is_active} - {self.created_at}>"