from odoo import fields, models, api, _


class EmployeeJoiningForm(models.Model):
    _name = 'employee.joining.form'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _description = 'Joining Form'

    name = fields.Char(string="Name")
    bank_name = fields.Char(string='Bank Name')
    spouse_name = fields.Char(string='Spouse Name')
    name_of_children = fields.Text(string='Name Of Childrens')
    bank_acc_number = fields.Char(string='Account Number')
    branch_bank = fields.Char(string='Branch')
    ifsc_code = fields.Char(string='IFSC Code')
    micr_code = fields.Char(string='MICR Code')
    aadhar_card_number = fields.Char(string='Aadhar Card Number')
    pan_card_number = fields.Char(string='Pan Card Number')
    pf_uan_number = fields.Char(string='PF UAN Number')
    esi_ip_number = fields.Char(string='ESI IP Number')
    blood_group = fields.Char(string='Blood Group')
    employee_name = fields.Char(string='Employee Name')
    designation = fields.Char(string='Designation')
    date_of_joining = fields.Date(string='Date Of Joining')
    date_of_birth = fields.Date(string='Date Of Birth')
    mail_id = fields.Char(string='Email')
    phone_number = fields.Char(string='Personal Phone Number')
    # spouse_dob = fields.Date(string='Spouse Date Of Birth')
    number_of_childes = fields.Char(string='Number Of Childes')
    marital_stats = fields.Selection([('married', 'Married'), ('single', 'Unmarried')], string='Marital Status')
    address = fields.Text(string='Address')
    fath_rel = fields.Char(string='Father Relation')
    moth_rel = fields.Char(string='Mother Relation')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', required=True, readonly=True, copy=False,
        tracking=True, default='draft')
    upload_cv = fields.Binary(string='Upload CV')
    aadhar_photo = fields.Binary(string='Aadhar Card Photo')
    pan_photo = fields.Binary(string='Pan Card Photo')
    bank_passbook = fields.Binary(string='Bank Passbook')
    photo = fields.Binary(string='Photo')
    father_number = fields.Char(string='Father Number')
    mother_number = fields.Char(string='Mother Number')
    branch = fields.Many2one('employee.branch',string='Branch')
    department_id = fields.Many2one('hr.department', string='Department')
    work_location = fields.Many2one('hr.work.location',string='Work Location(city)')
    work_place = fields.Char(string='Work Place(office)')
    highest_education_college_name = fields.Char(string='Highest Education College Name')
    highest_education_full_time_or_partime = fields.Selection(
        selection=[
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('distance', 'Distance Education'),
        ],
        string='Highest Education Qualification - Full Time / Part Time / Distance Education',default='full_time'
    )

    highest_education_degree = fields.Char(string='Highest Education Qualification - Degree')
    highest_education_qualification_specialization = fields.Char(
        string='Highest Education Qualification - Specialization')
    highest_education_qualification_passed_out_month_year = fields.Char(
        string='Highest Education Qualification - Passed Out Month Year')
    previous_employment_company_name = fields.Char(string='Previous Employment - Company Name')
    previous_employment_company_location = fields.Char(string='Previous Employment - Company Location')
    previous_employment_company_designation = fields.Char(string='Previous Employment - Company Designation')
    previous_employment_company_tenure = fields.Char(string='Previous Employment - Company Tenure')
    total_years_of_experience = fields.Integer(
        string='Total Years Of Experience')
    emergency_contact_person_name = fields.Char(string='Emergency Contact Person Name')
    emergency_contact_person_relationship = fields.Char(string='Emergency Contact Person Relationship')
    emergency_contact_person_mobile_number = fields.Char(string='Emergency Contact Person Mobile Number')
    emergency_contact_person_email = fields.Char(string='Emergency Contact Person Email')
    emergency_contact_person_correspondence_address = fields.Char(
        string='Emergency Contact Person Correspondence Address')
    emergency_details_any_allergies_specifically = fields.Char(string='Emergency Details - Any Allergies Specifically')
    nominee_name = fields.Char(string='Nominee Name')
    nominee_relation = fields.Char(string='Nominee Relation')
    nominee_id_proof = fields.Char(string='Nominee ID Proof Pan or Aadhar')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    skills = fields.Text(string="Skills ")
    hobbies = fields.Text(string="Hobbies and Intersets")
    active_social_media = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                               string='Are you active in social media')
    social_media_urls = fields.Text(string="Social media activities")
    have_you_done_anchoring = fields.Selection([('yes', 'Yes'), ('no', 'No')],
                                               string='Have you done anchoring')
    certification = fields.Text(string="Certification")
    insta_url = fields.Char(string="Instagram")
    fb_url = fields.Char(string="Facebook")
    linkedin_url = fields.Char(string="Linkedin")

    def action_confirm_employee(self):
        self.state = 'confirm'

    def action_create_user(self):
        # Create the user first
        user_vals = {
            'name': self.name,  # User name
            'login': self.mail_id,  # User login (use the office mail or unique field)
            'email': self.mail_id,
            # 'partner_id': 10# User email
        }
        user = self.env['res.users'].create(user_vals)  # Create the user

        # Call the method to create the employee and link it to this user
        self.action_create_employee(user)

        # Change the state to 'done'
        self.state = 'done'

    def action_create_employee(self, user):
        # Create the employee and link it to the user
        employee_vals = {
            'name': self.name,
            'job_title': self.designation,
            'mobile_phone': self.phone_number,
            'work_email': self.mail_id,
            'department_id': self.department_id.id,
            'private_email': self.mail_id,
            'private_phone': self.phone_number,
            'gender': self.gender,
            'date_of_joining': self.date_of_joining,
            'bank_name': self.bank_name,
            'branch_bank': self.branch_bank,
            'ifsc_code': self.ifsc_code,
            'blood_group': self.blood_group,
            'private_street': self.address,
            'private_email': self.mail_id,
            'private_phone': self.phone_number,
            'birthday': self.date_of_birth,
            'marital': self.marital_stats,
            'study_school': self.highest_education_college_name,
            'study_field': self.highest_education_degree,
            'emergency_contact': self.emergency_contact_person_name,
            'emergency_phone': self.emergency_contact_person_mobile_number,
            'emergency_contact_person_relationship': self.emergency_contact_person_relationship,
            'emergency_contact_person_email': self.emergency_contact_person_email,
            'emergency_contact_person_correspondence_address': self.emergency_contact_person_correspondence_address,
            'previous_employment_company_name': self.previous_employment_company_name,
            'previous_employment_company_location': self.previous_employment_company_location,
            'previous_employment_company_designation': self.previous_employment_company_designation,
            'total_years_of_experience': self.total_years_of_experience,
            'aadhar_card_number': self.aadhar_card_number,
            'pan_card_number': self.pan_card_number,
            'user_id': user.id,
            'branch_id': self.branch.id,
            'children': self.number_of_childes,
            'spouse_name': self.spouse_name,
            'related_joinee': self.id,  # Link the created user to the employee
            'work_location_id': self.work_location.id,
        }

        # Create the employee
        employee = self.env['hr.employee'].create(employee_vals)

    def action_cancel(self):
        self.state = 'cancel'

    def action_view_employee(self):
        """ Action to open sale orders related to the partner """
        return {
            'type': 'ir.actions.act_window',
            'name': 'Related Employee',
            'res_model': 'hr.employee',
            'view_mode': 'tree,form',
            'domain': [('related_joinee.id', '=', self.id)],
            'context': "{'create': False}"
        }

    employee_count = fields.Integer(string="Employee", compute="_compute_employee_count")

    def _compute_employee_count(self):
        for partner in self:
            employee_count = self.env['hr.employee'].search_count([('related_joinee', '=', partner.id)])
            partner.employee_count = employee_count  # ✅ Assign count correctly