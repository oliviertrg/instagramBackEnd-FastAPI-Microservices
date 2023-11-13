# import postgresql
from datetime import datetime
# 1. Import the config object from decouple.
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def csd():
 try :
    
    auth_provider = PlainTextAuthProvider(username='rioverrain', 
                                          password='cmlodmVyckBpbjIy')
    cluster = Cluster(['instagram-cassandra_comments-1'],port = 9042,
                      auth_provider=auth_provider)
    session = cluster.connect('comment') 
    print(f"conecting susseccefull")

 except Exception as e :
    print("-"*200)
    print("Connecting to database failed")
    print(f"Error {e}" )
 return session    


if __name__ == "__main__":
      csd()