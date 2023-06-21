def calling_database():
    # import necessary lib
    # from . import db
    from flask_table import Table, Col
    # NOTE unable to using this lib BC it haven't provide automap_base
    # from flask_mysqldb import MySQL
    from sqlalchemy.ext.automap import automap_base
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine

    # NOTE could be replace by db = SQLAlchemy(app); db.init_app; db.engine
    engine = create_engine('mysql+mysqlconnector://root@localhost:5001/travel')

    # create base Object
    Base = automap_base()

    # NOTE could be replace by db.engine two
    Base.prepare(engine, reflect=True)

    # could using global variable tas table
    User = Base.classes.user
        # for table_name in Base.classes.keys():
        # globals()[table_name] = Base.classes[table_name]
    
    # Create a session 数据库会话
    # NOTE still could replace by db.engine
    session = Session(engine)

    data = session.query(User).all()
    
    for obj in data:
        for attr, value in obj.__dict__.items():
            print(f"{attr}: {value}")
        print("\n") 
        
if __name__ == "__main__":
    calling_database