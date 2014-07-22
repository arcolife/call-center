from app import db
#from app.users import constants as USER
from flask.ext.mongoengine.wtf import model_form

# class User(db.Model):

#     __tablename__ = 'users_user'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(120))
#     role = db.Column(db.SmallInteger, default=USER.USER)
#     status = db.Column(db.SmallInteger, default=USER.NEW)
#     #homepage = db.Column(

#     def __init__(self, name=None, email=None, password=None):
#       self.name = name
#       self.email = email
#       self.password = password

#     def getStatus(self):
#       return USER.STATUS[self.status]

#     def getRole(self):
#       return USER.ROLE[self.role]

#     def __repr__(self):
#         return '<User %r>' % (self.name)

class Content(db.EmbeddedDocument):
    title = db.StringField(max_length=120, required=True)
    url = db.StringField()
    children = db.ListField(db.StringField(max_length=30))

class Metadata(db.Document):
    last_modified = db.DateTimeField(help_text='date when last modified')
    date_uploaded = db.DateTimeField(help_text='date published')
    children_count = db.IntField(default=0)

class HomePage(db.EmbeddedDocument):
    name = db.StringField(max_length=50)    
    children = db.ListField(db.EmbeddedDocumentField(Content))
    content = db.EmbeddedDocumentField(Content)
    metadata = db.ReferenceField(Metadata)
    
class User(db.Document):
    username = db.StringField(max_length=50, required=True)
    email = db.StringField(required=True)
    password = db.StringField(required=True) 
    homepage = db.EmbeddedDocumentField(HomePage)
    role = db.StringField(max_length=20)
    status = db.StringField(max_length=10)
    session = db.DictField() #db.StringField() 
    tags = db.ListField(db.StringField(max_length=30))

    #_id
    
# UserForm = model_form(User)

# def add_user(request):
#     form = UserForm(request.POST)
#     if request.method == 'POST' and form.validate():
#         # do something
#         redirect('done')
#     return render_response('add_user.html', form=form)
