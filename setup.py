# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name='dmsl',
    version='0.4',
    author='Daniel Skinner',
    author_email='daniel@dasa.cc',
    url='http://dmsl.dasa.cc',
    license = "MIT License",
    packages = ["dmsl"],
    requires = ["cython"],
    description='da Markup Language featuring html outlining via css-selectors, embedded python, and extensibility.',
    long_description = """\
Features CSS selectors and indention for declaring page layout. Embed
python in your documents such as functions, lambda's, variable declarations,
for loops, list comprehensions, etc, writing it just as you would normally.

Follow development at http://github.com/dasacc22/dmsl
    """,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Environment :: Web Environment",
        ],
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ Extension("dmsl.cdoc", ["dmsl/cdoc.pyx"]),
                    Extension("dmsl.cutils", ["dmsl/cutils.pyx"]),
                    Extension("dmsl.cfmt", ["dmsl/cfmt.pyx"])]
    )
