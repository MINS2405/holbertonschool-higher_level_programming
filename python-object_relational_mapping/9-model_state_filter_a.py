#!/usr/bin/python3
"""Script that lists all State objects containing the letter a"""

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

    # Query State objects containing 'a', ordered by id
    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id)

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
