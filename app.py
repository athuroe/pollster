# app.py
from Project import app,db
from flask import render_template,redirect,request,url_for
from Project.models import Poll_Result, PollTable
from datetime import date

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poll')
def poll():
    location = request.args.get('location')
    question = request.args.get('question')
    return render_template('poll.html', location=location, question=question)

@app.route('/results')
def results():
    rows = Poll_Result.query.all()
    table = PollTable(rows)
    return render_template('results.html', table=table)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add_one', methods=["POST", "GET"])
def add_one():
    face =  request.json[0]['face']
    today = date.today()
    location = request.args.get('location')
    question = request.args.get('question')

    #code that updates database here
    if (face == 'happy'):
        row_to_update = Poll_Result.query.filter_by(date=today).filter_by(location=location).filter_by(question=question).first()
        #If row does not exist, add one with happy_count=1
        if (row_to_update is None):
            print(row_to_update)
            new_row = Poll_Result(today,location,question,1,0)
            db.session.add(new_row)
            db.session.commit()
        #Else update existing row with happy_count+1
        else:
            print(row_to_update)
            row_to_update.happy_count = row_to_update.happy_count + 1
            db.session.add(row_to_update)
            db.session.commit()
    else:
        row_to_update = Poll_Result.query.filter_by(date=today).filter_by(location=location).filter_by(question=question).first()
        #If row does not exist, add one with sad_count=1
        if (row_to_update is None):
            print(row_to_update)
            new_row = Poll_Result(today,location,question,0,1)
            db.session.add(new_row)
            db.session.commit()
        #Else update existing row with sad_count+1
        else:
            print(row_to_update)
            row_to_update.sad_count = row_to_update.sad_count + 1
            db.session.add(row_to_update)
            db.session.commit()

    return json.dumps({'status':'OK','face':face});

@app.route('/delete/<int:id>')
def delete(id):
    row_to_delete = Poll_Result.query.get(id)
    db.session.delete(row_to_delete)
    db.session.commit()
    return redirect('/results')

if __name__ == '__main__':
    app.run(debug=True)
