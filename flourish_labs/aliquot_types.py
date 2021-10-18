from edc_lab import AliquotType

pl = AliquotType(name='Plasma', alpha_code='PL', numeric_code='32')

bc = AliquotType(name='Buffy Coat', alpha_code='BC', numeric_code='16')

wb = AliquotType(name='Whole Blood', alpha_code='WB', numeric_code='02')

wb.add_derivatives(bc, pl, wb)
