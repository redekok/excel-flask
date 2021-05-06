# https://github.com/vallettea/koala/issues/241
from app.helpers.koala.koala.ExcelCompiler import ExcelCompiler
from app.helpers.koala.koala.Spreadsheet import Spreadsheet

# from openpyxl import load_workbook

# def load_workbook():
#     return load_workbook(filename = 'engine.xlsx')
#
# def set_range(wb, min, max):
#     wb['input']['C2'] = min
#     wb['input']['C3'] = max
#
# def get_result(wb):
#     return wb['output']['C2']
#
# def random(min, max):
#     wb = load_workbook()
#     set_range(wb, min, max)
#
#     # TODO: compile excel
#
#     return get_result(wb)

def compile_random(min, max):
    """
    Note: apparently, it is possible to define names in Excel and use those
    freely with Koala, e.g.

    sp.cell_set_value('myNamedCell', 0)
    """
    sp = Spreadsheet('engine.xlsx')
    sp.cell_set_value('input!C2', min)
    sp.cell_set_value('input!C3', max)
    return sp.cell_evaluate('output!C2')
