import rpy2.robjects as robjects

r_source = robjects.r["source"]
r_source("addthree.R")

addthree = robjects.r["addthree"]

import pyarrow

array = pyarrow.array((1, 2, 3))
print("PYTHON ARRAY", array)

from pyarrow.cffi import ffi as arrow_c

c_array = arrow_c.new("struct ArrowArray*")
c_array_ptr = int(arrow_c.cast("uintptr_t", c_array))
array._export_to_c(c_array_ptr)

c_schema = arrow_c.new("struct ArrowSchema*")
c_schema_ptr = int(arrow_c.cast("uintptr_t", c_schema))
array.type._export_to_c(c_schema_ptr)

x = addthree(str(c_array_ptr), str(c_schema_ptr))
print("AFTER R FUNCTION", x)
