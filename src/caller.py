from rpyc import connect
import binaryninja


bv: binaryninja.BinaryView = connect('localhost', 8888).root.bv

for f in bv.functions:
    for caller in f.caller_sites:
        match caller.mlil:
            case binaryninja.MediumLevelILCall(params=[binaryninja.MediumLevelILConstPtr(), *_]):
                const = caller.mlil.params[0]
                print(hex(caller.address), const)
