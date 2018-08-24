# See LICENSE file for full copyright and licensing details.

{
    'name': 'Hotel Restaurant Management',
    'version': '10.0.1.0.0',
    'author': 'Serpent Consulting Services Pvt. Ltd., OpenERP SA',
    'category': 'Generic Modules/Hotel Restaurant',
    'website': 'http://www.serpentcs.com',
    'depends': ['hotel'],
    'license': 'AGPL-3',
    'demo': [
        # 'views/hotel_restaurant_data.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/hotel_restaurant_report.xml',
        'wizard/hotel_restaurant_wizard.xml',
        'views/res_table.xml',
        'views/kot.xml',
        'views/bill.xml',
        'views/folio_order_report.xml',
        'views/ir_sequence.xml',
        'views/hotel_restaurant_view.xml',
    ],
    'images': ['static/description/HotelRestaurant.png'],
    'installable': True
}
