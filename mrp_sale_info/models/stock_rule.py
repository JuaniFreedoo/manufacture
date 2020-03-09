# -*- coding: utf-8 -*-
# Copyright 2019 Rubén Bravo <rubenred18@gmail.com>
# Copyright 2020 Juan Ignacio Úbeda <juani@freedoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models


class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _prepare_mo_vals(
        self,
        product_id,
        product_qty,
        product_uom,
        location_id,
        name,
        origin,
        values,
        bom
    ):
        res = super(StockRule, self)._prepare_mo_vals(
            product_id,
            product_qty,
            product_uom,
            location_id,
            name,
            origin,
            values,
            bom
        )
        res.update({
            'sale_procurement_group_id': values.get(
                'group_id').id if values.get('group_id', False) else False,
        })
        return res
