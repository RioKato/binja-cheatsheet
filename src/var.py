from rpyc import connect
import binaryninja

bv: binaryninja.BinaryView = connect('localhost', 8888).root.bv

var = bv.get_data_var_at(0x00fd338)
typ = bv.get_type_by_name('struct_2')

if var.type.name == 'struct_2':
    field_0 = var['field_0'].value
    print(field_0)

field_0_p = bv.read_pointer(0x00fd338)
assert (field_0 == field_0_p)
print(field_0_p)
