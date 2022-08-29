# How to read config info file.

with open("./routes/env_conf.json", 'r', encoding='utf-8') as ec:
    json_data = json.load(ec)
    print(json_data)
DB_TYPE = json_data['DB_TYPE']
DB_NAME = json_data['DB_NAME']

print(DB_TYPE)
print(DB_NAME)

# BOOK_REQUESTS = json_data
   BOOK_REQUESTS = results
except:
   print ("Error: unable to fetch the data")

initializaed local database via creation a new database
DB_NAME = "abc"
DB_NAME = str(os.getenv('dbname'))   
if DB_NAME == "None":
    DB_NAME = "text_db"

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="www",  # please adjust the user name as same as the local MySQL's user name  -wayneW
  password="5566"  # change the password as you defined in your MySQL database  -wayneW
)
