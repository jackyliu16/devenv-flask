from . import db
from flask_table import Table, Col
from flask_mysqldb import MySQL
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# # 从 MySQL 表中获取数据
# cur = mysql.connection.cursor()
# cur.execute('''SELECT * FROM users''')
# data = cur.fetchall()
# # 使用 UserTable 类生成 HTML 表格
# table = UserTable(data)
# html = table.__html__()
# class UserTable(Table):
#     id = Col('id')
#     name = Col("name")
#     password = Col("pwd")
#     age = Col("age")
#     email = Col("email")
#     gender = Col("gender")


# engine = create_engine('mysql+mysqlconnector://root@localhost/travel')

# 创建一个 AutomapBase 对象
Base = automap_base()

# 使用反向工程工具将 MySQL 中所有的表映射为 ORM 对象模型
Base.prepare(db.engine, reflect=True)

# 获取 ORM 对象模型 (for table)
User = Base.classes.user
# for table_name in Base.classes.keys():
#     globals()[table_name] = Base.classes[table_name]

# # 创建会话
# session = Session(engine)

# # 使用 ORM 操作数据库
# user = User(name='John', age=25)
# session.add(user)
# session.commit()


