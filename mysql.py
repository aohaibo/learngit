import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host='10.13.45.87',
    port=3306,
    user='tester',
    password='123456',
    db='shake',
    charset='utf8'
)

# 获取游标
cursor = conn.cursor()

# 执行sql语句
sql = 'INSERT INTO `shake`.`t_real_money_reward_record74`(`id`, `shake_record_id`, `reward_code`, `account_id`, `create_time`, `reward_type`, `collect_status`, `collector_id`, `collector_salutation`, `has_push_notice`, `out_time_date`, `amount`) VALUES (777, 888, 227,testtes, 2019-11-09 23:44:33, 9, 0, NULL, NULL, 0, 2019-11-21 00:00:00', NULL)'
#rows = cursor.execute(sql, ('4', 'qzcsbj4'))

# 提交
conn.commit()

# 关闭游标
cursor.close()

# 关闭连接
conn.close()　　