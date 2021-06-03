# -*- coding: utf-8 -*-
#    Copyright (C) 2007  pronexo.com  (https://www.pronexo.com)
#    All Rights Reserved.
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
############################################################################## # 
# 
{
	'name': 'Owl POS Super',
	'summary': 'Ejemplo de como reemplazar un mensaje en el POS de Odoo',
	'description': 'Ejemplo de como reemplazar un mensaje en el POS de Odoo',
	'version': '14.1.0.0',
	'author': 'Pronexo',
    'website': "https://www.pronexo.com",
    'category': 'Sales/Point of Sale',
	'license': "AGPL-3",
	'maintainer': 'pronexo.com',
	'depends': [
		'point_of_sale'
	],
	'data': [
        'views/assets.xml',
    ],
	'external_dependencies': {
   
    },
	'auto_install': False,
	'installable': True,

}
