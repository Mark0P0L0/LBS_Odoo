# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    isTester = fields.Boolean("Tester", default=False, readonly=True, )

    @api.depends()
    def _is_tester(self):
        for r in self:
            r.isTester = (self.env['test.model'].search_count([("tester.id", "=", r.id)]) > 0)

    session_ids = fields.Many2many('openacademy.session',
        string="Attended Sessions", readonly=True)
