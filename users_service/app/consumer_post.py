from kafka import KafkaConsumer
import json
from config import curso

KAFKA_TOPIC = "UPDATE_NUMBERS_OF_POSTS"

CONFIRMED_KAFKA_TOPIC = "UPDATE_NUMBERS_OF_POSTS [confirmed] "


consumer = KafkaConsumer(
                        KAFKA_TOPIC,
                        bootstrap_servers=['host.docker.internal:9093'],
                        api_version=(0,11,5)
                        )


def kafka_queue():
  print("sending ","="*200,">>>>>>>>>>>>>>>>>>>>>>")
  try:
    print(consumer) 
    db = curso()
    c = db.cursor()
    for i in consumer:
      b = json.loads(i[6].decode())
      print(b)
      # {'total_posts': '28', 'user_id': '1'}
      # s = f"""insert into tests(test) values ('{b}')"""
      s = f"""UPDATE users
                SET post = {int(b["total_posts"])}
                WHERE user_id = {int(b["user_id"])} ;
                """

      # s = (b["order_id"],int(b["id_customer"]),b["payment_methods"],b["order_status"],float(b["total_prices"]),b["note"])
      # sqll = '''insert into transactions(orders_id,id_customer,
      #          payment_methods,order_status,
      #         total_prices,note)
      #         values(%s,%s,%s,%s,%s,%s) ;
      #         '''
      # c.execute(sqll,s)
      # db.commit()
      c.execute(s)
      db.commit()
      # print(f"this is orders : {b['order_id']} was send ","="*50,">>>>>>")
  except Exception as e:
      print(f"Error {e}")  

if __name__ == "__main__":
  kafka_queue()