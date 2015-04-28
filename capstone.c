#define PY_SSIZE_T_CLEAN

#include "Python.h"
#include "structmember.h"

#include <capstone/capstone.h>

#include "cs_insn_def.h"
#include "cs_def.h"

void initcapstone_ext(void)
{
  PyObject *mod;
  mod = Py_InitModule3("capstone_ext", module_methods, "Test capstone ext");
  if (mod == NULL) {
    return;
  }

  if (PyType_Ready(&CsInsnType) < 0) {
    return;
  }

  if (PyType_Ready(&CsType) < 0) {
    return;
  }

  Py_INCREF(&CsInsnType);
  PyModule_AddObject(mod, "CsInsn", (PyObject*)&CsInsnType);

  Py_INCREF(&CsType);
  PyModule_AddObject(mod, "Cs", (PyObject*)&CsType);
}
