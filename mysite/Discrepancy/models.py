# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InvoiceUom(models.Model):
    damageuomid = models.AutoField(db_column='DamageUOMID', primary_key=True)  # Field name made lowercase.
    damageuom = models.TextField(db_column='DamageUOM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Invoice UOM'


class InvoiceUom(models.Model):
    damageuomid = models.AutoField(db_column='DamageUOMID', primary_key=True)  # Field name made lowercase.
    damageuom = models.TextField(db_column='DamageUOM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Invoice-UOM'


class InvoiceUom(models.Model):
    damageuomid = models.AutoField(db_column='DamageUOMID', primary_key=True)  # Field name made lowercase.
    damageuom = models.TextField(db_column='DamageUOM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    damageuomid_0 = models.AutoField(db_column='DamageUOMID', primary_key=True)  # Field name made lowercase. Field renamed because of name conflict.
    damageuom_0 = models.TextField(db_column='DamageUOM', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict. This field type is a guess.
    damageuomid_1 = models.AutoField(db_column='DamageUOMID', primary_key=True)  # Field name made lowercase. Field renamed because of name conflict.
    damageuom_1 = models.TextField(db_column='DamageUOM', blank=True, null=True)  # Field name made lowercase. Field renamed because of name conflict. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Invoice_UOM'


class JdAction(models.Model):
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Action'


class JdArea(models.Model):
    areaid = models.AutoField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    area = models.TextField(db_column='Area', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Area'


class JdBuilding(models.Model):
    buildingid = models.AutoField(db_column='BuildingID', primary_key=True)  # Field name made lowercase.
    building = models.TextField(db_column='Building', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Building'


class JdClaimclass(models.Model):
    claimclassid = models.AutoField(db_column='ClaimClassID', primary_key=True)  # Field name made lowercase.
    claimclass = models.TextField(db_column='ClaimClass', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Claimclass'


class JdFinancialtype(models.Model):
    financialtypeid = models.AutoField(db_column='FinancialTypeID', primary_key=True)  # Field name made lowercase.
    financialtype = models.TextField(db_column='FinancialType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Financialtype'


class JdIncaseofglobalclaim(models.Model):
    in_case_of_global_claim = models.AutoField(db_column='In Case of Global Claim', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    incident_accident_action_confirmation_form_number = models.IntegerField(db_column='Incident/Accident Action Confirmation Form number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    claim_number = models.CharField(db_column='Claim Number', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forwarder_vendor_name = models.CharField(db_column='Forwarder/Vendor Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reimbursement_amount_field = models.FloatField(db_column='Reimbursement Amount ($)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_of_reimbursement = models.DateField(db_column='Date of Reimbursement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    close_date = models.DateField(db_column='Close date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    report_by = models.CharField(db_column='Report by', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_date = models.DateField(db_column='Report Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'JD_Incaseofglobalclaim'


class JdIncaseoflocalclaim(models.Model):
    in_case_of_local_claim = models.AutoField(db_column='In Case of Local Claim', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    incident_accident_action_confirmation_form_number = models.IntegerField(db_column='Incident/Accident Action Confirmation Form number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    forwarder_vendor_name = models.CharField(db_column='Forwarder/Vendor Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paymentmethodid = models.IntegerField(db_column='PaymentMethodID', blank=True, null=True)  # Field name made lowercase.
    cheque_or_payment_number = models.TextField(db_column='Cheque or payment number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    reimbursement_amount_field = models.FloatField(db_column='Reimbursement Amount ($)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    date_of_reimbursement = models.DateField(db_column='Date of Reimbursement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reimbursement_evident_file = models.CharField(db_column='Reimbursement Evident_file', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_acceptance = models.TextField(db_column='WD Acceptance', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wd_acceptor = models.CharField(db_column='WD Acceptor', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wd_acceptance_date = models.DateField(db_column='WD Acceptance Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    close_date = models.DateField(db_column='Close date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'JD_Incaseoflocalclaim'


class JdInventorytype(models.Model):
    inventorytypeid = models.AutoField(db_column='InventoryTypeID', primary_key=True)  # Field name made lowercase.
    inventorytype = models.TextField(db_column='InventoryType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Inventorytype'


class JdModeoftransportation(models.Model):
    modeoftransportationid = models.AutoField(db_column='ModeofTransportationID', primary_key=True)  # Field name made lowercase.
    modeoftransportation = models.TextField(db_column='ModeofTransportation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Modeoftransportation'


class JdPaymentmethod(models.Model):
    paymentmethodid = models.AutoField(db_column='PaymentMethodID', primary_key=True)  # Field name made lowercase.
    paymentmethod = models.TextField(db_column='PaymentMethod', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Paymentmethod'


class JdSqeinspectionform(models.Model):
    sqe_inspection_form_number = models.AutoField(db_column='SQE Inspection Form number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    requester_buyer_s_disposition_result_form_number = models.IntegerField(db_column="Requester/Buyer's Disposition Result Form number", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sqe_decision = models.TextField(db_column='SQE Decision', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    not_accept_quantity = models.IntegerField(db_column='Not Accept Quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sqe_remark = models.TextField(db_column='SQE Remark', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    picture_file = models.CharField(db_column='Picture_file', max_length=255, blank=True, null=True)  # Field name made lowercase.
    report_by = models.CharField(db_column='Report by', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_date = models.DateField(db_column='Report Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    remark = models.TextField(db_column='Remark', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    approve_by = models.CharField(db_column='Approve By', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    approve_date = models.DateField(db_column='Approve Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logistics_decision = models.TextField(db_column='Logistics Decision', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    concur_by = models.CharField(db_column='Concur by', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    concur_date = models.DateField(db_column='Concur Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'JD_SQEinspectionform'


class JdShipmentsdamagerecordform(models.Model):
    transaction_number = models.AutoField(db_column='Transaction Number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    areaid = models.ForeignKey(JdArea, models.DO_NOTHING, db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    lanetypeid = models.ForeignKey('JdLanetype', models.DO_NOTHING, db_column='laneTypeID', blank=True, null=True)  # Field name made lowercase.
    flight_number = models.TextField(db_column='Flight Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    modeoftransportationid = models.ForeignKey(JdModeoftransportation, models.DO_NOTHING, db_column='ModeofTransportationID', blank=True, null=True)  # Field name made lowercase.
    forwarder = models.TextField(db_column='Forwarder', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shipper_name = models.TextField(db_column='Shipper Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    shipper_country = models.TextField(db_column='Shipper Country', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    incident_location_name = models.TextField(db_column='Incident Location Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    buildingid = models.ForeignKey(JdBuilding, models.DO_NOTHING, db_column='BuildingID', blank=True, null=True)  # Field name made lowercase.
    financialtypeid = models.ForeignKey(JdFinancialtype, models.DO_NOTHING, db_column='FinancialTypeID', blank=True, null=True)  # Field name made lowercase.
    inventorytypeid = models.ForeignKey(JdInventorytype, models.DO_NOTHING, db_column='InventoryTypeID', blank=True, null=True)  # Field name made lowercase.
    customs_declaration_number = models.TextField(db_column='Customs Declaration Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    invoice_number = models.TextField(db_column='Invoice number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    pick_ticket_or_delivery_note_number_or_po_number = models.TextField(db_column='Pick Ticket or Delivery note Number or PO number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    mawb_hawb_bill_of_landing = models.TextField(db_column='MAWB / HAWB / Bill of Landing', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    supplier_name = models.TextField(db_column='Supplier Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    partnumber = models.ForeignKey('Partnumber', models.DO_NOTHING, db_column='PartNumber', blank=True, null=True)  # Field name made lowercase.
    invoice_quantity = models.IntegerField(db_column='Invoice Quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    unit_price = models.FloatField(db_column='Unit price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_package = models.IntegerField(db_column='Total package', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date_of_incident = models.IntegerField(db_column='Date of Incident', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    symptomdamageid = models.ForeignKey('JdSymptomdamage', models.DO_NOTHING, db_column='SymptomDamageID', blank=True, null=True)  # Field name made lowercase.
    other = models.IntegerField(db_column='OTHER', blank=True, null=True)  # Field name made lowercase.
    damage_quantity = models.IntegerField(db_column='Damage Quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    damageuomid = models.ForeignKey(InvoiceUom, models.DO_NOTHING, db_column='DamageUOMID', blank=True, null=True)  # Field name made lowercase.
    detail_of_damage = models.TextField(db_column='Detail of Damage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    requester_name = models.CharField(db_column='Requester Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    buyer_name = models.CharField(db_column='Buyer Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    picture_file = models.CharField(db_column='Picture_file', max_length=255, blank=True, null=True)  # Field name made lowercase.
    shipping_documents_file = models.CharField(db_column='Shipping Documents_file', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    submit_by = models.CharField(db_column='Submit by', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    submitdate = models.ForeignKey('WdFiscalweek', models.DO_NOTHING, db_column='SubmitDate', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    processing_time = models.DateTimeField(db_column='Processing time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'JD_Shipmentsdamagerecordform'


class JdSymptomdamage(models.Model):
    symptomdamageid = models.AutoField(db_column='SymptomDamageID', primary_key=True)  # Field name made lowercase.
    symptomdamage = models.TextField(db_column='SymptomDamage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_Symptomdamage'


class JdTransactionreviewtype(models.Model):
    transactionreviewtype = models.AutoField(db_column='TransactionReviewType', primary_key=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_TransactionReviewType'


class JdTransactionreview(models.Model):
    transactionreviewid = models.AutoField(db_column='TransactionReviewID', primary_key=True)  # Field name made lowercase.
    transaction_number = models.IntegerField(db_column='Transaction Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transactionreviewtype = models.IntegerField(db_column='TransactionReviewType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'JD_Transactionreview'


class JdConfirmationform(models.Model):
    incident_accident_action_confirmation_form_number = models.AutoField(db_column='Incident/Accident Action Confirmation Form number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    incident_accident_investigation_result_form_number = models.IntegerField(db_column='Incident/Accident Investigation Result Form number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    requester_buyer_s_disposition_result_form_number = models.IntegerField(db_column="Requester/Buyer's Disposition Result Form number", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sqe_inspection_form_number = models.IntegerField(db_column='SQE Inspection Form number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actionid = models.IntegerField(db_column='ActionID', blank=True, null=True)  # Field name made lowercase.
    action_remark = models.TextField(db_column='Action Remark', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    claimclassid = models.IntegerField(db_column='ClaimClassID', blank=True, null=True)  # Field name made lowercase.
    expected_settlement_amount = models.FloatField(db_column='Expected Settlement Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_by = models.CharField(db_column='Report by', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_date = models.DateField(db_column='Report Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'JD_confirmationform'


class JdDispositionresultform(models.Model):
    requester_buyer_s_disposition_result_form_number = models.AutoField(db_column="Requester/Buyer's Disposition Result Form number", primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    require_sqe_inspection_process_or_not_field = models.TextField(db_column='Require SQE inspection process or not?', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. This field type is a guess.
    sqe_name = models.CharField(db_column='SQE Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'JD_dispositionresultform'


class JdInvestigationresultform(models.Model):
    incident_accident_investigation_result_form_number = models.AutoField(db_column='Incident/Accident Investigation Result Form number', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_review_number = models.IntegerField(db_column='Transaction Review number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    vendor_supplier_fwd_name = models.TextField(db_column='Vendor / Supplier / FWD Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_email = models.CharField(db_column='Contact Email', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contact_number = models.IntegerField(db_column='Contact Number', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rootcause = models.TextField(db_column='Rootcause', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    corrective_action = models.TextField(db_column='Corrective Action', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    preventive_action = models.TextField(db_column='Preventive Action', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    number_8d_report_attachment_if_have_file = models.CharField(db_column='8D Report Attachment (If have)_file', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it wasn't a valid Python identifier.
    report_by = models.CharField(db_column='Report by', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_date = models.DateTimeField(db_column='Report Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'JD_investigationresultform'


class JdLanetype(models.Model):
    lanetypeid = models.AutoField(db_column='laneTypeID', primary_key=True)  # Field name made lowercase.
    lanetype = models.TextField(db_column='laneType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'JD_lanetype'


class OnejdAdminemail(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teeraphat_inta_wdc_com = models.CharField(db_column='teeraphat.inta@wdc.com', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ONEJD_Adminemail'


class OnejdAdminname(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teeraphat_inta = models.TextField(db_column='teeraphat inta', blank=True, null=True)  # Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ONEJD_Adminname'


class OnejdEmailuser(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teeraphat_inta_wdc_com = models.CharField(db_column='teeraphat.inta@wdc.com', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ONEJD_Emailuser'


class OnejdMasterTableAdmin(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_of_admin = models.IntegerField(db_column='Type of Admin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    user_name = models.IntegerField(db_column='User Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.IntegerField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    password = models.IntegerField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    user_group = models.IntegerField(db_column='User group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organization = models.IntegerField(db_column='Organization', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONEJD_Master table Admin'


class OnejdOrganization(models.Model):
    organizationid = models.CharField(db_column='OrganizationID', primary_key=True, max_length=255)  # Field name made lowercase.
    consigneename = models.TextField(db_column='Consigneename', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    consigneecountry = models.TextField(db_column='Consigneecountry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ONEJD_Organization'


class OnejdPasswordAdmin(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wellcome18 = models.TextField(db_column='Wellcome18', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONEJD_Password Admin'


class OnejdPassworduser(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    wellcome18 = models.CharField(db_column='Wellcome18', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONEJD_Passworduser'


class OnejdTypeOfAdmin(models.Model):
    type_of_admin = models.AutoField(db_column='Type of Admin', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_of_incident_field = models.IntegerField(db_column='Type of Incident ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    process_type_field = models.IntegerField(db_column='Process type ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'ONEJD_Type of Admin'


class OnejdTypeofincident(models.Model):
    type_of_incident = models.AutoField(db_column='Type of Incident', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    damage = models.TextField(db_column='Damage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    discrepancy = models.TextField(db_column='Discrepancy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ONEJD_Typeofincident'


class OnejdUsergroup(models.Model):
    user_group = models.AutoField(db_column='User group', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    prb_usage = models.TextField(db_column='PRB Usage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.
    bpi_usage = models.TextField(db_column='BPI Usage', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ONEJD_Usergroup'


class OnejdUsername(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teeraphat_inta = models.CharField(db_column='teeraphat inta', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'ONEJD_Username'


class OnejdLoginpage(models.Model):
    employee_id = models.AutoField(db_column='Employee ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    email = models.IntegerField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    password = models.IntegerField(db_column='Password', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ONEJD_loginpage'


class OnejdProcessType(models.Model):
    process_type = models.AutoField(db_column='process type', primary_key=True)  # Field renamed to remove unsuitable characters.
    add = models.TextField(db_column='Add', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    delete = models.TextField(db_column='Delete', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    normal = models.TextField(db_column='Normal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ONEJD_process type'


class Partnumber(models.Model):
    partnumber = models.CharField(db_column='PartNumber', primary_key=True, max_length=255)  # Field name made lowercase.
    partdescription = models.TextField(db_column='PartDescription', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commodity_type = models.TextField(db_column='Commodity_Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    part_group = models.TextField(db_column='Part_Group', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invoice_uom = models.TextField(db_column='Invoice_UOM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PartNumber'


class Partgroup(models.Model):
    part_groupid = models.AutoField(db_column='Part_GroupID', primary_key=True)  # Field name made lowercase.
    part_group = models.TextField(db_column='Part_Group', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Partgroup'


class TdAction(models.Model):
    actionid = models.AutoField(db_column='ActionID', primary_key=True)  # Field name made lowercase.
    action = models.TextField(db_column='Action', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TD_Action'


class TdArea(models.Model):
    areaid = models.AutoField(db_column='AreaID', primary_key=True)  # Field name made lowercase.
    area = models.TextField(db_column='Area', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TD_Area'


class TdCauseAction(models.Model):
    cause_actionid = models.AutoField(db_column='Cause&ActionID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    reviewid = models.IntegerField(db_column='ReviewID', blank=True, null=True)  # Field name made lowercase.
    rootcause = models.TextField(db_column='Rootcause', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    action_number = models.IntegerField(db_column='Action_Number', blank=True, null=True)  # Field name made lowercase.
    reference_documents = models.TextField(db_column='Reference documents', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_by = models.CharField(db_column='Report_by', max_length=255, blank=True, null=True)  # Field name made lowercase.
    report_date = models.DateField(db_column='Report_Date', blank=True, null=True)  # Field name made lowercase.
    processing_time = models.DateField(db_column='Processing_time', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TD_Cause&Action'


class TdDiscrepancyrecordform(models.Model):
    transaction_number = models.AutoField(db_column='Transaction_number', primary_key=True)  # Field name made lowercase.
    areaid = models.ForeignKey(TdArea, models.DO_NOTHING, db_column='AreaID', blank=True, null=True)  # Field name made lowercase.
    fightnumber = models.CharField(db_column='FightNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modeoftransportationid = models.ForeignKey(JdModeoftransportation, models.DO_NOTHING, db_column='ModeofTransportationID', blank=True, null=True)  # Field name made lowercase.
    forwarder = models.CharField(db_column='Forwarder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shippername = models.CharField(db_column='ShipperName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    shippercountry = models.CharField(db_column='ShipperCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customs_declaration_number = models.TextField(db_column='Customs_Declaration_Number', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invoice_number = models.TextField(db_column='Invoice_number', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickticketor = models.CharField(db_column='PickTicketor', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mawb_hawb_bill_of_landing = models.TextField(db_column='MAWB_HAWB_Bill_of_Landing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    suppliername = models.TextField(db_column='SupplierName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    partnumber = models.CharField(db_column='PartNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invoice_quantity = models.FloatField(db_column='Invoice Quantity', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    damageuomid = models.CharField(db_column='DamageUOMID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    unitprice_field = models.FloatField(db_column='Unitprice($)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_package = models.IntegerField(db_column='Total_package', blank=True, null=True)  # Field name made lowercase.
    dateofincident = models.DateField(db_column='DateofIncident', blank=True, null=True)  # Field name made lowercase.
    typeofdiscrepancyid = models.ForeignKey('TdTypeofdiscrepancy', models.DO_NOTHING, db_column='TypeofDiscrepancyID', blank=True, null=True)  # Field name made lowercase.
    detailofdiscrepancy = models.FileField(db_column='DetailofDiscrepancy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    shipping_documents_fie = models.FileField(db_column='Shipping_Documents_fie', blank=True, null=True)  # Field name made lowercase.
    other_file = models.TextField(blank=True, null=True)
    submitby = models.CharField(db_column='Submitby', max_length=50, blank=True, null=True)  # Field name made lowercase.
    submitdate = models.DateField(db_column='SubmitDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status1 = models.CharField(db_column='Status1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status2 = models.CharField(db_column='Status2', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TD_DiscrepancyRecordForm'


class TdSupervisorData(models.Model):
    cause_actionid = models.AutoField(db_column='Cause&ActionID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transaction_number = models.ForeignKey(TdDiscrepancyrecordform, models.DO_NOTHING, db_column='Transaction_number', blank=True, null=True)  # Field name made lowercase.
    reviewid = models.IntegerField(db_column='ReviewID', blank=True, null=True)  # Field name made lowercase.
    rootcause = models.TextField(db_column='Rootcause', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actionid = models.ForeignKey(TdAction, models.DO_NOTHING, db_column='ActionID', blank=True, null=True)  # Field name made lowercase.
    reference_documents = models.TextField(db_column='Reference documents', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    report_by = models.CharField(db_column='Report_by', max_length=255, blank=True, null=True)  # Field name made lowercase.
    report_date = models.DateField(db_column='Report_Date', blank=True, null=True)  # Field name made lowercase.
    processing_time = models.DateField(db_column='Processing_time', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TD_Supervisor-data'


class TdTransactionreview(models.Model):
    transactionreviewid = models.AutoField(db_column='TransactionReviewID', primary_key=True)  # Field name made lowercase.
    transactionreview = models.TextField(db_column='Transactionreview', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transaction_number = models.IntegerField(db_column='Transaction_number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TD_TransactionReview'


class TdTypeofdiscrepancy(models.Model):
    typeofdiscrepancyid = models.AutoField(db_column='TypeofDiscrepancyID', primary_key=True)  # Field name made lowercase.
    type_of_discrepancy = models.TextField(db_column='Type of Discrepancy', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TD_TypeofDiscrepancy'


class WdFiscalweek(models.Model):
    submitdate = models.DateField(db_column='SubmitDate', primary_key=True)  # Field name made lowercase.
    wd_fiscalweek = models.TextField(db_column='WD_Fiscalweek', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'WD_Fiscalweek'
