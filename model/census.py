#!/usr/bin/env python
# encoding: utf-8
"""
census.py

Created by Orestes Sanchez on 2012-03-07.
Copyright (c) 2012 Telefónica I+D. All rights reserved.
"""

import sys
import os
import unittest



class Census:
    def __init__(self, domain, address_seq ):
        self.domain = domain
        self.address_seq = address_seq
        self.census = {}
        for a in self.address_seq:
            user = AnonymousUser( a, self.domain)
            self.census[ user.id ] = user
        pass
        
    def verify( self, uuid ):
        return 


class CensusTests(unittest.TestCase):
    def setUp(self):
        self.emails = [ "first@first.com", "second@second.com", "third@third.com"]
        self.domain = "domain.com"
        pass
        
    def test_domain( self ):
        emptySeq = []
        c = Census( self.domain, emptySeq )
        self.assertEqual( c.domain, self.domain )
        self.assertSequenceEqual( c.address_seq, emptySeq )
        pass

    def test_emails( self ):
        c = Census( self.domain, self.emails )
        self.assertEqual( c.domain, self.domain )
        self.assertSequenceEqual( c.address_seq, self.emails )
        pass


if __name__ == '__main__':
    unittest.main()