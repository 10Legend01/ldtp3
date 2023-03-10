#!/usr/bin/env python3
"""
LDTP v3 Core.

@author: Mikhail Nazarov <mihailnazarov01@mail.ru>
@copyright: Copyright (c) 2022 Mikhail Nazarov
@license: LGPL

http://ldtp.freedesktop.org

This file may be distributed and/or modified under the terms of the GNU Lesser General
Public License version 2 as published by the Free Software Foundation. This file
is distributed without any warranty; without even the implied warranty of 
merchantability or fitness for a particular purpose.

See 'COPYING' in the source distribution for more information.

Headers in this file shall remain intact.
"""

from setuptools import setup

setup(name="ldtp",
      version="4.0.0",
      description="Linux Desktop Testing Project Version 3",
      maintainer="Mikhail Nazarov",
      maintainer_email="mihailnazarov01@mail.ru",
      license="GNU Lesser General Public License (LGPL)",
      install_requires=["twisted"],
      packages=["ldtp", "ldtpd", "ooldtp", "ldtputils", "ldtpme"],
      long_description="Linux Desktop Testing Project is aimed at producing " \
          "high quality cross platform GUI test automation framework and cutting-edge tools that " \
          "can be used to test GNU/Linux/Windows/Mac Desktop and improve it. It uses the " \
          "Accessibility libraries to poke through the applications user " \
          "interface. LDTP is a Linux / Unix GUI application testing tool. " \
          "It runs on Linux / Windows / Mac OSX / Solaris / FreeBSD / Embedded environment (Palm Source).",
      scripts=["scripts/ldtp"],
      classifiers=[
        "Development Status :: 5 - Production",
        "Environment :: X11 Applications :: GTK",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Solaris",
        "Operating System :: POSIX :: FreeBSD",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Topic :: Desktop Environment",
        ],
      )
