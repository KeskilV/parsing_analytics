__all__ = ['counts_s_in_j']

def counts_s_in_j(jewels:str,stones:str) -> int:
    '''
    функция возвращает количество камней в ЮИ учебная
    '''
    return sum([x in stones for x in jewels])