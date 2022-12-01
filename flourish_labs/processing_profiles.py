from edc_lab import Process, ProcessingProfile

from .aliquot_types import wb, pl, bc, dna_pcr, ss, pbmc, rs, serum, lithium_heparin

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

child_plasma_processing = ProcessingProfile(
    name='plasma_store', aliquot_type=wb)
pl_plasma_process = Process(aliquot_type=pl, aliquot_count=4)
pbmc_plasma_process = Process(aliquot_type=pbmc, aliquot_count=4)
child_plasma_processing.add_processes(
    pl_plasma_process, pbmc_plasma_process)

glucose_processing = ProcessingProfile(name='glucose', aliquot_type=wb)
glucose_pl_process = Process(aliquot_type=pl, aliquot_count=3)
glucose_processing.add_processes(glucose_pl_process)

insulin_processing = ProcessingProfile(name='insulin', aliquot_type=wb)

chemistry_processing = ProcessingProfile(name='chemistry', aliquot_type=wb)

lead_processing = ProcessingProfile(name='lead_levels', aliquot_type=wb)

fbc_processing = ProcessingProfile(name='fbc', aliquot_type=wb)

infant_serum_processing = ProcessingProfile(name='serum', aliquot_type=wb)
infant_serum_process = Process(aliquot_type=serum, aliquot_count=1)
infant_serum_processing.add_processes(infant_serum_process)


lithium_heparin_processing = ProcessingProfile(name='lithium_heparin', aliquot_type=wb)
lithium_heparin_process = Process(aliquot_type=lithium_heparin, aliquot_count=1)
lithium_heparin_processing.add_processes(lithium_heparin_process)
