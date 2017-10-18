import sys
import csv

from CTFd import create_app
from CTFd.models import db, Teams

def import_teams(filename):
    with open(filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            user_name = row['user_name'].decode("gbk")
            team_name = row['team_name'].decode("gbk")
            password = row['password'].decode("gbk")
            email = row['email'].decode("gbk")
            team = Teams(
                user_name=user_name,
                name=team_name,
                password=password,
                email=email)
            team.verified = True
            team.affiliation = row['school'].decode("gbk")
            db.session.add(team)
            print(team)
        db.session.commit()
        db.session.close()


app = create_app()
with app.app_context():
    import_teams(sys.argv[1])

