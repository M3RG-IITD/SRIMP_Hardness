def make_hill(chemicals):
    
    '''
    Function for converting chemical formula to hill notation
    takes input as a list. For example, 
    >> chemicals =['Al2O3']
    >> make_hill(chemicals)
    Output: ['Al$_2$O$_3$']
    '''
    
    hill_all = []
    for col in chemicals:
        hill = ''
        for ele in col:
            if ele in ['2','3','4','5','6','7','8','9','10','11','12','13']:
                hill = hill + '$_' + ele + '$'
            else:
                hill = hill + ele
#         print(hill)
        hill_all.append(hill)
    return hill_all
