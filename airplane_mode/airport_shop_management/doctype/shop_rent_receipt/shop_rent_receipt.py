# Copyright (c) 2024, Abhishek Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months


class ShopRentReceipt(Document):
	def validate(self):
		self.to_date = add_months(self.from_date,self.tenure)
		self.grand_total = self.payment_per_month*self.tenure
		
	def on_submit(self):
		airport_shop = frappe.db.get_value("Shop Contract Details",self.shop_contract_details,"airport_shop")
		self.expiry_date_validation(airport_shop)
		self.update_expires_date()
		
	def expiry_date_validation(self,airport_shop):
		if self.to_date:
			if frappe.db.exists(self.doctype, {"docstatus":1,"airport_shop":airport_shop,"to_date": (">=",self.from_date ), "name": ("!=", self.name)}):
				frappe.throw(frappe._("This shop is already rented for this Date!"))
	
	def update_expires_date(self):
		frappe.db.set_value("Shop Contract Details",self.shop_contract_details,"expiry_date",self.to_date)