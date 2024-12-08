from passlib.context import CryptContext
from sqlalchemy import Column, String, Text, Boolean, Integer, BigInteger, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from models.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, index=True)
    number = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    fullname = Column(String, nullable=False)
    acc_status = Column(String, nullable=False)
    user_status = Column(String, nullable=False)
    is_moderator = Column(Boolean, nullable=False, default=False)

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="user")

class Master(Base):
    __tablename__ = 'masters'

    name = Column(String, primary_key=True)

    orders = relationship("Order", back_populates="master")

class ClothingModel(Base):
    __tablename__ = 'clothing_models'

    name = Column(String, primary_key=True)
    description = Column(Text, nullable=False, default="")
    price = Column(BigInteger, nullable=False, default=500)
    color = Column(String, nullable=False, default="white")
    average_rating = Column(Integer)
    size = Column(String, nullable=False, default="S")
    # img = Column()

    orders = relationship("Order", back_populates="cloth")
    reviews = relationship("Review", back_populates="cloth")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    master_name = Column(String, ForeignKey('masters.name'), nullable=False)
    cloth_name = Column(String, ForeignKey('clothing_models.name'), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    update_date = Column(DateTime(timezone=True), nullable=False, default=func.now(), onupdate=func.now())
    status = Column(String, nullable=False, default="Создан")
    delivery = Column(String, nullable=False, default="Почта")



    user = relationship("User", back_populates="orders")
    master = relationship("Master", back_populates="orders")
    cloth = relationship("ClothingModel", back_populates="orders")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey('users.id'), nullable=False)
    cloth_name = Column(String, ForeignKey('clothing_models.name'), nullable=False)
    rate = Column(Integer, nullable=False, default=5)
    description = Column(Text, nullable=False, default=" ")
    # img = Column()

    user = relationship("User", back_populates="reviews")
    cloth = relationship("ClothingModel", back_populates="reviews")

    __table_args__ = (
        CheckConstraint('rate >= 1 AND rate <= 5', name='check_rate_range'),
    )



