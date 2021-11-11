library(arrow)
library(reticulate)

a <- Array$create(c(1, 2, 3))

pc <- import("pyarrow.compute")

result <- pc$add(a, 3)

print(result)
