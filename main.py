from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///projektai.db')
Session = sessionmaker(bind=engine)
session = Session()

projektas1 = Projektas("Projektas1", 20000)
projektas2 = Projektas("Projektas2", 45000)
session.add(projektas1)
session.add(projektas2)
session.commit()
