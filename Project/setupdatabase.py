from app import db, Poll_Result

#Creates all the tabels
db.create_all()

spyken = Poll_Result('Spyken', 'Var maten god?', 3,2)
polhem = Poll_Result('Polhem', 'Var maten god?',4,1)

#None
#None
print(spyken.id)
print(polhem.id)

db.session.add_all([spyken,polhem])

db.session.commit()

print(spyken.id)
print(polhem.id)
