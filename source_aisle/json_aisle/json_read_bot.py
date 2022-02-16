import json

def json_hash_val(str_cvt: str)->dict:
    #each val len is 19 and key len is 1
    """returns the hash vals from json file created for hashing purposes
    Arguments:
    str_cvt[str]: the string that should be hashed using unique hash algo
    
    Returns:
        dict: containing hashvals a dict
    """
    with open(r'json_stuff\unique_hash.json', 'r') as jammer:
        main = json.loads(jammer.read())
        real_ans = ''.join(list(map(lambda x: main[x], str_cvt)))
    return real_ans




if __name__=='__main__':
    pass