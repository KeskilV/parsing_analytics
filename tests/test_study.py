import unittest


from study import *

class Test_study_counts_s_in_j(unittest.TestCase):
    def test_counts(self):
        test_data = list([('aabbccd', 'ab', 4)])
        test_data.append(('dfgfsdhfhsd', 'df', 6))
        test_data.append(('', 'ffhfg', 0))
        test_data.append(('aaaa', 'a', 4))
        self.assertEqual(all(counts_s_in_j(*td[:-1]) == td[-1] for td in test_data),
                         True)

if __name__ == '__main__':
    unittest.main()
    #print(counts_s_in_j('aabbccd', 'ab'))
