from edc_lab import Process, ProcessingProfile

from .aliquot_types import wb, pl, bc, dna_pcr, ss, pbmc, rs

viral_load_processing = ProcessingProfile(name='viral_load', aliquot_type=wb)
vl_pl_process = Process(aliquot_type=pl, aliquot_count=3)
vl_bc_process = Process(aliquot_type=bc, aliquot_count=1)
viral_load_processing.add_processes(vl_pl_process, vl_bc_process)

hematology_processing = ProcessingProfile(name='hematology', aliquot_type=wb)

cbc_processing = ProcessingProfile(name='complete_blood_count', aliquot_type=wb)

cd4_processing = ProcessingProfile(name='CD4', aliquot_type=wb)

dna_pcr_processing = ProcessingProfile(name='dna_pcr', aliquot_type=dna_pcr)

stool_sample_processing = ProcessingProfile(name='stool_sample', aliquot_type=ss)

rectal_swab_processing = ProcessingProfile(name='rectal_swab', aliquot_type=rs)

infant_plasma_cykotines_processing = ProcessingProfile(
    name='plasma_cykotines_store', aliquot_type=wb)
pl_plasma_process = Process(aliquot_type=pl, aliquot_count=4)
pbmc_plasma_process = Process(aliquot_type=pbmc, aliquot_count=4)

glucose_processing = ProcessingProfile(name='glucose', aliquot_type=wb)
glucose_pl_process = Process(aliquot_type=pl, aliquot_count=3)
glucose_processing.add_processes(glucose_pl_process)

insulin_processing = ProcessingProfile(name='insulin', aliquot_type=wb)

lipids_processing = ProcessingProfile(name='lipids', aliquot_type=wb)

lead_processing = ProcessingProfile(name='lead_levels', aliquot_type=wb)

anemia_processing = ProcessingProfile(name='anemia', aliquot_type=wb)
