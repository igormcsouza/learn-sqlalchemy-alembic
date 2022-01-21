# Learn SQLAlchemy with Alembic

## Setup

All the commands you need are listed below. Follow the steps to get ready with
sqlalchemy and alembic everywhere.

1. Initialize the alembic environment, which install a folder and a config file
so we can edit it according to our needs.

2. Edit `alembic.ini` to write down the URI to the database, where it will be
stored all the tables and stuff.

3. Edit `migrations/env.py` which is created on step 1. This part you must
change the lines where the Metadata Object is referenced. Import the Base here
and set the line below.

        target_metadata = Base.metadata.

4. Build your models as wish, just remember base has to be on the same file as
the classes that inherit from Base. On a context of mutiple files, you can have
one file that calls the base and all the classes.

5. Create the revision on autogeneration mode, that makes the version and
generate the file that will be execute on the database. After created review
the file to make sure is as wish.

6. Upgrate the database implementing the recent revision you make. That will
change the database.

7. Go through steps 5 and 6 as much as you need. Always when a new migration
is necessary. For more complex stuff refer the official documentation.

## Useful commands

* Initialize migrations with alembic: Before any other migration command you
need to initialize the alembic, that will create a specific folder and config
file, so we can use to point to our system specifications.

        user$ alembic init migrations

* Create a migration file: This file contains all the changes to be make on
database as well as a downgrade version that helps when a mistake is made and
a rollback is needed. Review the file before applying the changes to make sure
the right things is going to be done.

        user$ alembic revision --autogenerate -m "Message"

* Apply the migrations: Once everything is ok, apply the modifications to the
database.

        user$ alembic upgrade heads
