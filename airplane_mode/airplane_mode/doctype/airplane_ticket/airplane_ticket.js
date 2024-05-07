frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        if (frm.doc.docstatus===0){
            frm.add_custom_button(("Assign Seat"), function() {
                frappe.prompt({
                    label: 'Seat',
                    fieldname: 'seat',
                    fieldtype: 'Data'
                }, (values) => {
                    frm.set_value("seat",values.seat)
                    frm.refresh_fields("seat")
                })
            }, ("Action"));
        }
    },
});