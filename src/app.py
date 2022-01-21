from src.models import UserModel, session_maker


def main():

    first_name = input("Type your first name: ")

    # create a user
    user = UserModel(first_name=first_name)

    # Add the user to the database
    with session_maker() as session:
        session.add(user)
        session.commit()