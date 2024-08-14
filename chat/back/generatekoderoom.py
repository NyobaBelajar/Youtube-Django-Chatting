import uuid
import random
import datetime

# Start Transaction Kode
def generate_transaction_id():
  return f"{uuid.uuid4().hex[:10]}{random.randint(1000000, 9999999)}"

def gen_kode():
    date = datetime.datetime.now()
    return f"{generate_transaction_id()}-{date.year}{date.month}{date.day}"