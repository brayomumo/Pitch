from app import create_app,db
from flask_script import Manager, Server
from app.models import User, Pitch
from flask_migrate import Migrate, MigrateCommand

#Create app instance 
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app,db)
migrate.add_command('db', MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Review = Review)

if __name__=='__main__':
    manager.run()
