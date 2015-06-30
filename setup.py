#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


version = '1.0'


class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None
        self.pytest_args = ['--cov', 'turnstile', '--cov-report', 'term-missing', '--doctest-modules', 'turnstile']

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='turnstile-codevalidator',
    packages=find_packages(),
    version=version,
    description='Turnstile-Codevalidator - Codevalidator check and command for turnstile',
    author='Zalando SE',
    url='https://github.com/zalando/turnstile-codevalidator',
    license='Apache License Version 2.0',
    install_requires=['click', 'GitPython', 'codevalidator', 'turnstile-core>=2.1.0'],
    tests_require=['pytest-cov', 'pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Version Control',
    ],
    long_description=open('README.rst').read(),
    entry_points={'turnstile.commands': ['codevalidator = turnstile_codevalidator.command'],
                  'turnstile.pre_commit': ['codevalidator = turnstile_codevalidator.check']}
)
