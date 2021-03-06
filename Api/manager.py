# -*- coding: utf-8 -*-
import os
from app import create_app, Config
from app.Extensions import db
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server, Command
from app.Models import db_Account

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db',MigrateCommand)
manager.add_command("runserver", Server(host=Config.RUNHOST, port=Config.RUNPORT, use_debugger=Config.USEFLASKDEBUG))

if __name__ == '__main__':
    manager.run()
