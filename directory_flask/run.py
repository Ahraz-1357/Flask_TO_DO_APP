from app import createapp,db
from app.models import Task
app=createapp()



if __name__=="__main__":
    app.run(debug=True)