# -*- coding: utf-8 -*-
{
    'name': "INSURANCE AGGREGATOR KSA",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "TRANSGLOBAL LLC.",
    'website': "https://www.transglobal.com.eg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', "sale",
                "account_auto_transfer",
                "theme_default",
                "base_setup",
                "snailmail_account",
                "sales_team",
                "auth_signup",
                "web",
                "account_accountant",
                "utm",
                "social_media",
                "http_routing",
                "account_asset",
                "portal",
                "website",
                "iap_mail",
                "account_bank_statement_import_camt",
                "bus",
                "web_dashboard",
                "sms",
                "account_edi_ubl",
                "website_sms",
                "account_bank_statement_import",
                "analytic",
                "auth_totp_portal",
                "fetchmail",
                "website_mail",
                "resource",
                "web_mobile",
                "web_editor",
                "account_ponto",
                "account_followup",
                "rating",
                "account_bank_statement_import_csv",
                "portal_rating",
                "account_online_synchronization",
                "product",
                "l10n_sa",
                "website_livechat",
                "account_online_sync",
                "website_form",
                "web_kanban_gauge",
                "account_reports_tax",
                "account_yodlee",
                "snailmail_account_followup",
                "account_predictive_bills",
                "web_gantt",
                "payment_transfer",
                "web_enterprise",
                "payment",
                "website_payment",
                "web_grid",
                "analytic_enterprise",
                "uom",
                "account_reports",
                "snailmail",
                "mail_bot",
                "mail_mobile",
                "account",
                "account_edi",
                "im_livechat_mail_bot",
                "google_recaptcha",
                "digest",
                "base_import",
                "phone_validation",
                "mail",
                "digest_enterprise",
                "currency_rate_live",
                "iap",
                "im_livechat_enterprise",
                "account_bank_statement_import_ofx",
                "im_livechat",
                "website_sale_dashboard",
                "account_budget",
                "mail_enterprise",
                "web_map",
                "website_enterprise",
                "auth_totp",
                "sale_account_accountant",
                "account_invoice_extract",
                "account_edi_facturx",
                "l10n_multilang",
                "account_plaid",
                "payment_fix_register_token",
                "website_sale",
                "web_cohort",
                "web_tour",
                "base",
                "sale_enterprise"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/wb_homepage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'external_dependencies': {
        'python': ['hijri-converter',
                   'pyfcm']
    },
    'installable': True,
    'application': True,
    'uninstall_hook': 'uninstall_hook',
}
