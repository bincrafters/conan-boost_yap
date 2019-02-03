#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostConvertConan(base.BoostBaseConan):
    name = "boost_yap"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_yap"
    lib_short_names = ["yap"]
    header_only_libs = ["yap"]
    b2_requires = [
        "boost_hana",
        "boost_preprocessor",
        "boost_type_index"
    ]
