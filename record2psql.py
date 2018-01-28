import psycopg2
import shapefile

locale = input("Locale: ")
name = input("Name: ")

fpath = "Resources/{locale}/{name}".format(locale=locale, name=name)

print("Reading file")
sh = shapefile.Reader(fpath)
print("Fetching records...")
records = sh.records()
print("Fetched all records ({})".format(len(records)))

print("Connection Databse..")
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    user="postgres",
    password="<!-- DB PASSWORD HERE -->",
    database="geo"
)
cur = conn.cursor()
print("Succesfully connected to Database with cursor {}".format(id(cur)))

vals = []

print("Making values...")
for rec in records:
    if rec[19]:
        vals.append(
            [
                rec[19],
                rec[1].decode('euc-kr') if type(rec[1]) is type(b'') else rec[1],
                rec[2].decode('euc-kr') if type(rec[2]) is type(b'') else rec[2],
                rec[3],
                rec[4],
                rec[9],
                rec[15],
                rec[16],
                rec[25],
                rec[0]
            ]
        )
print("Made values.")

open("out.json","w",encoding="UTF-8").write(__import__("json").dumps(vals, indent=4))

base_query = "INSERT INTO {locale} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(locale=locale)
try:
    cur.executemany(base_query, vals)
except Exception as ex:
    print(ex)
    print(cur.query)

conn.commit()
print(cur.statusmessage)

