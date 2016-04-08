#coding:utf-8
import os
import os.path
import MySQLdb
import time
#values=[]


#读取文件
rootdir = 'E:\\thunder\\52g163\\1632'								   # 指明被遍历的文件夹

#数据库操作
try:


	start = time.time()
	print 'start'
	i = 1
	for parent,dirnames,filenames in os.walk(rootdir):	#三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
		for filename in filenames:						#输出文件信息
			print i
			print filename
			i=i+1
			sql = filename
			sql = "LOAD DATA LOCAL INFILE 'E:/thunder/52g163/1632/"+sql+"' INTO TABLE sgk163 FIELDS TERMINATED BY '----'"
			#print sql
			conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',port=3306,charset='utf8')
			cur =conn.cursor()
			conn.select_db('163sgk')
			count=cur.execute(sql)
			print 'there has %s rows record' % count
			conn.commit()
			cur.close()
			conn.close()
	c = time.time()-start
	print('time:%0.2f'%(c))
	print 'there has %s rows record' % count



except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])