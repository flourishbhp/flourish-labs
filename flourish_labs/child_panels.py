from edc_lab import RequisitionPanel, LabProfile
from .processing_profiles import dna_pcr_processing, stool_sample_processing
from .aliquot_types import dna_pcr, ss
from edc_lab.site_labs import site_labs

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



child_lab_profile.add_panel(dna_pcr_panel)
child_lab_profile.add_panel(stool_sample_panel)

site_labs.register(child_lab_profile,)
