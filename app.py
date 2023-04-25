from website import create_app, db
from flask_migrate import init,stamp,migrate,upgrade

#Runs our application
app = create_app()
app.app_context().push()
db.create_all()



if __name__=='__main__':
 app.run(debug=True)
