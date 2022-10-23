import pandas as pd

from pretreatment import *


import unittest
import pandas as pd

class Test_oil_qiality_improve(unittest.TestCase):
    #choosefile('results/SL_всеЮИ2022-09-01-15-28/_joined-2022-09-09-10-18.xlsx')
#('results/SL_всеЮИ2022-09-01-15-28', '_joined-2022-09-09-10-18', 'xlsx')
#('_', '_', '_')
    def test_choosefile_v0(self):
        self.assertEqual(choosefile('results/SL_всеЮИ2022-09-01-15-28/_joined-2022-09-09-10-18.xlsx')
                         ,('results/SL_всеЮИ2022-09-01-15-28', '_joined-2022-09-09-10-18', 'xlsx'))
    
    def test_choosefile_todo(self):
        self.assertEqual(choosefile()
                         ,('_', '_', '_'))
    
    def test_firstclear(self):
        data = pd.read_excel('data/_joined-2022-09-09-10-18-Copy1.xlsx')
        deleted = firstclear(data)
        self.assertEqual((len(data),len(deleted)), (35647,8))
    
    
    def test_len(self):
        data = pd.read_excel('data/_joined-2022-09-09-10-18-Copy1.xlsx')
        self.assertEqual(len(data), 35655)
    
    def test_checkcolumns_v2(self):
        data = pd.read_excel('data/_joined-2022-09-09-10-18-Copy1.xlsx').head()
        controlcolumns = {'art', 'd0', 'd1', 'filname', 'gems', 'gems2', 'gold',
 'gold2', 'h1', 'price', 'price2', 'source', 'url', 'weight'}
        self.assertEqual(check_columns(data, controlcolumns), True)
        
    def test_checkcolumns_v1(self):
        data = pd.read_excel('data/_joined-2022-09-09-10-18-Copy1.xlsx').head()
        controlcolumns = {'art', 'extracol', 'd0', 'd1', 'filname', 'gems', 'gems2', 'gold',
 'gold2', 'h1', 'price', 'price2', 'source', 'url', 'weight'}
        self.assertEqual(check_columns(data, controlcolumns), False)
        
    def test_checkcolumns_v3(self):
        data = pd.read_excel('data/_joined-2022-09-09-10-18-Copy1.xlsx').head()
        controlcolumns = {'art', 'd0', 'd1', 'filname', 'gems', 'gems2', 'gold',
 'gold2', 'h1', 'price', 'price2', 'source', 'url', 'weight'}
        self.assertEqual(check_columns(data, controlcolumns, ignore_extra=False), False)


if __name__ == '__main__':
    unittest.main()


'''
#feature for ipynb
res = unittest.main(argv=[''], verbosity=3, exit=False)

# if we want our notebook to stop processing due to failures, we need a cell itself to fail
assert len(res.result.failures) == 0
'''