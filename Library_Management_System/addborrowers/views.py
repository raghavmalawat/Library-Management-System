from django.shortcuts import render
from django.db import connection
from .models import Borrower

cursor = connection.cursor()
query = "ALTER TABLE Borrower AUTO_INCREMENT=1000;"
cursor.execute(query)
def index(request):
	ssnexist = False
	message = ""
	if(request.method == "POST"):
		fname = request.POST['fname']
		ssn = request.POST['ssn']
		address = request.POST['address']
		phone = request.POST['phone']
		#query = "call reset_autoincrement('Borrower'); "
		#cursor.execute(query)
		query = "SELECT Ssn FROM Borrower WHERE Ssn = '" + ssn + "'"
		cursor.execute(query)

		if(cursor.fetchone() != None):
			ssnexist = True
			query = "SELECT Card_id FROM Borrower WHERE Ssn = '" + ssn + "'"
			cursor.execute(query)
			message = "SSN already exists.The card number is:"+str(cursor.fetchone()[0]);
		else:
			query = 'INSERT INTO Borrower(Ssn,Bname,Address,Phone) VALUES("'+ ssn +'","'+ fname +'","'+ address +'","'+ phone +'");'
			cursor.execute(query)
			query = "SELECT Card_id FROM Borrower WHERE Ssn = '" + ssn + "'"
			cursor.execute(query)
			message = "Successfully added the borrower.The card number is:"+str(cursor.fetchone()[0]);

	return render(request,'addborrowers/index.html',{'ssnexist':ssnexist,'message':message})
