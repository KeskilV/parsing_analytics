import pandas as pd
#readme 
def choosefile(io=None):
    '''
    v22-10-13
    Signature:
        choosefile(
        io = None )
        ) -> Tuple[path:str,filename:str,exstention:str]
    Docstring:
        Предлагает папки и файлы - возвращает путь, имя файла без расширения и расширение, 
        если в параметре указан io то не предлагает, а раскладывает указанный io
    Parameters
    ----------
    io : str, bytes, ExcelFile, xlrd.Book, path object, or file-like object
    Any valid string path is acceptable. The string could be a URL. Valid
    URL schemes include http, ftp, s3, and file. For file URLs, a host is
    expected. A local file could be: ``file://localhost/path/to/table.xlsx``.
    '''
    import os
    if io:
        path =  io.split('/')[:-1]
        filename = io.split('/')[-1].split('.')[:-1]
        fileexst = io.split('.')[-1]
        return ('/'.join(path),'.'.join(filename),fileexst)
    else:
        print(os.listdir())
        return ('_','_','_')
    
def check_columns(data, controlcolumns, ignore_extra = True):
    '''
    v22-10-12
    Signature:
        check_columns(
        data: 'DataFrame',
        controlcolumns: 'list-like'
        ignore_extra = True
        ) -> 'bool'
    Docstring:
        Проверяет соответствие столбцов в обрабатываемом файле, 
        по умолчанию игнорирует избыточные столбцы
    Parametrs
    ---------
        data: DataFrame
        controlcolumns: 'list-like'
            должны содержаться эти столбцы
        ignore_extra: bool, default True
            игнорирует избыточные столбцы
    Returns
    -------
        True|False
    '''
    set_data_columns = set(data.columns)
    set_columns = set (controlcolumns)
    if ignore_extra:
        return set_columns.issubset(set_data_columns)
    else:
        return set_columns == set_data_columns
    

def firstclear(df):
    '''
    v22-10-12
    Signature:
        first_clear(
        df: 'DataFrame',
        ) -> 'DataFrame'
    Docstring:
        Удаляет неинформативные данные с пустой ценой с df, возвращает удаленные в виде 
        DataFrame
    Parametrs
    ---------
        df: DataFrame
    
    Returns
    -------
        DataFrame
    '''
    deleted = df[df['price'].isna()]
    df.dropna(subset=['price'], inplace=True)
    return deleted

#Tests
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