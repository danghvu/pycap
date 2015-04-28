# pycap
Yet another Python binding for capstone.

#### Why ?
The current binding is using ctypes and Cython, this is an attempt to use the
Python native API extensions.

#### Status ?
Version alpha, only for testing purpose.

#### Features ?

7x faster than ctypes, 20% faster than Cython.

#### TODO

- [x] cs_disasm
- [x] cs_disasm_lite
- [ ] cs_detail
- [ ] cs_option
- [ ] test_suite
