from flask import Flask as flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#database Schema
class UrlRepo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(250), nullable = False)
    target = db.Column(db.Integer, default = 0)
    timeStamp = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<URL: %r>' % self.url

#bind function to an url
@app.route('/home', methods=['POST','GET']) 
def index():

    if request.method == 'POST':
        input_url = request.form['url']
        new_url = UrlRepo(url=input_url)

        try:
            db.session.add(new_url)
            db.session.commit()
            url = UrlRepo.query.order_by(UrlRepo.timeStamp).all()
            return render_template('repo.html', url=url)
            #return redirect('repo.html', url=url)
        
        except:
            return "Cannot add URL to the repo"

    else:
        return render_template('index.html')

@app.route('/phishing_repo')
def show_repo():
    return render_template('repo.html')

# @app.route('/dynamicURL/<username>')
# def show_user(username):
#     return f"Hello {username}!"

if __name__ == "__main__":
    app.run(debug=True)