
# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testNotaTriangle(self):
        self.assertEqual(classifyTriangle(2,3,6), 'NotATriangle')
        self.assertEqual(classifyTriangle(7,3,1), 'NotATriangle')
        self.assertEqual(classifyTriangle(13,2,37), 'NotATriangle')
        self.assertEqual(classifyTriangle(23,-12,12), 'InvalidInput')
        self.assertEqual(classifyTriangle(0,12,12), 'InvalidInput')
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(5,4,3),'Right','5,4,3 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testIsocelosTriangle(self):
        self.assertEqual(classifyTriangle(2,2,4), 'Isoceles','2,2,4 should be isocelus')
        self.assertEqual(classifyTriangle(2,4,4), 'Isoceles','2,4,4 should be isocelus')
        self.assertEqual(classifyTriangle(5,2,5), 'Isoceles','5,2,5 should be isocelus')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene','3,4,8 should be scalene')

    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

