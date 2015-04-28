from capstone_ext import *

# taken from capstone/binding/python/capstone/__init__.py

__all__ = [
    'Cs',
    'CsInsn',
#    'cs_disasm_quick',
#    'cs_disasm_lite',
#    'cs_version',
#    'cs_support',
#    'cs_disasm',
#    'version_bind',
#    'debug',

    'CS_API_MAJOR',
    'CS_API_MINOR',

    'CS_ARCH_ARM',
    'CS_ARCH_ARM64',
    'CS_ARCH_MIPS',
    'CS_ARCH_X86',
    'CS_ARCH_PPC',
    'CS_ARCH_SPARC',
    'CS_ARCH_SYSZ',
    'CS_ARCH_XCORE',
    'CS_ARCH_ALL',

    'CS_MODE_LITTLE_ENDIAN',
    'CS_MODE_BIG_ENDIAN',
    'CS_MODE_16',
    'CS_MODE_32',
    'CS_MODE_64',
    'CS_MODE_ARM',
    'CS_MODE_THUMB',
    'CS_MODE_MCLASS',
    'CS_MODE_MICRO',
    'CS_MODE_MIPS3',
    'CS_MODE_MIPS32R6',
    'CS_MODE_MIPSGP64',
    'CS_MODE_V8',
    'CS_MODE_V9',
    'CS_MODE_MIPS32',
    'CS_MODE_MIPS64',

    'CS_OPT_SYNTAX',
    'CS_OPT_SYNTAX_DEFAULT',
    'CS_OPT_SYNTAX_INTEL',
    'CS_OPT_SYNTAX_ATT',
    'CS_OPT_SYNTAX_NOREGNAME',

    'CS_OPT_DETAIL',
    'CS_OPT_MODE',
    'CS_OPT_ON',
    'CS_OPT_OFF',

    'CS_ERR_OK',
    'CS_ERR_MEM',
    'CS_ERR_ARCH',
    'CS_ERR_HANDLE',
    'CS_ERR_CSH',
    'CS_ERR_MODE',
    'CS_ERR_OPTION',
    'CS_ERR_DETAIL',
    'CS_ERR_VERSION',
    'CS_ERR_MEMSETUP',
    'CS_ERR_DIET',
    'CS_ERR_SKIPDATA',
    'CS_ERR_X86_ATT',
    'CS_ERR_X86_INTEL',

    'CS_SUPPORT_DIET',
    'CS_SUPPORT_X86_REDUCE',
#    'CS_SKIPDATA_CALLBACK',

    'CS_OP_INVALID',
    'CS_OP_REG',
    'CS_OP_IMM',
    'CS_OP_MEM',
    'CS_OP_FP',

    'CS_GRP_INVALID',
    'CS_GRP_JUMP',
    'CS_GRP_CALL',
    'CS_GRP_RET',
    'CS_GRP_INT',
    'CS_GRP_IRET',

#    'CsError',
]

# Capstone C interface

# API version
CS_API_MAJOR = 3
CS_API_MINOR = 0

# architectures
CS_ARCH_ARM = 0
CS_ARCH_ARM64 = 1
CS_ARCH_MIPS = 2
CS_ARCH_X86 = 3
CS_ARCH_PPC = 4
CS_ARCH_SPARC = 5
CS_ARCH_SYSZ = 6
CS_ARCH_XCORE = 7
CS_ARCH_MAX = 8
CS_ARCH_ALL = 0xFFFF

# disasm mode
CS_MODE_LITTLE_ENDIAN = 0      # little-endian mode (default mode)
CS_MODE_ARM = 0                # ARM mode
CS_MODE_16 = (1 << 1)          # 16-bit mode (for X86)
CS_MODE_32 = (1 << 2)          # 32-bit mode (for X86)
CS_MODE_64 = (1 << 3)          # 64-bit mode (for X86, PPC)
CS_MODE_THUMB = (1 << 4)       # ARM's Thumb mode, including Thumb-2
CS_MODE_MCLASS = (1 << 5)      # ARM's Cortex-M series
CS_MODE_V8 = (1 << 6)          # ARMv8 A32 encodings for ARM
CS_MODE_MICRO = (1 << 4)       # MicroMips mode (MIPS architecture)
CS_MODE_MIPS3 = (1 << 5)       # Mips III ISA
CS_MODE_MIPS32R6 = (1 << 6)    # Mips32r6 ISA
CS_MODE_MIPSGP64 = (1 << 7)    # General Purpose Registers are 64-bit wide (MIPS arch)
CS_MODE_V9 = (1 << 4)          # Sparc V9 mode (for Sparc)
CS_MODE_BIG_ENDIAN = (1 << 31) # big-endian mode
CS_MODE_MIPS32 = CS_MODE_32    # Mips32 ISA
CS_MODE_MIPS64 = CS_MODE_64    # Mips64 ISA

# Capstone option type
CS_OPT_SYNTAX = 1    # Intel X86 asm syntax (CS_ARCH_X86 arch)
CS_OPT_DETAIL = 2    # Break down instruction structure into details
CS_OPT_MODE = 3      # Change engine's mode at run-time
CS_OPT_MEM = 4       # Change engine's mode at run-time
CS_OPT_SKIPDATA = 5  # Skip data when disassembling
CS_OPT_SKIPDATA_SETUP = 6      # Setup user-defined function for SKIPDATA option

# Capstone option value
CS_OPT_OFF = 0             # Turn OFF an option - default option of CS_OPT_DETAIL
CS_OPT_ON = 3              # Turn ON an option (CS_OPT_DETAIL)

# Common instruction operand types - to be consistent across all architectures.
CS_OP_INVALID = 0
CS_OP_REG = 1
CS_OP_IMM = 2
CS_OP_MEM = 3
CS_OP_FP  = 4

# Common instruction groups - to be consistent across all architectures.
CS_GRP_INVALID = 0  # uninitialized/invalid group.
CS_GRP_JUMP    = 1  # all jump instructions (conditional+direct+indirect jumps)
CS_GRP_CALL    = 2  # all call instructions
CS_GRP_RET     = 3  # all return instructions
CS_GRP_INT     = 4  # all interrupt instructions (int+syscall)
CS_GRP_IRET    = 5  # all interrupt return instructions

# Capstone syntax value
CS_OPT_SYNTAX_DEFAULT = 0    # Default assembly syntax of all platforms (CS_OPT_SYNTAX)
CS_OPT_SYNTAX_INTEL = 1    # Intel X86 asm syntax - default syntax on X86 (CS_OPT_SYNTAX, CS_ARCH_X86)
CS_OPT_SYNTAX_ATT = 2      # ATT asm syntax (CS_OPT_SYNTAX, CS_ARCH_X86)
CS_OPT_SYNTAX_NOREGNAME = 3   # Asm syntax prints register name with only number - (CS_OPT_SYNTAX, CS_ARCH_PPC, CS_ARCH_ARM)

# Capstone error type
CS_ERR_OK = 0      # No error: everything was fine
CS_ERR_MEM = 1     # Out-Of-Memory error: cs_open(), cs_disasm()
CS_ERR_ARCH = 2    # Unsupported architecture: cs_open()
CS_ERR_HANDLE = 3  # Invalid handle: cs_op_count(), cs_op_index()
CS_ERR_CSH = 4     # Invalid csh argument: cs_close(), cs_errno(), cs_option()
CS_ERR_MODE = 5    # Invalid/unsupported mode: cs_open()
CS_ERR_OPTION = 6  # Invalid/unsupported option: cs_option()
CS_ERR_DETAIL = 7  # Invalid/unsupported option: cs_option()
CS_ERR_MEMSETUP = 8
CS_ERR_VERSION = 9 # Unsupported version (bindings)
CS_ERR_DIET = 10   # Information irrelevant in diet engine
CS_ERR_SKIPDATA = 11 # Access irrelevant data for "data" instruction in SKIPDATA mode
CS_ERR_X86_ATT = 12 # X86 AT&T syntax is unsupported (opt-out at compile time)
CS_ERR_X86_INTEL = 13 # X86 Intel syntax is unsupported (opt-out at compile time)

# query id for cs_support()
CS_SUPPORT_DIET = CS_ARCH_ALL + 1
CS_SUPPORT_X86_REDUCE = CS_ARCH_ALL+2
