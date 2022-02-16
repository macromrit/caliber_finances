import csv

def csv_input(Mode, Amount, Time, AccntBalance, Filename):
    Amount = F'${Amount}'
    AccntBalance = F'${AccntBalance}'
    with open(F'C:\\python_pgms\\mysql_project_class12_new\\csv_history_aisle\\{Filename}.csv', mode='a', newline='') as jammer:
        x = csv.writer(jammer,
                       delimiter=',')
        if Mode=='c': #credited
            x.writerow((Amount, '------', Time, AccntBalance))

        else:#mode=='d'
            x.writerow(('------', Amount, Time, AccntBalance))
        
def initialize_user(Filename):
    with open(F'C:\\python_pgms\\mysql_project_class12_new\\csv_history_aisle\\{Filename}.csv', mode='x', newline='') as jammer:
        x = csv.writer(jammer, 
                       delimiter=',')
        x.writerow(['Credited', 'Debited','Transaction Time', 'Account Balance'])
        
if __name__=='__main__':
    pass