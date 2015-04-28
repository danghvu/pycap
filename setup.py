from distutils.core import setup, Extension

setup(
    name = 'CapstoneC',
    version = '1.0',
    description = 'This is a native binding for capstone',
    packages = ['capstone'],
    ext_modules = [
        Extension(
            'capstone_ext',
            ['src/pycap.c', 'src/cs.c', 'src/cs_insn.c'],
            include_dirs=['/usr/include', './include'],
            libraries=['capstone']
        )
    ]
)
