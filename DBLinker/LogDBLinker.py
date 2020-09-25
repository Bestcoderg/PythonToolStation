# version:python3
# Instructions:在数据库中（taiwan）查询某个用户对应的字段
# Time:2020-09-25
# Author:@Bestcoderg

import pandas as pd
import pymysql
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# 打开excel
writer = pd.ExcelWriter('/tmp/logout.xlsx')


for month in range(4, 9):
    for day in range(1, months[month] + 1):
        dbname = "kunlun_official_daily1_2020"+ '_' + str(month).rjust(2, '0') + '_' + str(day).rjust(2, '0')
        dbconn = pymysql.connect(
            host="10.22.246.100",
            port=3306,
            user="game",
            password="game",
            database=dbname
            #database="kunlun_official_daily1_2020_09_11"
        )
        sqlcmd = 'select * from _LogTAuctionExpireFlow where _RoleId=795448397382403711 AND _Op=1'
        tabledata = pd.read_sql(sqlcmd, dbconn)
        #print(tabledata)
        tabledata.to_excel(excel_writer=writer, sheet_name='sheet1', index=False)

for day in range(1, 15):
    dbname = "kunlun_official_daily1_2020_09_" + str(day).rjust(2, '0')
    dbconn = pymysql.connect(
        host="10.22.246.100",
        port=3306,
        user="game",
        password="game",
        database=dbname
        # database="kunlun_official_daily1_2020_09_11"
    )
    sqlcmd = 'select * from _LogTAuctionExpireFlow where _RoleId=795448397382403711 AND _Op=1'
    tabledata = pd.read_sql(sqlcmd, dbconn)
    #print(tabledata)

    tabledata.to_excel(excel_writer=writer, sheet_name='sheet1', index=False)

writer.save()