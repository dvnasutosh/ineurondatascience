
# Mysql : 
    
    #     1. Create a  table attribute dataset and dress dataset 
    #     2. Do a bulk load for these two table for respective dataset 
    #     3. read these dataset in pandas as a dataframe 
    #     4. Convert attribute dataset in json format 
#     5. Store this dataset into mongodb
#     6. in sql task try to perform left join operation with attrubute dataset and dress dataset on column Dress_ID
#     7. Write a sql query to find out how many unique dress that we have based on dress id 
#     8. Try to find out how mnay dress is having recommendation 0
#     9. Try to find out total dress sell for individual dress id 
#     10. Try to find out a third highest most selling dress id 


from cmath import nan
import mysql.connector as conn
import pymongo
import pandas as pd

mysql= conn.connect(host = "localhost",user="root", passwd='12345')
mongo=pymongo.MongoClient("mongodb+srv://Dragon:Dragon@cluster0.tdst7.mongodb.net/?retryWrites=true&w=majority")

# Task 1: Create a  table attribute dataset and dress dataset


mys_cur=mysql.cursor()
db_name='dress'
def initiate_db():
        #     1. Create a  table attribute dataset and dress dataset 
    mys_cur.execute("CREATE DATABASE IF NOT EXISTS dress;")
    
    mys_cur.execute(f"""
CREATE TABLE IF NOT EXISTS dress.attributes(
        `CRA` INT NOT NULL,
        `Style` VARCHAR(30),
        `Price` VARCHAR(30),
        `Rating` DOUBLE,
        `Size` VARCHAR(30),
        `Season` VARCHAR(30),
        `NeckLine` VARCHAR(30),
        `SleeveLength` VARCHAR(30),
        `waiseline` VARCHAR(30),
        `Material` VARCHAR(30),
        `FabricType` VARCHAR(30),
        `Decoration` VARCHAR(30),
        `Pattern Type` VARCHAR(30),
        `Recommendation` BOOLEAN,
        PRIMARY KEY(`CRA`)
    );""")
    mys_cur.fetchall()
    mys_cur.execute(f"""
    CREATE TABLE IF NOT EXISTS dress.sales(
        
        `Dress_ID` INT NOT NULL,
        `Date` DATE NOT NULL,
        `Sales` INT,
        CONSTRAINT FK_Dress_ID FOREIGN KEY (`Dress_ID`)
            REFERENCES attributes(CRA)
            ON UPDATE CASCADE
    );""")
    mys_cur.fetchall()
    mysql.commit()

def close_conn():
    mongo.close()
    mys_cur.close()
    mysql.close()
    
def bulk_load():
        #     2. Do a bulk load for these two table for respective dataset 
    import datetime
    sales=pd.read_excel('pandas\data fsds\Dress Sales.xlsx',index_col=0)
    attributes=pd.read_excel('pandas\data fsds\Attribute DataSet.xlsx')
    
    attributes=attributes.to_dict(orient='split')
    struct=str(attributes['columns']).replace(r"'",'').replace('[','').replace(']','')
    sqlattrstr=f"REPLACE INTO dress.attributes VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    n=[]
    for i in attributes['data']:
        for j in range(len(i)):
            if str(i[j])=='nan':
                # print('hit')
                i[j]=None
        n.append(tuple(i))
        
    mys_cur.executemany(sqlattrstr,n)
    
    sales=sales.to_dict(orient='split')
    # print(sales)
    n=[]
    for i in range(len(sales['index'])):
        for j in range(len(sales['columns'])):    
            if type(sales['columns'][j])==str:
                sales['columns'][j]=datetime.datetime.strptime(sales['columns'][j],r'%d/%m/%Y')
            sales_data=sales['data'][i][j]
            # print(sales_data, end=' ')
            if str(sales_data)=='nan':
                # print('hit')
                sales_data=None
            elif type(sales_data)==type(''):
                sales_data=-1
            elif type(sales_data)==type(0.0):
                sales_data=int(sales_data)
                
                # print(sales_data,'  ', type( sales_data),end='  ')
                # print((sales['index'][i],str(sales['columns'][j].date()),sales_data))
                
            n.append((sales['index'][i],str(sales['columns'][j].date()),sales_data))
    mys_cur.executemany('REPLACE INTO dress.sales VALUES(%s,%s,%s)',n)
    mysql.commit();
def bulk_read():
    #     3. read these dataset in pandas as a dataframe 
   mys_cur.execute(f'SELECT * FROM {db_name}.attributes;')
   attr=mys_cur.fetchall()
   attr=pd.DataFrame(attr,columns=['CRA','Style' ,'Price' , 'Rating','Size' ,'Season' ,'NeckLine' ,'SleeveLength' ,'waiseline' ,'Material' ,'FabricType' ,'Decoration' ,'Pattern Type', 'Recommendation'])

   mys_cur.execute(f'SELECT * FROM {db_name}.sales;')
   sale=pd.DataFrame(mys_cur.fetchall(),index=None,columns=['Dress_ID','Date','Sale'])
   return attr,sale  
# initiate_db()
# bulk_load()
a,s=bulk_read()
    #     4. Convert attribute dataset in json format 
print((a.to_json(orient='records')[0]))
#     5. Store this dataset into mongodb
def to_mongo(sales=(s.to_dict(orient='records')),attr=a.to_dict(orient='records')):
    
    
    for i in range(len(sales)):
        
       sales[i]['Date']=pd.to_datetime(sales[i]['Date'])
    mongo['dress']['sales'].insert_many(sales)
    mongo['dress']['attributes'].insert_many(attr)

to_mongo()

    

close_conn()
