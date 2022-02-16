#importin stuffs required
from datetime import datetime
from source_aisle.cod_gen_bot_aisle import otp_gen_bot as send_otp, unique_code_gen as pecu_id
from source_aisle.db_managment import validative as db_mani, man_vald as man_user_validation
from source_aisle.email_aisle import send_mail as mailup
from source_aisle.input_aisle import inputs as enterup
from source_aisle.qr_code_aisle import qr_gen_bot as make_qr, qr_recognizer_bot as read_qr
from source_aisle.user_codes import sample_outs as outputs
from source_aisle.json_aisle import json_read_bot as hashpas
from source_aisle.db_managment import csv_int as csvmaker
from getpass import getpass
from source_aisle.usr_shrs import users
from os import remove
#------------------------------------------>
#mail csv
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import yagmail

def acc_post_email(reciever_email: str, 
                   usdid: str): 
    right_from = 'amritsubramanian.c@gmail.com'
    act_receiver = reciever_email
    titly = outputs.Email_head_Title
    filename = F'csv_history_aisle\\{usdid}.csv'
    
    mrit = yagmail.SMTP(right_from, 'amma@@1953')
    mrit.send(
        to=act_receiver,
        subject=titly,
        contents='Your transactional history upto now has been written to the csv file pinged down:',
        attachments=filename
    )
    print('History has been mailed successfully!!')

#----------------------------------------->
def withdraw_funds(amount, id_m): 
    
    withdraw_db = db_mani.MainDb('MainStructure')
    det = list(filter(lambda x: True if id_m[4] in x else False,withdraw_db.display_dat('user_main')))[0]
    # print(id_m)
    # for i in withdraw_db.display_dat('user_main'): 
    #     if 'o!0$49lbk$' in i: print(i)

    if amount<det[8] and amount<=100001 and det:
        min_balance = det[8]-amount-1
        #updating db
        withdraw_db.upd_data('user_main', 'balance', min_balance, 'n', det[4])
        withdraw_db.insert_dat(1,str(datetime.now()), tablename='bankrevenue')
        withdraw_db.insert_dat(det[4], str(datetime.now()), amount, 'd', tablename='transactions')
        
        

        # print(outputs.user_debition.format(det[0], det[4], amount, 1, min_balance, str(datetime.now())))
        
        csvmaker.csv_input('d', amount, str(datetime.now()), min_balance, id_m[4])
        
        #sending email
        mailup.send_for_mail(det[6], outputs.Email_head_Title, outputs.suc_emailandres_debition+'\n'+outputs.user_debition.format(det[0], det[4], amount, 1, min_balance, str(datetime.now())))
        
        #printing output
        print(outputs.suc_emailandres_debition+'\n'+outputs.user_debition.format(det[0], det[4], amount, 1, min_balance, str(datetime.now())))
    else:
        print(outputs.unsuc_emailandres_debition)
        print('Insufficient balance/withdrawal limit exceeded')
        mailup.send_for_mail(det[6], outputs.Email_head_Title, outputs.unsuc_emailandres_debition)
    withdraw_db.close_db()
    print()
    


def deposit_funds(amount, id_m): 
    amnt = amount
    print()
    deposit_db = db_mani.MainDb('MainStructure')
    det = list(filter(lambda x: True if id_m[4] in x else False, deposit_db.display_dat('user_main')))[0]
    
    if 1<amnt and det:
        min_balance = det[8]+amnt-1
        #updating Balance
        deposit_db.upd_data('user_main', 'balance', min_balance, 'n', det[4])
        deposit_db.insert_dat(1,str(datetime.now()), tablename='bankrevenue')
        deposit_db.insert_dat(det[4], str(datetime.now()), amnt-1, 'c',tablename='transactions')

        
        csvmaker.csv_input('c', amount, str(datetime.now()), min_balance, id_m[4])
        
        #sending email
        mailup.send_for_mail(det[6], outputs.Email_head_Title, outputs.suc_emailandres_credition+'\n'+outputs.User_credition.format(det[0], det[4], amnt, 1, min_balance, str(datetime.now())))
        #printing output
        print( outputs.suc_emailandres_credition+'\n'+outputs.User_credition.format(det[0], det[4], amnt, 1, min_balance, str(datetime.now())))
        
    else:
        print(outputs.unsuc_emailandres_credition)
        print('Insufficient balance/withdrawal limit exceeded')
        mailup.send_for_mail(det[6], outputs.Email_head_Title, outputs.unsuc_emailandres_credition)
    deposit_db.close_db()
    print()


def transfer_funds(senders_id, receivers_id, amount): 
    #1$ should be deducted from the funds tranfered totaly from sender to recivers 100[debited]->99[credited]
    transferal = db_mani.MainDb('Mainstructure')
    amnt = amount
    print()
    det = list(filter(lambda x: True if senders_id[4] in x else False, transferal.display_dat('user_main')))[0]
    rec = list(filter(lambda x: True if receivers_id in x else False, transferal.display_dat('user_main')))[0]
    
    if amnt<=det[8] and det and receivers_id in rec:
        #reducing
        min_balance = det[8]-amnt
        #updating Balance
        transferal.upd_data('user_main', 'balance', min_balance, 'n', det[4])
        transferal.insert_dat(1,str(datetime.now()), tablename='bankrevenue')
        #maximising
        max_balance = rec[8]+amnt-1
        #updating Balance
        transferal.upd_data('user_main', 'balance', max_balance, 'n', rec[4])
        transferal.insert_dat(det[4], str(datetime.now()), amnt, 'd',tablename='transactions')
        transferal.insert_dat(rec[4], str(datetime.now()), amnt-1, 'c',tablename='transactions')
        
        #printing output
        print(outputs.suc_emailandres_transcation)
        print(outputs.User_Transaction_info.format(det[0], det[6], det[4],str(datetime.now()),rec[0], rec[6], rec[4], amnt, min_balance))
        
        csvmaker.csv_input('c', amnt, str(datetime.now()), max_balance, receivers_id)
        
        csvmaker.csv_input('d', amnt, str(datetime.now()), min_balance, senders_id[4])
        
        #sending email sender
        mailup.send_for_mail(det[6], outputs.Email_head_Title, outputs.suc_emailandres_transcation+'\n'+outputs.User_Transaction_info.format(det[0], det[6], det[4],str(datetime.now()),rec[0], rec[6], rec[4], amnt, min_balance))
        
        #sending email receiver
        mailup.send_for_mail(rec[6], outputs.Email_head_Title, outputs.suc_emailandres_transcation+'\n'+outputs.User_Transaction_info.format(det[0], det[6], det[4],str(datetime.now()),rec[0], det[6], rec[4], amnt, max_balance))
        # print(outputs.suc_emailandres_transcation+'\n'+outputs.User_Transaction_info.format(det[0], det[6], det[4],str(datetime.now()),rec[0], rec[6], rec[4], amnt, max_balance))
        
    else:
        print(outputs.unsuc_emailandres_transcation)
        print('Insufficient balance or no such user found')
        mailup.send_for_mail(det[6], outputs.Email_head_Title, outputs.unsuc_emailandres_transcation)
    print()
    transferal.close_db()
    
#------------------------------------------>

print('CALIBER FINANCES - <Indian unicorn-Fin-tech> | WELCOMES YOU!!\n')
while True:
    print(outputs.menu_1)
    while True:
        try:
            main_key = input('(enter your choice)-> ')
            break
        except: print('\nTry again... Enter valid input\n')
        
    if main_key=='1':#signup
        
        #name validation
        #usr_name
        while True:
            try:
                usr_name = enterup.name_in(input('Enter your name: '))
            except: print('\nTry again with valid input\n')
            else:
                print()
                if usr_name[1]: 
                    usr_name = usr_name[0]
                    break
                else: print(usr_name[0])
                print()
            finally: pass
            
        
        #GENDER
        #gender
        while True:
            try: 
                gender = enterup.gender_in(input('Enter your gender: '))
            except: print('\nTry again with valid input\n')
            else:
                print()
                if gender[1]: 
                    gender = gender[0]
                    break
                else: print(gender[0])
                print()
            finally: pass
            
        
        #D-O-B
        #dob
        while True:
            try:
                dob = enterup.dob_in(input('Enter your DOB(dd-mm-yyyy): '))
            except: print('\nTry again with valid input\n')
            else:
                brk_real = False
                print()
                if dob[1]:
                    dob = dob[0]
                    break
                else: 
                    if dob[0][0]=='t':
                        print(dob[0])
                        print('program terminating..')
                        brk_real = True
                        break
                    else: print(dob[0])
                print()
            finally: pass
            
        if brk_real: break
        else: pass
        
        
        #Nationality 
        #nationality
        while True:
            try:
                nationality = enterup.nationality_in(input('Enter your Nationality(IND/USA): '))
            except: print('\nTry again with valid input\n')
            else:
                print()
                if nationality[1]:
                    nationality = nationality[0]
                    break
                else:
                    print(nationality[0])
                print()
            finally: pass
        
        
        #Phone_n0
        #phone_no
        while True:
            try: 
                phone_no = enterup.phone_no_in(input('Enter your phone-number(10-11 digits): '))
            except: print('\nTry again with valid input\n')
            else:
                print()
                if phone_no[1]:
                    phone_no = phone_no[0]
                    break
                else: 
                    print(phone_no[0])
                print()
            finally: pass
        
        
        #password
        #password
        while True:
            try:
                password_1 = enterup.pass_in(getpass(prompt='Set Password: '))
                password_2 = getpass(prompt='Confirm Password: ')
            except: print('\nTry again with valid input\n')
            else:
                print()
                if password_1[1]:
                    if password_1[0]==password_2:
                        password = hashpas.json_hash_val(password_1[0])
                        break
                    else: print("passwords didn't match! Try again")
                else: 
                    print(password_1[0])
                print()
            finally: pass    
        
        #pincode
        #pincode
        while True:
            try:
                pincode = enterup.pincode_in(getpass(prompt='Set pincode: '))
                pincode_2 = getpass(prompt='Confirm pincode: ')
            except: print('\nTry again with valid input\n')
            else:
                print()
                if pincode[1]:
                    if pincode_2==pincode[0]:
                        pincode = pincode[0]
                        break
                    else: print("pin's didn't match! Try again")
                else: 
                    print(pincode[0])
                print()
            finally: pass
        
        #Email
        #email
        while True:
            brky = False
            #retrievin email from db
            email_collection = db_mani.MainDb('MainStructure')
            paras = email_collection.display_dat('user_main')
            #6
            paras = list(map(lambda x: x[6], paras))
            email_collection.close_db()
            try:
                email = enterup.email_in(input('Enter your E-Mail: '))
                if email[1]:
                    if email[0] in paras:
                        print('\nEmail has been sacked already...Try a new one\n')
                    else:
                        otp_generated = send_otp.gen_otp()
                        mailup.send_for_mail(email[0], outputs.otp_verification, F'your otp-> {otp_generated}')
                        print()
                        read_otp = input('enter the otp mailed: ')
                        print()
                        if otp_generated==read_otp:
                            email = email[0]
                            break
                        else: 
                            print("otp didn't match! Try again.")
                            resend = input('resend otp(y/n): ')
                            if resend == 'n':
                                brky = True
                                break
                            else: brky = False
                            print()
                else:  print('\nTry again with valid email\n')
                        
            except:  print('\nTry again with valid input\n')
            else: pass
            finally: pass
        
        if brky:
            print('program terminating...')
            break
        
        unique_id = pecu_id.gen_random()
        
        created_span = str(datetime.now())
        
        balance = .0
        
        #qrcode_making
        maxy = make_qr.gen_qr_code(unique_id, F'usr_qr_codes\\{unique_id}.jpg')
        
        #writtin into db
        main_wrt = db_mani.MainDb('MainStructure')
        x = main_wrt.insert_dat(usr_name, gender, dob, nationality, unique_id, phone_no, email, created_span, balance, pincode,password, tablename='user_main')
        main_wrt.close_db()
        csvmaker.initialize_user(unique_id)
        
        #writtin success
        if x: 
            print(outputs.signup_pass)
            z = outputs.User_created_email_info.format(usr_name, unique_id, balance, created_span, email, gender, phone_no, nationality, dob)
            print(z)
            mailup.send_for_mail(email, outputs.Email_head_Title, z, F'usr_qr_codes\\{unique_id}.jpg')
        
        else: print(outputs.signup_fail)
        print(outputs.splitter)
        
#----------------------------------------------------------------------------->>>
    elif main_key=='2': #Login qr_code
        main = read_qr.qr_reader()
        datas = db_mani.MainDb('MainStructure')
        try:
            main = list(filter(lambda x: True if main in x else False,datas.display_dat('user_main')))[0]
        except: print('user not found!!')
        else:
            if main: 
                #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                while True:
                    print('--------------------------------------------')
                    print(F'Logged in as {main[0]}--->')
                    print('--------------------------------------------')
                    print(outputs.menu_Login)
                    
                    while True:
                        try:
                            decision = input('(enter your choice)-> ')
                            break
                        except: print('Try Again.. Enter valid input')
                
                    if decision=='1': 
                        iny = True
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: pass
                            else: iny=False
                        except: 
                            iny = False
                            print('invalid input.. Try Again...')
                        if iny:
                            try:
                                amounty = float(input('Enter amount to be withdrawn: '))
                                withdraw_funds(amounty, main)#amnt, id        
                            except: print('invalid input.. Try Again...')
                        else: print('pincode didn\'t match...')
                        
                        
                    elif decision=='2': 
                        iny = True
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: pass
                            else: iny=False
                        except: 
                            iny = False
                            print('invalid input.. Try Again...')
                            
                        if iny:
                            try:
                                amounto = float(input('Enter amount to be deposited: '))
                                deposit_funds(amounto, main)#amnt, id        
                            except: print('invalid input.. Try Again...')
                        else: print('pincode didn\'t match...')
                        
                        
                    elif decision=='3': 
                        iny = True
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: pass
                            else: iny=False
                        except: 
                            iny = False
                            print('invalid input.. Try Again..')
                        if iny:
                            try:
                                amounti = float(input('Enter amount to be transferred: '))
                                rec_id = (input('Enter receiver\'s id: '))
                                transfer_funds(main, rec_id, amounti)#amnt, id
                            except: print('invalid input... No such user found.. Try Again...')
                        else: print('pincode didn\'t match...')
                    
                    elif decision=='4': #change pin
                        
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: 
                                pinnew = enterup.pincode_in(getpass('Enter your new pin: '))
                                pinnewconfirm = getpass('Enter your new pin: ')
                                if pinnew and pinnewconfirm==pinnew[0]:
                                    datas.upd_data('user_main', 'pincode', pinnew[0], 's', main[4])       
                                    print('pincode updated successfully...Login again...')
                                    print(outputs.splitter)
                                    break
                                else:
                                    print('Process Failed... Invalid pin entered or pincodes didn\'t match')
                        except: 
                            print('invalid input.. Try Again..')
                            
                            
                    elif decision=='5': #change password
                        
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: 
                                passcode = getpass('Enter password: ')
                                if hashpas.json_hash_val(passcode) == main[10]:
                                    enter1 = enterup.pass_in(getpass('Enter new password: '))
                                    if enter1[1]:
                                        enter2 = getpass('Enter new password: ')
                                        if enter2==enter1[0]:
                                            datas.upd_data('user_main', 'password_hash', hashpas.json_hash_val(enter2), 's', main[4])       
                                            print('password updated successfully...Login again...')
                                            print(outputs.splitter)
                                            break
                                        else: print('passwords didn\'t match.. Try again')
                                    else: print('invalid password.. Try again')
                                        
                                else:print('invalid password.. Try again')
                            else:print('invalid pin.. Try again')
                                        
                                
                        except: 
                            print('invalid input.. Try Again..')
                    
                    elif decision=='6': #email history
                        acc_post_email(main[6], main[4])
                        
                    elif decision=='7': #acnt info
                        balancy = list(filter(lambda x: True if x[4]==main[4] else False,db_mani.MainDb('Mainstructure').display_dat('user_main')))
                        balancy = balancy[0][8]
                        print(F'''
------------------------------
User's Info                  |
------------------------------
User name: {main[0]}
User id: {main[4]}
User balance: ${balancy}
account created on: {main[7]}
User's email id: {main[6]}
------------------------------
        ''')
                    
                    elif decision=='8': 
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                        except:
                            print('Invalid input. Try again!')
                        else:
                            if pin==main[9]:
                                print('pin matched')
                                dece = input('Do you want to delete this account(y/n): ').casefold()
                                if dece=='y':
                                    buby = db_mani.MainDb('MainStructure')
                                    buby.del_data('user_main', main[4])
                                    #------------------------------------
                                    remove(F'usr_qr_codes\\{main[4]}.jpg')
                                    remove(F'csv_history_aisle\\{main[4]}.csv')
                                    #------------------------------------
                                    print('Account deleted successfully!!')
                                    buby.close_db()
                                    
                                    break   
                                else: print('deletion process was aborted')
                            else: print('pincode didn\'t match')
                    
                    
                    elif decision=='9': 
                        print('Logging out...')
                        break
                    
                    else: print('Invalid input... Try again with a valid one.')
                    
                    print(outputs.splitter)
                    
                #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
                #usr pin = main[9]
            else: 
                print('No such user found! Try again.')
            datas.close_db()
#----------------------------------------------------------------------------->>> 
    elif main_key=='3':#manual login
        try:
            main = man_user_validation.man_authentication(input('Enter usr id: '), getpass(prompt='Enter password: '))
            print()
            datas = db_mani.MainDb('MainStructure')
            into = True
        except: into = False
        if into:
            if main:              
                main = main[1][0]
                #------------------------------------------------------------------------------------>
                while True:
                    print('--------------------------------------------')
                    print(F'Logged in as {main[0]}--->')
                    print('--------------------------------------------')
                    print(outputs.menu_Login)
                    
                    while True:
                        try:
                            decision = input('(enter your choice)-> ')
                            break
                        except: print('Try Again.. Enter valid input')
                
                    if decision=='1': 
                        iny = True
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: pass
                            else: iny=False
                        except: 
                            iny = False
                            print('invalid input.. Try Again...')
                        if iny:
                            try:
                                amounty = float(input('Enter amount to be withdrawn: '))
                                withdraw_funds(amounty, main)#amnt, id        
                            except: print('invalid input.. Try Again...')
                        else: print('pincode didn\'t match...')
                        
                        
                    elif decision=='2': 
                        iny = True
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: pass
                            else: iny=False
                        except: 
                            iny = False
                            print('invalid input.. Try Again...')
                            
                        if iny:
                            try:
                                amounto = float(input('Enter amount to be deposited: '))
                                deposit_funds(amounto, main)#amnt, id        
                            except: print('invalid input.. Try Again...')
                        else: print('pincode didn\'t match...')
                        
                        
                    elif decision=='3': 
                        iny = True
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: pass
                            else: iny=False
                        except: 
                            iny = False
                            print('invalid input.. Try Again..')
                        if iny:
                            try:
                                amounti = float(input('Enter amount to be transferred: '))
                                rec_id = (input('Enter receiver\'s id: '))
                                transfer_funds(main, rec_id, amounti)#amnt, id
                            except: print('invalid input... No such user found.. Try Again...')
                        else: print('pincode didn\'t match...')
                    
                    elif decision=='4': #change pin
                        
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: 
                                pinnew = enterup.pincode_in(getpass('Enter your new pin: '))
                                pinnewconfirm = getpass('Enter your new pin: ')
                                if pinnew and pinnewconfirm==pinnew[0]:
                                    datas.upd_data('user_main', 'pincode', pinnew[0], 's', main[4])       
                                    print('pincode updated successfully...Login again...')
                                    print(outputs.splitter)
                                    break
                                else:
                                    print('Process Failed... Invalid pin entered or pincodes didn\'t match')
                        except: 
                            print('invalid input.. Try Again..')
                            
                            
                    elif decision=='5': #change password
                        
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                            if pin==main[9]: 
                                passcode = getpass('Enter password: ')
                                if hashpas.json_hash_val(passcode) == main[10]:
                                    enter1 = enterup.pass_in(getpass('Enter new password: '))
                                    if enter1[1]:
                                        enter2 = getpass('Enter new password: ')
                                        if enter2==enter1[0]:
                                            datas.upd_data('user_main', 'password_hash', hashpas.json_hash_val(enter2), 's', main[4])       
                                            print('password updated successfully...Login again...')
                                            print(outputs.splitter)
                                            break
                                        else: print('passwords didn\'t match.. Try again')
                                    else: print('invalid password.. Try again')
                                        
                                else:print('invalid password.. Try again')
                            else:print('invalid pin.. Try again')
                                        
                                
                        except: 
                            print('invalid input.. Try Again..')
                    
                    elif decision=='6': #email history
                        acc_post_email(main[6], main[4])
                    
                    elif decision=='7': #acnt info
                        balancy = list(filter(lambda x: True if x[4]==main[4] else False,db_mani.MainDb('Mainstructure').display_dat('user_main')))
                        balancy = balancy[0][8]
                        print(F'''
------------------------------
User's Info                  |
------------------------------
User name: {main[0]}
User id: {main[4]}
User balance: ${balancy}
account created on: {main[7]}
User's email id: {main[6]}
------------------------------
    ''')
                    
                    elif decision=='8': 
                        try:
                            pin = getpass('Enter 4 digit pin: ')
                        except:
                            print('Invalid input. Try again!')
                        else:
                            if pin==main[9]:
                                print('pin matched')
                                dece = input('Do you want to delete this account(y/n): ').casefold()
                                if dece=='y':
                                    buby = db_mani.MainDb('MainStructure')
                                    buby.del_data('user_main', main[4])
                                    #------------------------------------
                                    remove(F'usr_qr_codes\\{main[4]}.jpg')
                                    remove(F'csv_history_aisle\\{main[4]}.csv')
                                    #------------------------------------
                                    print('Account deleted successfully!!')
                                    buby.close_db()
                                    
                                    break   
                                else: print('deletion process was aborted')
                            else: print('pincode didn\'t match')
                    
                    
                    elif decision=='9': 
                        print('Logging out...')
                        break
                    
                    else: print('Invalid input... Try again with a valid one.')
                    
                    print(outputs.splitter)
                #------------------------------------------------------------------------------------>
                datas.close_db()
                
                        
            else: 
                print('No such user found/password didn\'t match! Try again.')
                print()
        else: 
            print('Invalid input! Try again.')
            print()
        print(outputs.splitter)

#----------------------------------------------------------------------------->>>

    elif main_key=='4': 
        users.show_shares()
        print(outputs.splitter)
        
    elif main_key=='5': 
        print('Terminating....')
        break
    
    else: pass


