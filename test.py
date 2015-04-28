from capstone import *
import cPickle, pickle

import pickle

md = Cs(CS_ARCH_X86, CS_MODE_64)

CODE = "\x55\x48\x8b\x05\xb8\x13\x00\x00"

for c in md.disasm(CODE, 0x1000):
    print("0x%x:\t%s\t%s" % (c.address, c.mnemonic, c.op_str))


