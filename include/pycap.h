#ifndef PYCAP_H_
#define PYCAP_H_

#define PY_SSIZE_T_CLEAN

#include "Python.h"
#include "structmember.h"

#include <capstone/capstone.h>

typedef struct {
    PyObject_HEAD csh handle;
} Cs;

typedef struct {
    PyObject_HEAD cs_insn insn_;
} CsInsn;

#endif
