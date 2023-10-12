# Copyright (c) 2023, vignesh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Productmovement(Document):
	
	
	def before_save(self):


		if self.from_location != "" and self.to_location != "":
			product_from_location = frappe.get_doc("Location", {"name": self.from_location, "product_name": self.product_id})
			product_to_location = frappe.get_doc("Location", {"name": self.to_location, "product_name": self.product_id})
			product_from_location.quantity -= self.qty
			product_to_location.quantity += self.qty
			product_from_location.save()
			product_to_location.save()
		elif self.from_location == "" and self.to_location != "":
			product_to_location = frappe.get_doc("Location", {"name": self.to_location, "product_name": self.product_id})
			product_quantity = frappe.get_doc("Product", {"product_name": self.product_id})
			# product_to_location = frappe.get_doc("Location", {"name": self.to_location, "product_name": self.product_id})
			product_to_location.quantity += self.qty
			product_quantity.quantity -= self.qty
			product_quantity.save()
			product_to_location.save()
		else:
			frappe.msgprint("Please enter the to location and qty")




