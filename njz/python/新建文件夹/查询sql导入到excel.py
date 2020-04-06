import pymssql,xlwt,time,sys,xlrd
from xlutils.copy import copy
today_date = time.strftime("%Y%m%d", time.localtime(time.time()))
def mkfile(file_dist): #生成Excel 并定义列名
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'
    style.font = font
    for i in file_dist.keys():
        wbk=xlwt.Workbook(encoding='utf-8')
        sheet1=wbk.add_sheet(u'sheet1')
        for j in xrange(len(file_dist.get(i).split(','))):
            sheet1.write(0,j,file_dist.get(i).split(',')[j])
        wbk.save(i+today_date+'.xls')
def get_data(database,sql):#连接mssql 返回查询结果
    conn=pymssql.connect(host='localhost',user='ceshi',password='ceshi',database=database,charset='utf8')
    cur=conn.cursor()
    cur.execute(sql)
    result=cur.fetchall()
    cur.close()
    conn.close
    return result
def write_data_to_excel(database,name,sql): #追加sql执行结果到对应Excel表格
    result=get_data(database,sql)
    oldexcel=xlrd.open_workbook(name+today_date+'.xls')
    rows=oldexcel.sheets()[0].nrows
    newexcel=copy(oldexcel)
    sheet=newexcel.get_sheet(0)
    for i in xrange(len(result)):
        for j in xrange(len(result[i])):
            sheet.write(i+1,j,u"%s"%(result[i][j]))
    newexcel.save(name+today_date+'.xls')

if __name__=='__main__':
    file_dist = {u'合同': "u'id', u'address', u'rmb', u'data'",
                 u'租赁': "u'lyk', u'ly', u'rmb', u'data'"} #定义表字段
    mkfile(file_dist)
    sql1='select top 1 * from [dbo].[a_bak]'
    sql2="select top 2 * from [dbo].[a_bak]"
    db_dict={u'合同':sql1,u'租赁':sql2}  #定义表对应查询sql语句
    for k ,v in db_dict.items():
        write_data_to_excel('new_HouseRent_test',k,v)
        
        
        