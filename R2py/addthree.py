import rpy2.robjects as robjects

r_source = robjects.r["source"]
r_source("addthree.R")

addthree = robjects.r["addthree"]

import pyarrow

array = pyarrow.array((1, 2, 3))
print("PYTHON ARRAY", array)

from pyarrow.cffi import ffi as arrow_c

with arrow_c.new("struct ArrowArray*") as c_array, \
     arrow_c.new("struct ArrowSchema*") as c_schema:
    c_array_ptr = int(arrow_c.cast("uintptr_t", c_array))
    c_schema_ptr = int(arrow_c.cast("uintptr_t", c_schema))

    array._export_to_c(c_array_ptr)
    array.type._export_to_c(c_schema_ptr)

    r_result = addthree(str(c_array_ptr), str(c_schema_ptr))
    r_result["export_to_c"](float(c_array_ptr), float(c_schema_ptr))

    py_result = pyarrow.Array._import_from_c(c_array_ptr, c_schema_ptr)
    print("RESULT", py_result)
