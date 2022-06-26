from edc_lab import RequisitionPanel, LabProfile
from edc_lab.site_labs import site_labs

from .aliquot_types import dna_pcr, ss, wb, rs
from .processing_profiles import dna_pcr_processing, stool_sample_processing
from .processing_profiles import infant_plasma_cykotines_processing, rectal_swab_processing

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

child_lab_profile.add_panel(dna_pcr_panel)
child_lab_profile.add_panel(stool_sample_panel)
child_lab_profile.add_panel(infant_pl_cytokines_panel)
child_lab_profile.add_panel(rectal_swab_panel)

site_labs.register(child_lab_profile,)
