# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2010 - 2014 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': "Sentry Logger",

    'summary': "Sentry integration",
    'description': """
Sentry
======

Integration with Sentry Error reporting engine.

Insert sentry DSN to ~/.openerp_serverrc with value:
    sentry_dsn = sync+<Your Sentry DSN>


Optional Dependencies
---------------------

* bzrlib (for revno reporting on module repositories from LP)

Notes
-----

Module may slow down spawning of workers (~1s) due to the access of openerp
configuration

Contributors
------------
* Sandy Carter (sandy.carter@savoirfairelinux.com)
""",

    'author': "Savoir-faire Linux",
    'website': "http://www.savoirfairelinux.com",

    # Categories can be used to filter modules in modules listing
    # Check <odoo>/addons/base/module/module_data.xml of the full list
    'category': 'Extra Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['web'],
    'external_dependencies': {
        'python': [
            'raven',
            'raven_sanitize_openerp',
            'git',
        ],
    },
    'data': [
    ],

    'demo': [
    ],

    'qweb': [
        'static/src/xml/base.xml',
    ],

    'tests': [
    ],
}