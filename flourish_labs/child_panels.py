from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import dna_pcr, ss, wb, rs
from .processing_profiles import dna_pcr_processing, stool_sample_processing
from .processing_profiles import glucose_processing, insulin_processing
from .processing_profiles import infant_plasma_cykotines_processing, rectal_swab_processing
from .processing_profiles import lipids_processing, lead_processing, anemia_processing

child_lab_profile = LabProfile(
    name='flourish_child_lab_profile',
    requisition_model='flourish_child.childrequisition'
)

dna_pcr_panel = RequisitionPanel(
    name='dna_pcr',
    verbose_name='DNA PCR',
    aliquot_type=dna_pcr,
    processing_profile=dna_pcr_processing)

stool_sample_panel = RequisitionPanel(
    name='stool_sample',
    verbose_name='Stool Sample',
    aliquot_type=ss,
    processing_profile=stool_sample_processing)

infant_pl_cytokines_panel = RequisitionPanel(
    name='infant_pl_cytokines',
    verbose_name='Plasma Cytokines',
    aliquot_type=wb,
    processing_profile=infant_plasma_cykotines_processing)

rectal_swab_panel = RequisitionPanel(
    name='rectal_swab',
    verbose_name='Rectal Swab',
    aliquot_type=rs,
    processing_profile=rectal_swab_processing)

fasting_glucose_panel = RequisitionPanel(
    name='fasting_glucose',
    verbose_name='Fasting Glucose',
    aliquot_type=wb,
    processing_profile=glucose_processing)

fasting_insulin_panel = RequisitionPanel(
    name='fasting_insulin',
    verbose_name='Fasting Insulin',
    aliquot_type=wb,
    processing_profile=insulin_processing)

fasting_lipids_panel = RequisitionPanel(
    name='fasting_lipids',
    verbose_name='Fasting Lipids',
    aliquot_type=wb,
    processing_profile=lipids_processing)

lead_panel = RequisitionPanel(
    name='lead_level',
    verbose_name='Lead Levels',
    aliquot_type=wb,
    processing_profile=lead_processing)

anemia_panel = RequisitionPanel(
    name='anemia_testing',
    verbose_name='Anemia Testing (FBC)',
    aliquot_type=wb,
    processing_profile=anemia_processing)

child_lab_profile.add_panel(dna_pcr_panel)
child_lab_profile.add_panel(stool_sample_panel)
child_lab_profile.add_panel(infant_pl_cytokines_panel)
child_lab_profile.add_panel(rectal_swab_panel)
child_lab_profile.add_panel(fasting_glucose_panel)
child_lab_profile.add_panel(fasting_insulin_panel)
child_lab_profile.add_panel(fasting_lipids_panel)
child_lab_profile.add_panel(lead_panel)
child_lab_profile.add_panel(anemia_panel)

site_labs.register(child_lab_profile,)
