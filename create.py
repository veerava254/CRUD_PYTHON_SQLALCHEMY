from main import Bird, Session

with Session() as session:
  new_bird = Bird(name="Test2 Bird")
  session.add(new_bird)
  session.commit()
