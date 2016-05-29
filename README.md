## test_code

import urllib
import json
import psycopg2
from sqlalchemy.dialects.postgresql import JSON


jw = open("output.txt", "wb")
f = urllib.urlopen("https://www.dockstore.org:8443/api/v1/tools")
jw.write(f.read())
jw.close()

conn = psycopg2.connect("dbname='mydb' user='postgres' password='123' host='localhost'")
print "Opened database successfully"

cur = conn.cursor()

cur.execute('''CREATE TABLE tools(
	GLOBAL_ID	varchar primary key, 
	registry-id varchar, 
	  registry varchar,
		organization varchar,
		name varchar,
		toolname varchar,
		tooltype json,
		description varchar,
		author varchar,
		meta-version varchar,
		version varchar,
		version global-id varchar
       );''')



conn.commit()

conn.close() 
