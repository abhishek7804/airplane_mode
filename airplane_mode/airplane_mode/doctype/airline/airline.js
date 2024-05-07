// Copyright (c) 2024, Abhishek Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
  refresh(frm) {
    if (frm.doc.website) {
      const site_link = frm.doc.website;
      frm.add_web_link(site_link, "Visit Website");
    }
  },
});
