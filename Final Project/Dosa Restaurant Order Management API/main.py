from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Database URL
DATABASE_URL = "sqlite:///./db.sqlite"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI instance
app = FastAPI()

# Database models
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, unique=True, index=True)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    quantity = Column(Integer)
    timestamp = Column(Integer)
    notes = Column(String, nullable=True)

    customer = relationship("Customer")
    item = relationship("Item")


# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic schemas
class CustomerCreate(BaseModel):
    name: str
    phone: str

class CustomerUpdate(BaseModel):
    name: str
    phone: str

class CustomerOut(BaseModel): 
    id: int
    name: str
    phone: str

    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    name: str
    price: float

class ItemUpdate(BaseModel):
    name: str
    price: float

class ItemOut(BaseModel):  
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    customer_id: int
    item_id: int
    quantity: int
    timestamp: int
    notes: Optional[str] = None

class OrderUpdate(BaseModel):
    customer_id: int
    item_id: int
    quantity: int
    timestamp: int
    notes: Optional[str] = None

class OrderOut(BaseModel):  
    id: int
    customer_id: int
    item_id: int
    quantity: int
    timestamp: int
    notes: Optional[str] = None

    class Config:
        orm_mode = True

# Dependency for getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD operations for customers
@app.post("/customers", response_model=CustomerOut)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(name=customer.name, phone=customer.phone)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


@app.get("/customers/{id}", response_model=CustomerOut)
def read_customer(id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@app.put("/customers/{id}", response_model=CustomerOut)
def update_customer(id: int, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db_customer.name = customer.name
    db_customer.phone = customer.phone
    db.commit()
    db.refresh(db_customer)
    return db_customer


@app.delete("/customers/{id}")
def delete_customer(id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"message": "Customer deleted successfully"}


# CRUD operations for items
@app.post("/items", response_model=ItemOut)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{id}", response_model=ItemOut)
def read_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/items/{id}", response_model=ItemOut)
def update_item(id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}


# CRUD operations for orders
@app.post("/orders", response_model=OrderOut)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(
        customer_id=order.customer_id,
        item_id=order.item_id,
        quantity=order.quantity,
        timestamp=order.timestamp,
        notes=order.notes
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


@app.get("/orders/{id}", response_model=OrderOut)
def read_order(id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@app.put("/orders/{id}", response_model=OrderOut)
def update_order(id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db_order.customer_id = order.customer_id
    db_order.item_id = order.item_id
    db_order.quantity = order.quantity
    db_order.timestamp = order.timestamp
    db_order.notes = order.notes
    db.commit()
    db.refresh(db_order)
    return db_order


@app.delete("/orders/{id}")
def delete_order(id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted successfully"}
