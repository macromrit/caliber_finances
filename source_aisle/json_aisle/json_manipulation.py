# import json
# import random
# #obcures
# nums_obc = list('1234567890')
# alpha_low = list('abcdefghijklmnopqrstuvwxyz')
# alpha_up = list('abcdefghijklmnopqrstuvwxyz'.upper())
# special_chrs_in = list('~`!@#$%^&*()_-+=/?.>,<\'"\\')
# total_val = nums_obc+alpha_low+alpha_up+special_chrs_in

# #--------------------------gens 
# special_chrs = list('!@#$%&?><')


# with open(r'json_stuff\unique_hash.json', 'w') as jammer:
#     main_keys = dict()
    
#     for key in total_val: 
#         gen_code = ''
#         cnt = 0
#         while True:
#             if len(gen_code)<10:
#                 i=random.choice(special_chrs)
#                 gen_code+=i
                
#             else: 
#                 if e in maigen_codn_keys.values():
#                     gen_code=''
#                 else: 
#                     main_keys[key]='-'.join(gen_code)
#                     break
#             cnt+=1
        
#     jammer.write(json.dumps(main_keys, indent=4,sort_keys=True,))

# if __name__=='__main__':
#     pass