from venv import create
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from sqlalchemy import engine, Column, Integer, String, create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///sprint.db")
session = sessionmaker()
Base = declarative_base(engine)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True)
    name = Column(String, index = True)
    group = Column(String)


Base.metadata.create_all()


local_server = FastAPI()


@local_server.get("/")
def hello():
    return {"Status code" : "200"}

@local_server.post("/student/add/")
def basa(_id: int, name: str, group: str):
    user = Student(
        id = _id,
        name = name,
        group = group
    )
    db = session()
    db.add(user)
    db.commit()
    db.flush()
    return {"status" : "OK"}


@local_server.put("/student/update/")
def red(_id: int, name: str, group: str):
    db = session()
    if (db.query(Student).filter_by(id=_id).all()):
        db.execute(
            update(Student)
            .where(Student.id == _id)
            .values(name = name, group = group)
        )
        db.commit()
        db.flush()
        return ("Запись успешно обновлена!")
    else:
        return ("Такого студента нет в базе данных")


@local_server.get("/student/{student_id}/")
def s(student_id: int):
    s_id = student_id
    db = session()
    stud = db.query(Student).filter_by(id=s_id).all()
    if (stud):
        if (stud[0].id == s_id):
            return (f'{stud[0].id} | {stud[0].name} | {stud[0].group}')
        db.commit()
        db.flush()
    else:
        return "Такого студента нет."
    
@local_server.get("/student/all/")
def all_stu():
    db = session()
    students_all = db.query(Student).all()
    if (students_all):
        return ''.join([f'{students_all[i].id} | {students_all[i].name} | {students_all[i].group}' for i in range(len(students_all))])
    db.commit()
    db.flush() 

import uvicorn 


if __name__ == "__main__":
    uvicorn.run("bd:local_server", port=8000, reload=True)