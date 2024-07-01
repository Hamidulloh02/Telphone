import pandas as pd
from django.db import connection
from models import Word # MyModel o'z modelingiz nomi
import pandas as pd
data = pd.read_csv('D:\\Full projects\\auxwords.uz\\backend\\auxwordbackend\\Word\\lugat.csv')
print(data)

# # Ma'lumotlar bazasiga yozish
# for index, row in excel_data.iterrows():
#     my_model_instance = Word(field1=row['field1'], field2=row['field2'],) # Ma'lumotlarni joylash
#     my_model_instance.save() # Ma'lumotni saqlash

# # Transaktsiyani saqlash
# connection.commit()