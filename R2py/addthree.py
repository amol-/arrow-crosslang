import rpy2.robjects as robjects
from rpy2_arrow.pyarrow_rarrow import rarrow_to_py_array, converter as arrowconverter
from rpy2.robjects.conversion import localconverter

r_source = robjects.r["source"]
r_source("addthree.R")

addthree = robjects.r["addthree"]

import pyarrow

array = pyarrow.array((1, 2, 3))
print("PYTHON ARRAY", array)

with localconverter(arrowconverter):
    r_result = addthree(array)

py_result = rarrow_to_py_array(r_result)
print("RESULT", type(py_result), py_result)
