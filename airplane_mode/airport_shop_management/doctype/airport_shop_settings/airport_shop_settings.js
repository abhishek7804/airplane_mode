// Copyright (c) 2024, Abhishek Kumar and contributors
// For license information, please see license.txt
frappe.ui.form.on("Shop Contract Details", {
    onload: function(frm) {
        if (frm.doc.__islocal) {
            frappe.db.get_single_value("Airport Shop Settings","default_rent_amount").then((response) => {
                console.log(response);
                frm.set_value("rent_amount", response);
            });
        }
    }
});