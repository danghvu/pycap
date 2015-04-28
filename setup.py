from distutils.core import setup, Extension

setup(
    name = 'CapstoneC',
    version = '1.0',
    description = 'This is a native binding for capstone',
    packages = ['capstone'],
    ext_modules = [
        Extension('capstone_ext', ['capstone.c'], include_dirs=['/usr/include'],
        libraries=['capstone'])
    ]
)
