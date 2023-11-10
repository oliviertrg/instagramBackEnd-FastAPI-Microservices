from kafka import KafkaConsumer
import json
from config import curso

KAFKA_TOPIC = "UPDATE_NUMBERS_OF_FOLLOWING"

CONFIRMED_KAFKA_TOPIC = "UPDATE_NUMBERS_OF_FOLLOWING [confirmed] "


consumer = KafkaConsumer(
                        KAFKA_TOPIC,
                        bootstrap_servers=['host.docker.internal:9093'],
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
      s = f"""UPDATE users
                SET followings = {int(b["total_following"])}
                WHERE user_id = {int(b["user_id"])} ;
                """

      c.execute(s)
      db.commit()

  except Exception as e:
      print(f"Error {e}")  

if __name__ == "__main__":
  kafka_queue()