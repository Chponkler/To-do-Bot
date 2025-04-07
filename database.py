from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum
from datetime import datetime

Base = declarative_base()

class Priority(enum.Enum):
    HIGH = "🔴 Высокий"
    MEDIUM = "🟡 Средний"
    LOW = "🟢 Низкий"

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String(255))
    category = Column(String(50))
    deadline = Column(DateTime)
    priority = Column(Enum(Priority))
    is_completed = Column(Boolean, default=False)
    is_recurring = Column(Boolean, default=False)
    recurrence_rule = Column(String(50))  # "daily", "weekly", "monthly"
    template_id = Column(Integer, ForeignKey("templates.id"))
    postponed_count = Column(Integer, default=0)
    
    template = relationship("Template", back_populates="tasks")

class Template(Base):
    __tablename__ = "templates"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String(50))
    tasks = relationship("Task", back_populates="template")
