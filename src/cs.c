#include "pycap.h"

int Cs_init(Cs *self, PyObject *args, PyObject *kwds)
{
  cs_arch arch;
  cs_mode mode;
  csh handle;

  if (self != NULL) {
    if (!PyArg_ParseTuple(args, "II", &arch, &mode))
      return -1;

    if (cs_open(arch, mode, &handle) != CS_ERR_OK)
      return -1;

    self->handle = handle;
  }
  return 0;
}

void Cs_dealloc(Cs* self)
{
  cs_close(&self->handle);
  self->ob_type->tp_free((PyObject*)self);
}

extern PyTypeObject CsInsnType;

PyObject * Cs_disasm(PyObject *self, PyObject *args)
{
  const char* buffer;
  Py_ssize_t addr, buflen;
  cs_insn *insn;
  size_t count;
  PyListObject *list;

  list = (PyListObject *) Py_BuildValue("[]");

  if (!PyArg_ParseTuple(args, "s#n", &buffer, &buflen, &addr))
    return (PyObject*) list;

  count = cs_disasm(((Cs *)self)->handle, (const uint8_t*) buffer, buflen, addr, 0, &insn);

  size_t j;
  for (j = 0; j < count; j++) {
    CsInsn *py_insn = NULL;
    py_insn = PyObject_New(CsInsn, &CsInsnType);
    memcpy((char*) py_insn + offsetof(CsInsn, insn_), &insn[j], sizeof(cs_insn));
    PyList_Append((PyObject*) list, (PyObject*) py_insn);
  }
  return (PyObject*) list;
}

PyMethodDef Cs_methods[] = {
  {"disasm", (PyCFunction) Cs_disasm, METH_VARARGS, "disassemble"},
  { NULL },
};

PyTypeObject CsType = {
  PyObject_HEAD_INIT(NULL)
    0,                         /* ob_size */
  "Cs",               /* tp_name */
  sizeof(Cs),         /* tp_basicsize */
  0,                         /* tp_itemsize */
  (destructor)Cs_dealloc, /* tp_dealloc */
  0,                         /* tp_print */
  0,                         /* tp_getattr */
  0,                         /* tp_setattr */
  0,                         /* tp_compare */
  0,                         /* tp_repr */
  0,                         /* tp_as_number */
  0,                         /* tp_as_sequence */
  0,                         /* tp_as_mapping */
  0,                         /* tp_hash */
  0,                         /* tp_call */
  0,                         /* tp_str */
  0,                         /* tp_getattro */
  0,                         /* tp_setattro */
  0,                         /* tp_as_buffer */
  Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags*/
  "Cs object",        /* tp_doc */
  0,                         /* tp_traverse */
  0,                         /* tp_clear */
  0,                         /* tp_richcompare */
  0,                         /* tp_weaklistoffset */
  0,                         /* tp_iter */
  0,                         /* tp_iternext */
  Cs_methods,         /* tp_methods */
  0,         /* tp_members */
  0,                         /* tp_getset */
  0,                         /* tp_base */
  0,                         /* tp_dict */
  0,                         /* tp_descr_get */
  0,                         /* tp_descr_set */
  0,                         /* tp_dictoffset */
  (initproc)Cs_init,  /* tp_init */
  0,                         /* tp_alloc */
  PyType_GenericNew,                         /* tp_new */
};


