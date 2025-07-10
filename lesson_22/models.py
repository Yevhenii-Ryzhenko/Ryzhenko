"""
Службовий код
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)

    courses = relationship("Courses", secondary="relations", back_populates="students")

class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    course_duration = Column(Integer)
    diploma = Column(Boolean)

    students = relationship("Students", secondary="relations", back_populates="courses")

class Relation(Base):
    __tablename__ = 'relations'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)