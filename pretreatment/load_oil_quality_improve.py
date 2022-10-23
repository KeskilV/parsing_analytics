import pandas as pd


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
        path = io.split('/')[:-1]
        filename = io.split('/')[-1].split('.')[:-1]
        fileexst = io.split('.')[-1]
        return ('/'.join(path), '.'.join(filename), fileexst)
    else:
        print(os.listdir())
        return ('_', '_', '_')


def check_columns(data, controlcolumns, ignore_extra=True):
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
    set_columns = set(controlcolumns)
    if ignore_extra:
        return set_columns.issubset(set_data_columns)
    else:
        return set_columns == set_data_columns


def firstclear(df:pd.DataFrame) -> pd.DataFrame:
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