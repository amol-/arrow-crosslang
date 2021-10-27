import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM(classpath=["./dependencies/*", "./target/*"])

FillTen = JClass('FillTen')


import pyarrow as pa

array = pa.array([0]*10)



from pyarrow.cffi import ffi as arrow_c

c_array = arrow_c.new("struct ArrowArray*")
c_array_ptr = int(arrow_c.cast("uintptr_t", c_array))
array._export_to_c(c_array_ptr)

c_schema = arrow_c.new("struct ArrowSchema*")
c_schema_ptr = int(arrow_c.cast("uintptr_t", c_schema))
array.type._export_to_c(c_schema_ptr)

FillTen.fillCArray(c_array_ptr, c_schema_ptr)

print("ARRAY", array)
