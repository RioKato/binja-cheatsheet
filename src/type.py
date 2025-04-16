import binaryninja as bn
import rpyc

bv: bn.BinaryView = rpyc.connect('127.0.0.1', 8888)

# create new type
with bn.types.StructureBuilder.builder(bv, 'hoo') as hoo:
    hoo.append(bn.Type.int(4), 'test0')

# append field test1
with bn.types.Type.builder(bv, 'hoo') as hoo:
    hoo.append(bn.Type.int(4), 'test1')
