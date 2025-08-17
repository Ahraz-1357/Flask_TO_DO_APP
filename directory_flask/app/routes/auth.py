from flask import Flask,redirect,render_template,flash,request,Blueprint,session,url_for
auth_bp=Blueprint('auth',__name__)
USER_CREDENTIALS={
    "username":"admin",
    "password":"1234"
}
@auth_bp.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username==USER_CREDENTIALS["username"] and password==USER_CREDENTIALS["password"]:
            session['user']=username
            flash("login Successful","success")
        else:
            flash("Invalid Credentials",'Danger')
            return render_template("login.html")
    return render_template("login.html")

@auth_bp.route('/logout')
def logout():
    session.pop('user',None)
    flash("Logged out succesfully",'info')
    return redirect(url_for('auth.login'))

    