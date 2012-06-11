#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Juhani Numminen <juhaninumminen0@gmail.com>
# License: GNU GPL v3+

from distutils.core import setup

setup(name="langtools",
        version="0.1",
        author="Juhani Numminen",
        author_email="juhaninumminen0@gmail.com",
        url="https://github.com/jnumm/langtools",
        description="Natural language tools library",
        long_description=open("README.rst").read(),
        classifiers=[
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Text Processing :: Linguistic",
        ],
        platforms=["OS Independent"],
        license="GPLv3+",
        packages=["langtools"],
        )
