# Copyright (c) 2024, Abhishek kumar and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data()
	chart=get_chart_data(data)
	report_summary=get_summary(data)
	return columns, data ,None , chart ,report_summary

def get_columns():
    columns = [
        {
            "fieldname": "airline",
            "label": "Airlines",
            "fieldtype": "Link",
            "options": "Airline",
			"width":200
        },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
			"width":200
        }
    ]
    return columns


def get_data():
    all_data = frappe.db.sql("""
        SELECT al.name AS airline, COALESCE(SUM(at.total_amount), 0) AS revenue
        FROM `tabAirline` al
        LEFT JOIN `tabAirplane` ap ON ap.airline = al.name
        LEFT JOIN `tabAirplane Flight` af ON af.airplane = ap.name
        LEFT JOIN `tabAirplane Ticket` at ON at.flight = af.name AND at.docstatus = 1
        GROUP BY al.name ORDER BY revenue desc
    """, as_dict=True)
    return all_data








def get_chart_data(data):
    if data:
        labels = []
        values = []
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#C0C0C0', '#808080', '#800000', '#808000', '#008000', '#800080', '#008080', '#000080']
        for report_data in data:
            labels.append(report_data.airline)
            values.append(report_data.revenue)

        chart = {
            'data': {
                'labels': labels,
                'datasets': [
                    {
                        'name': 'amount',
                        'chartType': 'pie',
                        'values': values
                    }
                ]
            },
            'type': 'pie',
            'colors': colors
        }
        return chart
    else:
        return None


def get_summary(data):
	total_revenue = 0.0
	if data:
		for reneue_data in data:
			total_revenue = total_revenue +flt(reneue_data.revenue)

	return [
		{
			"value": total_revenue,
			"label": _("Total Revenue"),
			"datatype": "Currency",
			"indicator":"Green" if total_revenue else "Red"
		}
	]
