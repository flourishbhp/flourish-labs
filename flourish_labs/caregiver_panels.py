from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import wb
from .processing_profiles import cbc_processing
from .processing_profiles import viral_load_processing, cd4_processing, hematology_processing

caregiver_lab_profile = LabProfile(
    name='flourish_caregiver_lab_profile',
    requisition_model='flourish_caregiver.caregiverrequisition')

viral_load_panel = RequisitionPanel(
    name='viral_load',
    verbose_name='Viral Load',
    aliquot_type=wb,
    processing_profile=viral_load_processing)

cd4_panel = RequisitionPanel(
    name='cd4',
    verbose_name='CD4',
    aliquot_type=wb,
    processing_profile=cd4_processing)

hematology_panel = RequisitionPanel(
    name='hematology',
    verbose_name='Hematology',
    aliquot_type=wb,
    processing_profile=hematology_processing)

cbc_panel = RequisitionPanel(
    name='complete_blood_count',
    verbose_name='Complete Blood Count',
    aliquot_type=wb,
    processing_profile=cbc_processing)

caregiver_lab_profile.add_panel(viral_load_panel)
caregiver_lab_profile.add_panel(cd4_panel)
caregiver_lab_profile.add_panel(hematology_panel)
caregiver_lab_profile.add_panel(cbc_panel)

site_labs.register(caregiver_lab_profile, )
