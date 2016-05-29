# test_code

import urllib
import json
import psycopg2





conn = psycopg2.connect("dbname='mydb' user='postgres' password='123' host='localhost'")
print "Opened database successfully"

cur = conn.cursor()

cur.execute('''CREATE TABLE tools(
	global-id	varcha	primary key, 
	registry-id	varchar, 
	registry	varchar,
	organization	varchar,
	name	varchar,
	toolname	varchar,
	tooltype	json,
	description	varchar,
	author	varchar,
	meta-version	varchar,
	version	varchar,
	version-global-id	varchar
       );''')
       
cur.execute('''CREATE TABLE tools_versions(
	name	varchar,
	global-id	varchar primary key, 
	registry-id	varchar,
	image	varchar,
	descriptor	json,
	dockerfile	json,
	meta-version	varchar,
       );''')

f = urllib.urlopen("https://www.dockstore.org:8443/api/v1/tools")
json_f = json.loads(f.read())

for i in json_f:
	cur.execute("insert into tools(global-id, registry-id, \
	registry, organization, name, toolname, tooltype, description, \
	author, version-global-id) \
	VALUES \
	(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(i[""])

conn.commit()

conn.close() 
