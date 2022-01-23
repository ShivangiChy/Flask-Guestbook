from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from views import main 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy()
db.init_app(app)
#app.register_blueprint(main)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    comment_text = db.Column(db.String(1000))

@app.route('/')
def index():
    comments = Comment.query.all()
    return render_template('index.html', comments=comments)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/sign', methods=['POST'])
def sign_post():
    name = request.form.get('name')
    comment = request.form.get('comment')

    new_comment = Comment(name=name, comment_text=comment)
    db.session.add(new_comment)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

#def create_app():
#    app = Flask(__name__)

#    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

#    db.init_app(app)

#    from .views import main 
#    app.register_blueprint(main)

#    return app