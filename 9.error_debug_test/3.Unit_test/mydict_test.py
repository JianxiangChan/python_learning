# -*- coding: utf-8 -*-

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    
    def setUp(self):    #每个case开始前调用
        print('setUp')  #每个case结束时调用
    
    def tearDown(self):
        print('tearDown')
    
    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d,dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')
    
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError): #use of with
            value = d['empty']
    
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    
if __name__ == '__main__':
    unittest.main()
    