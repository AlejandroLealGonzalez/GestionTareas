from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://admin:12345@localhost:3306/TSOFT2")

meta_data = MetaData()