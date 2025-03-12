#!/usr/bin/python3
"""Script that deletes all State objects with a name containing letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states with 'a' in their name
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Delete the states
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
