from flask import Flask as flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urldatabase.db'
db = SQLAlchemy(app)

from models import UrlRepo

#bind function to an url
@app.route('/', methods=['POST', "GET"]) 
def index():
    if request.method == "POST":
        input_url = request.form['url']
        new_url = UrlRepo(url=input_url)

        try:
            db.session.add(new_url)
            db.session.commit()
            return redirect('/phishing_repo')
        
        except:
            db.session.rollback()
            flash("Error adding URL","error")
            return redirect("/")
    
    return render_template('index.html')

@app.route('/phishing_repo', methods=["GET"])
def show_repo():
    url_list = UrlRepo.query.order_by(UrlRepo.timeStamp).all()
    return render_template("repo.html", url=url_list)
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)