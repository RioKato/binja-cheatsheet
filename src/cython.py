import binaryninja
import itertools
import re

# bv: binaryninja.BinaryView = None

__Pyx_StringTabEntry: binaryninja.Type = bv.types['__Pyx_StringTabEntry']
assert (__Pyx_StringTabEntry)


def define_string_tab(string_tab_start: int):
    sizeof_Pyx_StringTabEntry = len(__Pyx_StringTabEntry)
    string_tab_end = 0

    for i in itertools.count(string_tab_start, sizeof_Pyx_StringTabEntry):
        data = bv.read(i, sizeof_Pyx_StringTabEntry)

        if not any(data):
            string_tab_end = i
            break

    n = (string_tab_end - string_tab_start) // len(__Pyx_StringTabEntry)
    var = bv.data_vars[string_tab_start]
    var.type = binaryninja.Type.array(__Pyx_StringTabEntry, n)

    for v in var:
        s = v['s']

        if name := bv.get_ascii_string_at(s.value):
            s = bv.define_user_data_var(s.value, binaryninja.Type.array(binaryninja.Type.char(), len(name)))
            name = re.sub('[^0-9A-Za-z_]+', '_', name.value)
            p = v['p']
            p = bv.define_user_data_var(p.value, p.type.target)
            s.name = f'__pyx_n_s_{name}'
            p.name = f'__pyx_k_{name}'


ImportModule: binaryninja.Function = bv.get_functions_by_name('ImportModule')[0]


def serch_import_module():
    for cs in ImportModule.caller_sites:
        if mlil := cs.mlil:
            ssa = mlil.ssa_form

            if ssa.params and isinstance(ssa.params[0], binaryninja.MediumLevelILVarSsa):
                mlilssa_set = cs.function.mlil.ssa_form.get_ssa_var_definition(ssa.params[0])

                match mlilssa_set:
                    case binaryninja.MediumLevelILSetVarSsa(src=binaryninja.MediumLevelILLoadSsa(src=binaryninja.MediumLevelILConstPtr(constant=addr))):
                        print(hex(addr))


__pyx_string_tab: int = 0x00036540
define_string_tab(__pyx_string_tab)
serch_import_module()
