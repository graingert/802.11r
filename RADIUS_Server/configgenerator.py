#!/usr/bin/env python

for i in range(1, 256):
    template = """client vpn {{
    ipaddr = 152.78.236.{number}
    secret = testing123

    nastype = other
}}
"""
    print template.format(number=i)
