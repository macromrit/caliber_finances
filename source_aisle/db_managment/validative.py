import mysql.connector


class MainDb:
    
    def __init__(self, dbname:str) -> None:
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="amma@@1953",
                    database=dbname
                    )


    def display_dat(self, tablename: str)->list:
        main = self.mydb.cursor()
        main.execute(F'SeLeCt * FrOm {tablename}')
        ans = list(main)
        main.close()
        return ans

    
    def insert_dat(self, *contents, tablename)->bool:
        try:
            main = self.mydb.cursor()
            main.execute(F'InSeRt InTo {tablename} VaLuEs {contents}')
            self.mydb.commit()
            main.close()
        except: 
            self.mydb.rollback()
            prcs = False
        else: prcs = True
        finally: pass

        return prcs


    def del_data(self, tablename,unique_id)->bool:
        try:
            main = self.mydb.cursor()
            main.execute(F'DeLeTe FrOm {tablename} WhErE UnIqUe_Id="{unique_id}"')
            self.mydb.commit()
            main.close()
        except:
            self.mydb.rollback()
            prcs = False
        else: prcs = True
        finally: pass
        
        return prcs


    def upd_data(self, tablename, newvalname, newval, newvaltype, unique_id)->bool:
        '''n means number for newvaltype'''
        try:
            main = self.mydb.cursor()
            if newvaltype=='n':
                main.execute(F'UPDATE {tablename} set {newvalname}={newval} where unique_id = \'{unique_id}\'')
            else:
                main.execute(F'UPDATE {tablename} set {newvalname}=\'{newval}\' where unique_id = \'{unique_id}\'')
            self.mydb.commit()
            main.close()
        except: 
            self.mydb.rollback()
            prcs = False
        else: prcs = True
        finally: pass
        
        return prcs


    def close_db(self)->None:
        self.mydb.close()
        

if __name__=='__main__': 
    pass