# Copyright (c) 2024, Abhishek Kumar and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CrewMember(Document):
	def before_save(self):
		if self.first_name and self.last_name:
			self.full_name = f"{self.first_name} {self.last_name}".strip()
		elif self.first_name:
			self.full_name = self.first_name.strip()
		elif self.last_name:
			self.full_name = self.last_name.strip()
		else:
			self.full_name = ""
