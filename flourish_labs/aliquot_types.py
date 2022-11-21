from edc_lab import AliquotType

pl = AliquotType(name='Plasma', alpha_code='PL', numeric_code='32')

bc = AliquotType(name='Buffy Coat', alpha_code='BC', numeric_code='16')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')

ss = AliquotType(name='Stool Sample', alpha_code='SS', numeric_code='46')

dna_pcr = AliquotType(name='DNA PCR', alpha_code='DP', numeric_code='50')

pbmc = AliquotType(name='PBMC', alpha_code='PBMC', numeric_code='31')

rs = AliquotType(name='Rectal Swab', alpha_code='RS', numeric_code='61')

serum = AliquotType(name='Serum', alpha_code='SERUM', numeric_code='06')

wb.add_derivatives(bc, pl, wb, pbmc, serum)
