from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Response
from .. import models,schema
def show_all_blogs(db:Session):
    blogs = db.query(models.blog).all()
    return blogs 

def create_new_blog(request:schema.blog,db:Session):
    new_blog = models.blog(title=request.title,content=request.content,creator_id=1)
    db.add(new_blog)
    db.commit()
    return new_blog

def show_blog_by_id(id:int,response:Response,db:Session):
    blog = db.query(models.blog).filter(models.blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog with id{id} is not found")

    return blog
    

def delete_blog_by_id(id:int,db:Session):
    blog = db.query(models.blog).filter(models.blog.id==id).delete(synchronize_session=False)
    db.commit()

    return {"detail":f"the blog with id{id} is deleted"}


def update_blog_by_id(id:int,request:schema.blog,db:Session):
    blog = db.query(models.blog).filter(models.blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the blog with id{id} is not found")
    db.query(models.blog).filter(models.blog.id==id).update({"title":request.title,"content":request.content})
    db.commit()
    return "updated"