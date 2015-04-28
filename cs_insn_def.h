#ifndef CS_INSN_DEF_H_
#define CS_INSN_DEF_H_

typedef struct {
  PyObject_HEAD
  cs_insn insn_;
} CsInsn;

static int CsInsn_init(CsInsn *self, PyObject *args, PyObject *kwds)
{
  return 0;
}

static void CsInsn_dealloc(CsInsn *self)
{
}

static PyMethodDef CsInsn_methods[] = {
  { NULL },
};

#define OFFSET(f) (offsetof(CsInsn, insn_) + offsetof(cs_insn, f))

static PyMemberDef CsInsn_members[] = {
  {"id", T_UINT, OFFSET(id), 0, "id"},
  {"address", T_ULONG, OFFSET(address), 0, "address"},
  {"size", T_USHORT, OFFSET(size), 0, "size"},
  { NULL },
};

static PyObject * CsInsn_byte_get(PyObject *self, void* data) {
  return Py_BuildValue("s", ((CsInsn*) self)->insn_.bytes);
}

static PyObject * CsInsn_mnemonic_get(PyObject *self, void* data) {
  return Py_BuildValue("s", ((CsInsn*) self)->insn_.mnemonic);
}

static PyObject * CsInsn_opstr_get(PyObject *self, void* data) {
  return Py_BuildValue("s", ((CsInsn*) self)->insn_.op_str);
}

static PyGetSetDef CsInsn_getset[] = {
  {"bytes", CsInsn_byte_get, 0, "bytes", 0},
  {"mnemonic", CsInsn_mnemonic_get, 0, "mnemonic", 0},
  {"op_str", CsInsn_opstr_get, 0, "op_str", 0},
  { NULL },
};

static PyTypeObject CsInsnType = {
  PyObject_HEAD_INIT(NULL)
  0,                         /* ob_size */
  "CsInsn",               /* tp_name */
  sizeof(CsInsn),         /* tp_basicsize */
  0,                         /* tp_itemsize */
  (destructor)CsInsn_dealloc, /* tp_dealloc */
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
  "CsInsn object",        /* tp_doc */
  0,                         /* tp_traverse */
  0,                         /* tp_clear */
  0,                         /* tp_richcompare */
  0,                         /* tp_weaklistoffset */
  0,                         /* tp_iter */
  0,                         /* tp_iternext */
  CsInsn_methods,         /* tp_methods */
  CsInsn_members,         /* tp_members */
  CsInsn_getset,                         /* tp_getset */
  0,                         /* tp_base */
  0,                         /* tp_dict */
  0,                         /* tp_descr_get */
  0,                         /* tp_descr_set */
  0,                         /* tp_dictoffset */
  (initproc)CsInsn_init,  /* tp_init */
  0,                         /* tp_alloc */
  PyType_GenericNew,                         /* tp_new */
};

#endif
