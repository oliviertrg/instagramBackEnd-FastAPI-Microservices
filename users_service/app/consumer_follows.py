from kafka import KafkaConsumer
import json
from config import curso

ORDER_KAFKA_TOPIC = "UPDATE_NUMBERS_OF_FOLLOWS"

ORDER_CONFIRMED_KAFKA_TOPIC = "UPDATE_NUMBERS_OF_FOLLOWS [confirmed] "


consumer = KafkaConsumer(
                        ORDER_KAFKA_TOPIC,
                        bootstrap_servers=['host.docker.internal:9300'],
                        api_version=(0,11,5)
                        )

def kafka_queue():
  print("sending ","="*200,">>>>>>>>>>>>>>>>>>>>>>")
  try: 
    db = curso()
    c = db.cursor()
    for i in consumer:
      b = json.loads(i[6].decode())
      print(b)
      # s = (b["order_id"],int(b["id_customer"]),b["payment_methods"],b["order_status"],float(b["total_prices"]),b["note"])
      # sqll = '''insert into transactions(orders_id,id_customer,
      #          payment_methods,order_status,
      #         total_prices,note)
      #         values(%s,%s,%s,%s,%s,%s) ;
      #         '''
      # c.execute(sqll,s)
      # db.commit()
      # print(f"this is orders : {b['order_id']} was send ","="*50,">>>>>>")
  except Exception as e:
      print(f"Error {e}")  

if __name__ == "__main__":
  kafka_queue()