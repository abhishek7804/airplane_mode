// Copyright (c) 2024, Abhishek Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
  refresh(frm) {
    if (frm.doc.airplane) {
      frappe.db
        .get_value("Airplane", frm.doc.airplane, "airline")
        .then((response) => {
          let airline = response.message.airline;

          frm.fields_dict["crew_members"].grid.get_field(
            "crew_member"
          ).get_query = function (doc, cdt, cdn) {
            return {
              filters: [
                ["airline", "=", airline],
                [
                  "name",
                  "not in",
                  frm.doc.crew_members.map((row) => row.crew_member),
                ],
                ["enabled","=",1]
              ],
            };
          };
        });
    }
    if (frm.doc.source_airport) {
      frm.set_query("entry_gate_number", () => {
        return {
          filters: {
            airport: frm.doc.source_airport,
          },
        };
      });
    }
    if (frm.doc.destination_airport) {
      frm.set_query("exit_gate_number", () => {
        return {
          filters: {
            airport: frm.doc.destination_airport,
          },
        };
      });
    }
  },
  airplane(frm) {
    frappe.db
      .get_value("Airplane", frm.doc.airplane, "airline")
      .then((response) => {
        let airline = response.message.airline;

        frm.fields_dict["crew_members"].grid.get_field(
          "crew_member"
        ).get_query = function (doc, cdt, cdn) {
          return {
            filters: [
              ["airline", "=", airline],
              [
                "name",
                "not in",
                frm.doc.crew_members.map((row) => row.crew_member),
              ],
              ["enabled","=",1]
            ],
          };
        };
      });
    frm.refresh_fields("crew_members");
  },
  source_airport(frm) {
    if (frm.doc.source_airport) {
      frm.set_query("entry_gate_number", () => {
        return {
          filters: {
            airport: frm.doc.source_airport,
          },
        };
      });
    }
  },
  destination_airport(frm) {
    if (frm.doc.destination_airport) {
      frm.set_query("exit_gate_number", () => {
        return {
          filters: {
            airport: frm.doc.destination_airport,
          },
        };
      });
    }
  },
});
