from matplotlib import pyplot as plt
import sys 
from matplotlib import pylab
sys.path.insert(1, '\python_pgms\mysql_project_class12_new\source_aisle\db_managment')
import validative

users = {
    'C.Amrit Subramanian [C.E.O]': 40,
    'S.Surya [C.O.O]': 40,
    'M.Adethya [C.F.O]': 20,
}

def show_shares():
    main = validative.MainDb('MainStructure')
    x = main.display_dat('Bankrevenue')
    main.close_db()
    total_val = sum(list(map(lambda z: z[0], x)))+100_000_000



    spliters = list(users.items())
    main_vals = list(map(lambda x: x[1], users.items())), list(map(lambda x: f'{x[0]}\n${x[1]/100*total_val:.2f} | {x[1]}%', users.items()))



    fig = pylab.gcf()
    fig.canvas.set_window_title('Shares Composition'+F' | equity value: 1% -> ${(1/100*total_val):.2f} | bussiness valuation -> ${total_val}')

    plt.pie(main_vals[0], labels=main_vals[1])

    plt.show()
    
if __name__=='__main__':
    show_shares()