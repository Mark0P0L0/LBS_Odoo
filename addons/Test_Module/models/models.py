# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Test(models.Model):
    _name = 'test.model'

    test_name = fields.Char(string="Title", required=True)
    test_purpose = fields.Text(string="Test purpose")
    tester_id = fields.Many2one('res.partner', string="Tester", domain=['|', ('tester', '=', True), ('category_id.name',"Tester")])

class TestSession(models.Model):
    _name = 'test.session'

    name = fields.Char(required=True)
    test = _fields.Many2one("test.model", ondelete='casscade', string='Test', required=True)
    start_date = fields.Date(string="Start date", default=fields.Date.today)
    end_date = fields.Date(string="Start date", default=fields.Date.today, compute="_session_duration")
    duration = fields.Float(digits=(6, 2), help="Duration in days")

    @api.depends('start_date', 'end_date')
    def _session_duration(self):
        for r in self:
            if not (r.start_date and r.end_date):
                r.duration = 0.0
            else:
                time_delta = (fields.Datetime.from_string(r.end_date) - fields.Datetime.from_string(r.start_date))
                r.duration = time_delta_days + 1

    @api.onchange('start_date', 'end_date')
    def _verify_valid_dates(self):
        if fields.Datetime.from_string(self.end_date) < fields.Datetime.from_string(self.start_date):
            return {
                'warning': {
                    'title': "Incorrect date values",
                    'message': "Start date can't be later than the end date",
                    },

}
class Subtask(models.Model):
    _name = 'lbs_test.subtask'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    resposible = fields.Many2one('res.users',
                                ondelete='set null', string="Responsible user", index=True)
    state = fields.Selection([('cancelled', "Cancelled"),
                                ('todo', "To do"),
                                ('done', "Done"),
                                ], default='todo')
    task = fields.Many2one('project.task',
                           ondelete='set null', string="Main task", index=True)



class Task(models.Model):
    _inherit = 'project.task'

subtask_ids = fields.One2many('lbs_test.subtask', 'task', string="Subtasks")