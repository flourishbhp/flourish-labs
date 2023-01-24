from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import dna_pcr, ss, wb, rs
from .processing_profiles import chemistry_processing, lead_processing, fbc_processing
from .processing_profiles import dna_pcr_processing, stool_sample_processing
from .processing_profiles import glucose_processing, insulin_processing
from .processing_profiles import infant_plasma_cykotines_processing, rectal_swab_processing
from .processing_profiles import infant_serum_processing, child_plasma_processing, lithium_heparin_processing

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

chemistry_panel = RequisitionPanel(
    name='chemistry',
    verbose_name='Chemistry',
    aliquot_type=wb,
    processing_profile=chemistry_processing)

lead_panel = RequisitionPanel(
    name='lead_level',
    verbose_name='Lead',
    aliquot_type=wb,
    processing_profile=lead_processing)

fbc_panel = RequisitionPanel(
    name='fbc',
    verbose_name='FBC',
    aliquot_type=wb,
    processing_profile=fbc_processing)

serum_panel = RequisitionPanel(
    name='serum_storage',
    verbose_name='Infant Serum (Store Only)',
    aliquot_type=wb,
    processing_profile=infant_serum_processing)

child_pl_store_panel = RequisitionPanel(
    name='child_pl_store',
    verbose_name='Plasma Storage',
    aliquot_type=wb,
    processing_profile=child_plasma_processing)

lithium_heparin_panel = RequisitionPanel(
    name='lithium_heparin',
    verbose_name='QuantiFERON Requisition Form',
    aliquot_type=wb,
    processing_profile=lithium_heparin_processing
)

child_lab_profile.add_panel(dna_pcr_panel)
child_lab_profile.add_panel(stool_sample_panel)
child_lab_profile.add_panel(infant_pl_cytokines_panel)
child_lab_profile.add_panel(rectal_swab_panel)
child_lab_profile.add_panel(fasting_glucose_panel)
child_lab_profile.add_panel(fasting_insulin_panel)
child_lab_profile.add_panel(chemistry_panel)
child_lab_profile.add_panel(lead_panel)
child_lab_profile.add_panel(fbc_panel)
child_lab_profile.add_panel(serum_panel)
child_lab_profile.add_panel(child_pl_store_panel)
child_lab_profile.add_panel(lithium_heparin_panel)

site_labs.register(child_lab_profile,)
