#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

def seed_database(session, num_records):
    print(f"Seeding {num_records} records into the database...")

    games = [
        Game(
            title=fake.name(),
            genre=fake.word(),
            platform=fake.word(),
            price=random.randint(0, 60)
        )
        for _ in range(num_records)
    ]

    session.bulk_save_objects(games)
    session.commit()

if __name__ == '__main__':
    # Adjust the database URL as needed
    engine = create_engine('sqlite:///seed_db.db')

    # Bind the engine to the session
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()

    # Specify the number of records you want to seed
    num_records_to_seed = 50

    # Call the seed_database function to seed the database
    seed_database(session, num_records_to_seed)

    print("Seeding completed.")
