from edc_lab import LabProfile, RequisitionPanel
from edc_lab.site_labs import site_labs

from .aliquot_types import breast_milk, wb
from .processing_profiles import breast_milk_processing, cbc_processing
from .processing_profiles import cd4_processing, hematology_processing, \
    viral_load_processing

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

breast_milk_panel = RequisitionPanel(
    name='breast_milk',
    verbose_name='Breast Milk',
    aliquot_type=breast_milk,
    processing_profile=breast_milk_processing)

caregiver_lab_profile.add_panel(viral_load_panel)
caregiver_lab_profile.add_panel(cd4_panel)
caregiver_lab_profile.add_panel(hematology_panel)
caregiver_lab_profile.add_panel(cbc_panel)
caregiver_lab_profile.add_panel(breast_milk_panel)

site_labs.register(caregiver_lab_profile, )
