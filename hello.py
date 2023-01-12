import psycopg2
import psycopg2.extras
from flask import Flask, render_template, request,flash,redirect, url_for
from flask_wtf import FlaskForm,Form
from wtforms import (StringField, SubmitField,TextAreaField ,BooleanField,IntegerField, SelectField,PasswordField,validators)
from wtforms.validators import DataRequired
app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

def toConnect():
	connect= psycopg2.connect(
		database= "jesusaur",
		user = "jesusaurweb",
		password="Dbz3phyrus1",
		host="127.0.0.1",
		port="5432"
	)
	return connect



@app.route('/')
def mainIndex():
	return render_template('mainpage.html')

@app.route('/inventory')
def showview():
	connect = toConnect()
	"""rows returned from postgres are just an ordered list"""
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from inventory_available')
		inventory= c.fetchall()
		print(inventory)
	return render_template('inventoryview.html', inventory=inventory)


@app.route('/manager')
def showmanagerview():
	connect = toConnect()
	"""rows returned from postgres are just an ordered list"""
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from managerinfo')
		contactinfo= c.fetchall()
		print(contactinfo)
	return render_template('managerinfoview.html',contactinfo=contactinfo)

@app.route('/taskcomplete')
def taskcompleteview():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from taskcomplete')
		employeeinfo= c.fetchall()
		print(employeeinfo)
	return render_template('taskcompleteview.html', employeeinfo=employeeinfo)

@app.route('/taskincomplete')
def taskincompleteview():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from taskincomplete')
		employeeinfohelp= c.fetchall()
		print(employeeinfohelp)
	return render_template('taskincompleteview.html', employeeinfohelp=employeeinfohelp)

@app.route('/teaminfo')
def teaminfoview():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from teaminfo')
		teaminfofull= c.fetchall()
		print(teaminfofull)
	return render_template('teaminfoview.html', teaminfofull=teaminfofull)

@app.route('/orderinfo')
def orderinfoview():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from teamorderinfo')
		teamorderinfofull= c.fetchall()
		print(teamorderinfofull)
	return render_template('orderinfoview.html', teamorderinfofull=teamorderinfofull)
	#*******************views end***********

@app.route('/coworker')
def employeetable():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from Employees')
		employee= c.fetchall()
		print(employee)
	return render_template('employees.html',employee=employee)

	#**********not tested on server yet***************

@app.route('/team')
def teamtable():
	connect = toConnect()
	"""rows returned from postgres are just an ordered list"""
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from teams')
		team= c.fetchall()
		print(team)
	return render_template('teams.html',team=team)

@app.route('/teamleader')
def teamleadertable():
	connect = toConnect()
	"""rows returned from postgres are just an ordered list"""
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from team_leaders')
		teamleaders= c.fetchall()
		print(teamleaders)
	return render_template('teamleaders.html',teamleaders=teamleaders)

url = '/experiment'
@app.route(url)
def experimenttable():
	connect = toConnect()
	"""rows returned from postgres are just an ordered list"""

	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from experiments')
		experiment= c.fetchall()
		print(experiment)
	return render_template('experiments.html',experiment=experiment)

@app.route('/task')
def taskstable():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from tasks')
		task= c.fetchall()
		print(task)
	return render_template('tasks.html',task=task)

@app.route('/equipment')
def equipmenttable():
	connect = toConnect()
	"""rows returned from postgres are just an ordered list"""
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from equipment_inv')
		equipment= c.fetchall()
		print(equipment)
	return render_template('equpment.html',equipment=equipment)

@app.route('/disposable')
def disposabletable():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from disposables_inv')
		disposable= c.fetchall()
		print(disposable)
	return render_template('disposables.html',disposable=disposable)

@app.route('/orders')
def disposableordertable():
	"""rows returned from postgres are just an ordered list"""
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		c.execute('select * from disposables_orders')
		disposableorder= c.fetchall()
		print(disposableorder)
	return render_template('orders.html',disposableorder=disposableorder)

@app.route('/Delete/<id>' )
def Delete(id):
	connect = toConnect()
	rows_deleted = 0
	try:	
		cur = connect.cursor()
		cur.execute("delete from Employees where emp_id = %s ",(id,))
		rows_deleted = cur.rowcount
		connect.commit()
		print(id)
		connect.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		connect.commit()

	return render_template('test.html',answer=id)

@app.route('/Deleteteamleader/<id>' )
def Deleteteamleader(id):
	connect = toConnect()
	rows_deleted = 0
	try:	
		cur = connect.cursor()
		cur.execute("delete from team_leaders where emp_id = %s ",(id,))
		rows_deleted = cur.rowcount
		connect.commit()
		print(id)
		connect.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		connect.commit()

	return render_template('test.html',answer=id)

@app.route('/Deleteteam/<id>/<id1>' )
def Deleteteam(id,id1):
	connect = toConnect()
	rows_deleted = 0
	try:	
		cur = connect.cursor()
		cur.execute("delete from teams where team_id = %s  And  emp_id = %s",(id1,id,))
		rows_deleted = cur.rowcount
		connect.commit()
		print(id)
		connect.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		connect.commit()

	return render_template('test.html',answer=id)

@app.route('/Deletetask/<id>/<id1>' )
def Deletetask(id,id1):
	connect = toConnect()
	rows_deleted = 0
	try:	
		cur = connect.cursor()
		cur.execute("delete from tasks where task_id = %s  And  exper_id = %s",(id1,id,))
		rows_deleted = cur.rowcount
		connect.commit()
		print(id)
		connect.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		connect.commit()

	return render_template('test.html',answer=id)

@app.route("/Employeeadd", methods=["GET","POST"])
def addEmployee():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into employees(emp_id,first_name,last_name,dob,address,salary,hire_date,Phone_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);""",(request.form['emp_id'],request.form['first_name'],request.form['last_name'],request.form['dob'],request.form['address'],request.form['salary'],request.form['hire_date'],request.form['Phone_no']))
			flash('Employee has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('employeetable'))
		return render_template("addemployee.html")

@app.route("/experimentsadd", methods=["GET","POST"])
def addexperiments():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into experiments (exper_id,team_id,equipment_type,equip_needed,disposable_type,dispos_needed,completed,result) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);""",(request.form['exper_id'],request.form['team_id'],request.form['equipment_type'],request.form['equip_needed'],request.form['disposable_type'],request.form['dispos_needed'],request.form['completed'],request.form['result']))
			flash('Experiments has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('experimenttable'))
		return render_template("addexperiment.html")

@app.route("/orderssadd", methods=["GET","POST"])
def addorders():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into disposables_orders (disposable_type,ordered_amount,emp_id,total_cost) VALUES(%s,%s,%s,%s);""",(request.form['disposable_type'],request.form['ordered_amount'],request.form['emp_id'],request.form['total_cost']))
			flash('Orders has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('disposableordertable'))
		return render_template("addorders.html")
 
@app.route("/tasksadd", methods=["GET","POST"])
def addtasks():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into tasks(task_id,exper_id,emp_id,completed,result) VALUES(%s,%s,%s,%s,%s);""",(request.form['task_id'],request.form['exper_id'],request.form['emp_id'],request.form['completed'],request.form['result']))
			flash('Tasks has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('taskstable'))
		return render_template("addtasks.html")

@app.route("/disposablessadd", methods=["GET","POST"])
def adddisposables():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into disposables_inv(equipment_type,exper_id,emp_id,completed,result) VALUES(%s,%s,%s,%s,%s);""",(request.form['task_id'],request.form['exper_id'],request.form['emp_id'],request.form['completed'],request.form['result']))
			flash('Tasks has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('disposabletable'))
		return render_template("adddisposable.html")

@app.route("/equipmentadd", methods=["GET","POST"])
def addequipment():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into equipment_inv(equipment_type,inv_available) VALUES(%s,%s);""",(request.form['equipment_type'],request.form['inv_available']))
			flash('Equipment has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('equipmenttable'))
		return render_template("addequipment.html")     

@app.route("/teamadd", methods=["GET","POST"])
def addteam():
    connect = toConnect()
    with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
        if request.method == 'POST':
            c.execute("""Insert into teams(team_id,emp_id) VALUES(%s,%s);""",(request.form['team_id'],request.form['emp_id']))
            flash('Equipment has been successfully added', 'success')
            connect.commit()
            return redirect(url_for('teamtable'))
        return render_template("addteam.html")
           
@app.route("/teamleaderadd", methods=["GET","POST"])
def addteamleaders():
	connect = toConnect()
	with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
		if request.method == 'POST':
			c.execute("""Insert into team_leaders (team_id,emp_id) VALUES(%s,%s);""",(request.form['team_id'],request.form['emp_id']))
			flash('Equipment has been successfully added', 'success')
			connect.commit()
			return redirect(url_for('teamleadertable'))
		return render_template("addteamleader.html")     
@app.route("/employeeupdate", methods=["GET","POST"])
def editemployees():
    connect = toConnect()
    
    with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
        if request.method == 'POST':
            c.execute("""update Employees set first_name = %s,last_name= %s,dob= %s,address= %s,salary= %s,hire_date= %s,Phone_no= %s where emp_id = %s ;""",(request.form['first_name']
        ,request.form['last_name'],request.form['dob'],request.form['address'],request.form['salary'],request.form['hire_date'],request.form['Phone_no'],request.form['emp_id']))
            flash('Employees has been successfully updated', 'success')
            connect.commit()
            return redirect(url_for('employeetable'))
        return render_template("addemployee.html")

@app.route("/experimentsupdate", methods=["GET","POST"])
def editexperiments():
    connect = toConnect()
    
    with connect.cursor(cursor_factory=psycopg2.extras.DictCursor) as c:
        if request.method == 'POST':
            c.execute("""update experiments set team_id = %s,equipment_type= %s,equip_needed= %s,disposable_type= %s,dispos_needed= %s,completed= %s,result= %s where exper_id = %s ;"""
            	,(request.form['team_id'],request.form['equipment_type'],request.form['equip_needed'],request.form['disposable_type'],request.form['dispos_needed'],request.form['completed'],request.form['result'],request.form['exper_id']))
            flash('experiments has been successfully updated','success')
            connect.commit()
            return redirect(url_for('experimenttable'))
        return render_template("addexperiment.html")

if __name__ == '__main__':
	app.run(debug = True)

