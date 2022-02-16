import validative

import sys
sys.path.insert(1, '\python_pgms\mysql_project_class12_new\source_aisle\json_aisle')
import json_read_bot

def man_authentication(unique_code: str, passcode: str)->bool:
    try: 
        x = validative.MainDb('MainStructure')
        vals = x.display_dat('user_main')
        x.close_db()
        main_ans = list(map(lambda x: x, filter(lambda x: True if unique_code in x else False, vals)))
        if json_read_bot.json_hash_val(passcode)==main_ans[0][10]: return True, main_ans
        else: return False
    except: return False



if __name__=='__main__':
    pass