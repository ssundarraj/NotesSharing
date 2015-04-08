from ..models import *
from app import app, db  # Your init files
from sqlalchemy import or_, and_


def add_star(file_id, user_rno):
    starred_file = stars(file_id=file_id, starrer=user_rno)
    db.session.add(starred_file)
    db.session.commit()

def get_stars(file_id):
    all_stars = stars.query.filter(stars.file_id.like(file_id)).all()
    return len(all_stars)

def has_starred(file_id, user_rno):
    starred = stars.query.filter(and_(stars.file_id.like(file_id), 
                                      stars.starrer.like(user_rno))).all()
    return len(starred) >= 1

if __name__=='__main__':
    print has_starred(1, '106112091')
