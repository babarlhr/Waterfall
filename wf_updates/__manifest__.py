# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'wf Updates',
    'summary': 'all customization of the wfpumps',
    'depends': ['base','sale','product','mrp','stock','sale_management','sales_team'],
    'data': [
        'wizard/quotations_seals.xml',
        'views/test_view.xml',
        'report/wf_saleperson.xml',
        'report/purchase_reports.xml',
        'report/Poproduct_detailed_report.xml',
        'report/product_product_templates.xml',
     
        'report/report_mrp_workorder.xml',
        'report/sale_report_templates.xml',
        'report/sale_report.xml',
        'report/wf_qoutation_report.xml',
        'report/wf_qoutation_arabic_report.xml',
        'report/wf_packing_list_report.xml',
        'report/wf_packing_list_arabic_report.xml',
        'report/purchase_order_templates.xml',
        'report/Odoo_Studio_report_wf_quotation_document_customization.xml',
        'report/report_purchaseorder_document_customization.xml',
        'report/report_deliveryslip.xml',
        'report/report_deliveryslip_customization.xml',
        'report/report_invoice.xml',
        'report/report_invoice_arabic.xml',
        'report/wf_predispatch_report.xml',
        'report/report_payment_receipt_templates.xml',
        'report/report_templates.xml',
        'report/report_stockpicking_operations.xml',
        'report/report_delivery_order.xml',
        'report/report_wf_costanalysis.xml',
        'report/product_ncr_templates.xml',
        'report/product_report.xml',
        'report/sales_order_acknowledgement.xml',
        'report/purchase_price_comparison.xml',
        'security/ir.model.access.csv',
        'security/wf_security.xml',
        'data/WF_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
