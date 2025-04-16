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


__pyx_string_tab: int = 0x00036540
define_string_tab(__pyx_string_tab)
