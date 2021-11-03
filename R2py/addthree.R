library(arrow)

addthree <- function(array_ptr_s, schema_ptr_s) {
  array_ptr <- as.numeric(array_ptr_s)
  schema_ptr <- as.numeric(schema_ptr_s)

  a <- Array$import_from_c(array_ptr, schema_ptr)

  return(a + 3)
}

