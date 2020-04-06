#镇江智慧物价网
import urllib
import urllib.request
import time
pch=time.strftime("%y%m%d%H%M%S", time.localtime())
def createDb(cursor,conn):
  sql = """
  IF OBJECT_ID('spjg', 'U') IS NOT NULL DROP TABLE spjg  
  CREATE TABLE spjg (id INT NOT NULL identity(1,1),spmc VARCHAR(100),jg numeric(10,2),sply VARCHAR(100),zqsj datetime,PRIMARY KEY(id))   
  """   
  cursor.execute(sql)   
  conn.commit()

url = "http://www.jiage880.com/clz/pjindex.aspx"
#使用user_agent变量！！
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
print(response)
content = response.read().decode('utf-8')
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, "html.parser")
items = soup.select("span.zi_h13s")
import pymssql
server = "localhost"
user = "sa"
#数据库用户名与密码
password = "141026"
database = "cgdatajdk"
conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()

for item in items:
     sql = "INSERT INTO spjg(spmc,jg,sply,zqsj,zqpc) VALUES ('"+item.encode_contents().decode('utf-8')+"',"+item.parent.parent.parent.find("span",{"class":"zi_h16"}).encode_contents().decode('utf-8')+",'镇江智慧物价网',getdate(),'"+pch+"')"
     cursor.execute(sql)
     conn.commit()

conn.close()


#常州价格通网
import urllib
import urllib.request
import pymssql

def shuju(i):
     url = "http://www.jgtong.com.cn/newshxf/ljtscpf.aspx?page="+str(i)+"&addtime=&cat_code=&ispj="
     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
     req = urllib.request.Request(url, headers={
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
     })
     response = urllib.request.urlopen(req)
     content = response.read().decode('utf-8')
     from bs4 import BeautifulSoup
     soup = BeautifulSoup(content, "html.parser")
     items = soup.select("table.table_hui1")
     server = "localhost"
     user = "sa"
     password = "141026"
     database = "cgdatajdk"
     conn = pymssql.connect(server, user, password, database)
     cursor = conn.cursor()
     for item in items:
          items1=item.find("tr")
          count=0
          spmc=""
          cgjg=""
          pjdjg=""
          for item1 in items1:
               count+=1
               if count==2:
                    spmc=str(item1.string).strip()
               if count==6:
                    cgjg=str(item1.string).strip()
               if count==8:
                    pjdjg=str(item1.string).strip()
          sql = "INSERT INTO spjg(spmc,jg,sply,zqsj,zqpc) VALUES ('"+spmc+"',"+cgjg+",'常州价格通网菜场',getdate(),'"+pch+"')"
          sql += "INSERT INTO spjg(spmc,jg,sply,zqsj,zqpc) VALUES ('"+spmc+"',"+pjdjg+",'常州价格通网平价店',getdate(),'"+pch+"')"
          cursor.execute(sql)
          conn.commit()

for i in range(1,4) :
     shuju(i)
     conn.close()


#凌家塘
import urllib
import urllib.request
import time

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

url = "http://www.ljt.cn/%5Cpriceinfo%5Cpriceinfo_"+time.strftime("%m%d", time.localtime())+".htm"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read().decode('gb2312')
from bs4 import BeautifulSoup
soup = BeautifulSoup(content, "html.parser")
items = soup.select('tr[height="19"]')
import pymssql
server = "localhost"
user = "sa"
password = "141026"
database = "cgdatajdk"
conn = pymssql.connect(server, user, password, database)
cursor = conn.cursor()
for item in items:
     items1=item.select('td')
     count=0
     spmc=""
     jg=""
     for item1 in items1:
          count+=1
          if count==1:
               spmc=str(item1.text).strip()
          if count==4:
               jg=str(item1.text).strip()
     if is_number(jg):
          sql = "INSERT INTO spjg(spmc,jg,sply,zqsj,zqpc) VALUES ('"+spmc+"',"+str(float(jg)/2)+",'凌家塘',getdate(),'"+pch+"')"
          cursor.execute(sql)
          conn.commit()

conn.close()

