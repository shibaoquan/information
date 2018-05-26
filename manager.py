from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import app, db


# 创建骄脚本管理器对象
manager = Manager(app)
Migrate(app, manager)
manager.add_command("db", MigrateCommand)



@app.route('/')
def index():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
