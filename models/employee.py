from odoo import fields,models,api,_

class InheritEmployee(models.Model):
    _inherit = 'hr.employee'

    related_joinee = fields.Many2one('employee.joining.form', string="Related Joinee")
    blood_group = fields.Char(string='Blood Group')
    emergency_contact_person_relationship = fields.Char(string='Emergency Contact Person Relationship')
    emergency_contact_person_email = fields.Char(string='Emergency Contact Person Email')
    emergency_contact_person_correspondence_address = fields.Char(
        string='Emergency Contact Person Correspondence Address')

    bank_name = fields.Char(string='Bank Name')
    branch_bank = fields.Char(string='Branch')
    ifsc_code = fields.Char(string='IFSC Code')

    spouse_name = fields.Char(string='Spouse Name')

    date_of_joining = fields.Date(string='Date Of Joining')

    previous_employment_company_name = fields.Char(string='Previous Employment - Company Name')
    previous_employment_company_location = fields.Char(string='Previous Employment - Company Location')
    previous_employment_company_designation = fields.Char(string='Previous Employment - Company Designation')
    total_years_of_experience = fields.Integer(
        string='Total Years Of Experience')

    aadhar_card_number = fields.Char(string='Aadhar Card Number')
    pan_card_number = fields.Char(string='Pan Card Number')
