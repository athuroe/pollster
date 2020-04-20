from app import db, Poll_Result

## READ ##
all_results = Poll_Result.query.all() # list of puppy objects in the table
print (all_results)

my_result = Poll_Result('Katte','Var maten god?',5,10)
db.session.add(my_result)
db.session.commit()

all_results = Poll_Result.query.all() # list of puppy objects in the table
print (all_results)
