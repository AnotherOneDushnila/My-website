import psycopg2
from typing import List, Any, Tuple
from os import environ



USERNAME = environ.get("USERNAME")
DB_PASSWORD = environ.get("DB_PASSWORD")
HOST = environ.get("HOST")
DB_NAME = environ.get("DB_NAME")
PORT = "5423"



class Base:

    def fetch_all() -> List[Any]:
        """
        This method fetches all messages from the database
        """
        conn = psycopg2.connect(

            database = DB_NAME,
            user = USERNAME,
            password = DB_PASSWORD,
            host = HOST,
            port = PORT

        )
        
        cursor = conn.cursor()

        cursor.execute("SELECT info, name FROM mysite_messeges")
        result = cursor.fetchall()

        conn.close()

        return Base.parse(result)
    


    def fetch_new() -> List[Any]:
        """
        This method fetches new messages from the database
        """
        conn = psycopg2.connect(

            user = USERNAME,
            password = DB_PASSWORD,
            host = HOST,
            port = PORT

        )
        
        cursor = conn.cursor()

        result = cursor.execute("SELECT info, name FROM mysite_messeges WHERE flag = 'Ready to send'") 
        result = cursor.fetchall()

        cursor.execute("UPDATE mysite_messeges SET flag = 'Cheked' WHERE flag = 'Ready to send'")
        conn.commit()
        
        conn.close()

        return Base.parse(result)

    


    def parse(data : List[Tuple]):
        
        info : str; contact : str
        fd = data[0]
        
        info_contact = [*fd]

        info, contact = info_contact[0], info_contact[1]

        result = info + '\n' + contact

        print(type(result))
        print(result)

        return result
