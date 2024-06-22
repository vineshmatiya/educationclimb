from flask import *  
app = Flask(__name__)  

app.secret_key = 'vinesh'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check username and password (this is a simple example, you should use a more secure method)
        if username == 'vinesh' and password == '12345':
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template("register.html")
  
@app.route('/')  
def home():  
    if 'logged_in' in session and session['logged_in']:
        return render_template('home.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/contact')
def contact():
    if 'logged_in' in session and session['logged_in']:
        return render_template('contact.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/aboutus')
def aboutus():
    if 'logged_in' in session and session['logged_in']:
        return render_template('aboutus.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning')
def logicalreasoning():
    if 'logged_in' in session and session['logged_in']:
        return render_template('logicalreasoning.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning/bloodrelation')
def bloodrelation():
    if 'logged_in' in session and session['logged_in']:
        return render_template('bloodrelation.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning/clockandcalender')
def clockandcalender():
    if 'logged_in' in session and session['logged_in']:
        return render_template('clockandcalender.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning/codingdecoding')
def codingdecoding():
    if 'logged_in' in session and session['logged_in']:
        return render_template('codingdecoding.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning/direction')
def direction():
    if 'logged_in' in session and session['logged_in']:
        return render_template('direction.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning/numberandletterseries')
def numberandletterseries():
    if 'logged_in' in session and session['logged_in']:
        return render_template('numberandletterseries.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/logicalreasoning/seatingarrangment')
def seatingarrangment():
    if 'logged_in' in session and session['logged_in']:
        return render_template('seatingarrangment.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude')
def quantitiveapptitude():
    if 'logged_in' in session and session['logged_in']:
        return render_template('quantitiveapptitude.html', username=session['username'])
    else:
        return redirect(url_for('login'))  

@app.route('/quantitiveapptitude/average')
def average():
    if 'logged_in' in session and session['logged_in']:
        return render_template('average.html', username=session['username'])
    else:
        return redirect(url_for('login'))  

@app.route('/quantitiveapptitude/ciandsi')
def ciandsi():
    if 'logged_in' in session and session['logged_in']:
        return render_template('ciandsi.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude/hcfandlcm')
def hcfandlcm():
    if 'logged_in' in session and session['logged_in']:
        return render_template('hcfandlcm.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude/percentage')
def percentage():
    if 'logged_in' in session and session['logged_in']:
        return render_template('percentage.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude/profitlossanddiscount')
def profitlossanddiscount():
    if 'logged_in' in session and session['logged_in']:
        return render_template('profitlossanddiscount.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude/ratioandportion')
def ratioandportion():
    if 'logged_in' in session and session['logged_in']:
        return render_template('ratioandportion.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude/timeandwork')
def timeandwork():
    if 'logged_in' in session and session['logged_in']:
        return render_template('timeandwork.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quantitiveapptitude/timespeedanddistance')
def timespeedanddistance():
    if 'logged_in' in session and session['logged_in']:
        return render_template('timespeedanddistance.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/verbalability')
def verbalability():
    if 'logged_in' in session and session['logged_in']:
        return render_template('verbalability.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/verbalability/analog')
def analog():
    if 'logged_in' in session and session['logged_in']:
        return render_template('analog.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/verbalability/lrreadingcomprehension')
def lrreadingcomprehension():
    if 'logged_in' in session and session['logged_in']:
        return render_template('lrreadingcomprehension.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/verbalability/spottheerror')
def spottheerror():
    if 'logged_in' in session and session['logged_in']:
        return render_template('spottheerror.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/verbalability/statementandconclusion')
def statementandconclusion():
    if 'logged_in' in session and session['logged_in']:
        return render_template('statementandconclusion.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

@app.route('/quiz')
def quiz():
    if 'logged_in' in session and session['logged_in']:
        return render_template('quiz.html', username=session['username'])
    else:
        return redirect(url_for('login')) 

if __name__ == '__main__':  
    app.run(debug = True)  