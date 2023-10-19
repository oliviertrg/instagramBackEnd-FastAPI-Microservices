# import postgresql
from datetime import datetime
# 1. Import the config object from decouple.
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

async def csd():
 try :
    
    auth_provider = PlainTextAuthProvider(username='rioverrain', password='rioverr@in22')
    cluster = Cluster(['instagram-cassandra_posts-1'],port = 9042,
                      auth_provider=auth_provider)
    session = cluster.connect('posts') 
    print(f"conecting susseccefull")

 except Exception as e :
    print("-"*200)
    print("Connecting to database failed")
    print(f"Error {e}" )
 return session    


if __name__ == "__main__":
      csd()
      