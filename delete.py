from main import Bird, Session

with Session() as session:
  bird = session.query(Bird).filter_by(id=4).one()
  session.delete(bird)
  session.commit()
