from edc_lab import AliquotType

pl = AliquotType(name='Plasma', alpha_code='PL', numeric_code='32')

bc = AliquotType(name='Buffy Coat', alpha_code='BC', numeric_code='16')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')

wb.add_derivatives(bc, pl, wb)

# TODO : Change numeric code and alpha-code if necessary
ss = AliquotType(name='Stool Sample', alpha_code='SS', numeric_code='01')

dna_pcr = AliquotType(name='DNA PCR', alpha_code='DP', numeric_code='50')

