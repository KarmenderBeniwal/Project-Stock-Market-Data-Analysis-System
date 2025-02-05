from sqlalchemy import create_engine, Column, Float, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
import os

Base = declarative_base()


class StockData(Base):
    __tablename__ = "stock_data"
    symbol = Column(String, primary_key=True)
    date = Column(Date, primary_key=True)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)


def get_db():
    os.makedirs("../data", exist_ok=True)
    engine = create_engine("sqlite:///../data/stocks.db")
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()
