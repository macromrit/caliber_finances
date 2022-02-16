import random
###########################################################################################
#connect path via sys as root directory differs
import sys
# insert at 1
sys.path.insert(1, '/python_pgms/mysql_project_class12_new/source_aisle/db_managment')
import validative
###########################################################################################

#retrieving data for unique_id noveltation
x = validative.MainDb('MainStructure')
vals = x.display_dat('user_main')
x.close_db()

###########################################################################################
def gen_random()->str:
    while True:
        ints=list('1234567890')
        strs=list('abcdefghijklmnopqrstuvwxyz')
        spcl_chrs = list('!@#$%&')
        main_ans = ''
        for i in range(3):
            main_ans+=random.choice(ints)
        for i in range(3): 
            main_ans+=random.choice(spcl_chrs)
        for i in range(4):
            main_ans+=random.choice(strs)

        main_ans = list(main_ans)
        random.shuffle(main_ans)
        main_ans=''.join(main_ans)
        if main_ans in list(map(lambda x:x[4], vals)): pass
        else: break
    return main_ans



###########################################################################################
if __name__=='__main__':
    pass