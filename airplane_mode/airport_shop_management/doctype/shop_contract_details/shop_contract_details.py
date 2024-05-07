# Copyright (c) 2024, Abhishek Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _
import frappe.utils


class ShopContractDetails(Document):
	def on_submit(self):
		frappe.db.set_value("Airport Shop",self.airport_shop,"shop_contract_details",self.name,update_modified=True)


def reminder_for_payment():
	all_data=frappe.get_all("Shop Contract Details",{"docstatus":1,"airport_shop":["!=",["",None]],"expiry_date": ("=",frappe.utils.nowdate() )},["tenant","airport_shop","airport","name"])
	email_list=[]
	for data in all_data:
		email=frappe.db.get_value("Tenant Tnformation",{"name":data.tenant},"email")
		email_list.append(email)
	if email_list:
		subject="Payment Sheduler"
		message="Reminder for payment for next month"
		frappe.sendmail(
				email_list,
				subject=subject,
				message=message,
				delayed=True)



