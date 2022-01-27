# -*- coding: utf-8 -*-
{
    'name': "Order kanban view in crm.lead", 
    'version': '14.0.0.1',
    'category': 'Sales',
    'depends': ['sale'],
    'license': 'AGPL-3',
    'summary': 'Order kanban view in crm.lead',
    'description': """
Changes sort in  kanban view in crm.lead  by create date
    """,
    'installable': True,
    'auto_install': False,
    'author': "",

    'data': [
        'views/views.xml',
    ],
}
