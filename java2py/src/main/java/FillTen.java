import org.apache.arrow.c.ArrowArray;
import org.apache.arrow.c.ArrowSchema;
import org.apache.arrow.c.Data;
import org.apache.arrow.memory.RootAllocator;
import org.apache.arrow.vector.FieldVector;
import org.apache.arrow.vector.BigIntVector;
import org.apache.arrow.vector.ValueVector;


public class FillTen {
    public static void fillCArray(long c_array_ptr, long c_schema_ptr) {
        ArrowArray arrow_array = ArrowArray.wrap(c_array_ptr);
        ArrowSchema arrow_schema = ArrowSchema.wrap(c_schema_ptr);

        RootAllocator allocator = new RootAllocator();
        FieldVector v = Data.importVector(allocator, arrow_array, arrow_schema, null);
        FillTen.fillValueVector(v);
    }

    public static void fillValueVector(ValueVector v) {
        BigIntVector iv = (BigIntVector)v;
        iv.setSafe(0, 1);
        iv.setSafe(1, 2);
        iv.setSafe(2, 3);
        iv.setSafe(3, 4);
        iv.setSafe(4, 5);
        iv.setSafe(5, 6);
        iv.setSafe(6, 7);
        iv.setSafe(7, 8);
        iv.setSafe(8, 9);
        iv.setSafe(9, 10);
    }
}
