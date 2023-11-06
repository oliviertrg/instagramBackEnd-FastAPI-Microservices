# import postgresql
from datetime import datetime
# 1. Import the config object from decouple.
import psycopg2cffi

def curso():
 try :
    
    conn = psycopg2cffi.connect(
                           database = 'postgres',
                           user = 'rioverrain',
                           host = 'host.docker.internal',
                           port = 5432,
                           password = 'cmlodmVyckBpbjIy'
                           
                        )

    print(f"conecting susseccefull")
    

 except Exception as e :
    print("-"*200)
    print("Connecting to database failed")
    print(f"Error {e}" )

 return conn


if __name__ == "__main__":
         curso()