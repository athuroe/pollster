# models.py
from Project import db
from flask_table import Table, Col, LinkCol

#### MODELS ####

class Poll_Result(db.Model):

    # Manual table name choice
    __tablename__ = 'result'

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    location = db.Column(db.Text)
    question = db.Column(db.Text)
    happy_count = db.Column(db.Integer)
    sad_count = db.Column(db.Integer)

    def __init__(self,date,location,question,happy_count,sad_count):
        self.date = date
        self.location = location
        self.question = question
        self.happy_count = happy_count
        self.sad_count = sad_count

    def __repr__(self):
        return f"{self.location} has {self.happy_count} happy customers and {self.sad_count} sad customers"

#### Table to view results ####

class PollTable(Table):
    id = Col('id')
    date = Col('date')
    location = Col('location')
    question = Col('question')
    happy_count = Col('happy_count')
    sad_count = Col('sad_count')
    delete = LinkCol('Delete','delete',url_kwargs=dict(id='id'))
