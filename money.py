from flask import Flask, session, request, render_template, redirect
app = Flask(__name__)
app.secret_key ='Randoming'

@app.route('/')
def gold():
	if 'gold' not in session:
		session['gold'] = 0
	if 'log' not in session:
		session['log'] = []
	return render_template('money.html')

@app.route('/process', methods=['POST'])
def getgold():
	import random
	ranges = {
		'farm':(10,20),
		'cave':(5,10),
		'house':(2,5),
		'casino':(-50,50),
	}

	building = request.form['building']
	newgold = random.randint(*ranges[building])
	session['gold'] += newgold
	#session['log'].append('Earned %d Gold from %s'%(newgold,building))
	session['log'].append({'amount':newgold,'building':building})
	if len(session['log']) > 5:
		session['log'] = session['log'][-5:]

	return redirect('/')
app.run(debug=True)