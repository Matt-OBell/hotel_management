# See LICENSE file for full copyright and licensing details.

{
    'name': 'Reservation',
    'author': 'Mattobell Nigeria Ltd, OpenERP SA',
    'category': 'Generic Modules/Hotel Reservation',
    'website': 'http://www.mattobell.com',
    'depends': [
        'hotel',
    ],
    'license': 'LGPL-3',
    'demo': [
    ],
    'data': [
        'data/ir_sequence.xml',
        'data/mail_template.xml',
        'security/ir.model.access.csv',
        'views/hotel_reservation.xml',
        'wizard/hotel_reservation_wizard.xml',
        'report/hotel_reservation_report.xml',
        'views/report_checkin.xml',
        'views/report_checkout.xml',
        'views/max_room.xml',
        'views/room_res.xml',
        'views/room_summ_view.xml',
    ],
    # 'js': ['static/src/js/hotel_room_summary.js', ],
    'qweb': ['static/src/xml/hotel_room_summary.xml'],
    'css': ['static/src/css/room_summary.css'],
    'images': ['static/description/HotelReservation.png'],
    'installable': True,
    'auto_install': False,
}
