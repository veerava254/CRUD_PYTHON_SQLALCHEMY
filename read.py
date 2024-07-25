from main import Session, Bird
from sqlalchemy import select

# Session to get all recors
with Session() as session:
  birds = session.query(Bird).all()
  for bird in birds:
    print(bird)

# Session to get all recors
with Session() as session:
  birds = session.execute(select(Bird)).scalars().all()
  for bird in birds:
    print(bird)

# filter by id
with Session() as session:
  bird = session.query(Bird).filter_by(id=1).one()
  print(bird)

# filter by name
with Session() as session:
  query = select(Bird).where(Bird.name == "Test1 Bird")
  bird = session.execute(query).scalar_one()
  print(bird)
