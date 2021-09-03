from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from flask_mail import Mail
#with open('config.json','r') as c:
#	params=json.load(c)['params']
#	data=json.load(c)['data']
date = datetime.now()
experience = date.year-2019
c={
	"params":
	{
		"local_uri":"mysql://root:@localhost/portfolio",
		"pro_uri":"mysql://upma5o7dhdq9pzi:shivamR@J-123@eu-az-sql-serv1.database.windows.net/ddwhvui12qtl0cl"
	},
	"data":{
		"name":"Shivam Raj Dubey",
		"header":"Web Developer - Freelancer - Full Stack Developer",
		"option1":"Portfolio",
		"option2":"About",
		"option3":"Contact",
		"t-loc":"Location",
		"loc":"India, Asia",
		"email":"admin@theshivam.tech",
		"about-me":"Web Developer, Freelancer, Full Stack Developer",
		"copyright":"Shivam Raj Dubey 2021",
		"about-p1-div1":"This is Shivam Raj Dubey. Freelancer, Web Developer, Full Stack Developer. I know the languages Python, C#, Core Java. I have worked with the python framework Flask.",
		"about-p2-div2":"If you wanna have your digital presence than you can contact me for any Web Development works.",
		"about-p3-div2":"Web Developer | New to AI | FullStack Developer | Python | Flask | C# | Java | JavaScript | Freelancer",
		"por-topic1":"I generaly know three Praogramming Languages- (i.) Python  (ii.) Java(core)  (iii.) C# ",
		"por-topic2":"I'm a Full Stack Developer. I can work on both (i)Frontend & (ii)Backend and can also (iii)manage database. I'm able to create Dynamic Website from Flask framework.",
		"por-topic3":"As before I was practicing my Knowledge. So yet, I haven't worked with any company. But never mind on this as I'm having my full confidence on me and my Knowledge that, I will be able to satisfy you with my work. So you can have faith on me.",
		"por-topic4":"I'm always ready to learn new things. As being a Developer. I always have to learn upcoming things. So that I could present the best version of my self to my clients(you).",
		"por-topic5":"I'm a Reader. I use to read autobiography and biography of success people. I love to know and learn form the experience of the success people like Elon Musk, Jeff Bezos, Bill Gates, Steve Jobs,Warren Buffett,etc.",
		"por-topic6":"While practicing Development. I also learned very usefull skill Content Creation and Designing which enhances the beauty. I can create Content and Design it for you.",
		"por-h1":"Programming Language",
		"por-h2":"Web Development",
		"por-h3":"Experience",
		"por-h4":"I'm always ready to learn New things",
		"por-h5":"I'm a Reader",
		"por-h6":"Content Creation"




	},
	"links":{
		"facebook":"https://www.facebook.com/profile.php?id=100027876074853",
		"twitter":"https://twitter.com/ShivamRajDubey2",
		"linkedin":"https://www.linkedin.com/in/shivam-raj-dubey-5610361ba/",
		"img":{
		"por-img1":"",
		"por-img2":"",
		"por-img3":"",
		"por-img4":"",
		"por-img5":"",
		"por-img6":""
		}
	},
	"gmail":{
	"user":"thshivam.tech@gmail.com",
	"password":"shivamR@J-1911"
	}
 }
params = c['params']
data = c['data']
links = c['links']
gmail = c['gmail']

local_server= True

app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=gmail['user'],
    MAIL_PASSWORD=gmail['password']
)

db = SQLAlchemy(app)
mail = Mail(app)

if (local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['pro_uri']



class Message(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100),unique=False,nullable=False)
    message = db.Column(db.String(200),unique=False,nullable=False)
    phone_num = db.Column(db.VARCHAR(12),unique=True,nullable=False)
    date = db.Column(db.String(12),unique=False,nullable=False)

try:
	@app.route("/",methods=['GET','POST'])
	def home():
		print('123')
		try:
			print('456')
			if request.method == 'POST':
				print('789')
				y = request.form.get('longitude')
				x = request.form.get('latitude')
				print(str(x) +" | "+ str(y))
				body = 'longitude: '+str(y)+' latitude: '+str(x)
				mail.send_message('User Location', sender='thshivam.tech@gmail.com', recipients=['dubeyshivam1911@gmail.com'], body=body)
				return render_template('index.html',data=data,links=links,geo_submit='',submit='/sentMessage')
				#mail.send_message('New Location For theshivam.tech ', sender=[gmail['user']], recipients=[gmail['user']], body=body)
			return render_template('index.html',data=data,links=links,geo_submit='document.forms[0].submit();',submit='/sentMessage')
		except:
			return redirect('/error')
	@app.route('/sentMessage', methods=['POST'])
	def __message__():
		try:
			name=request.form.get('name')
			email=request.form.get('email')
			phone_num=request.form.get('phone')
			message=request.form.get('message')
			body = 'Name: '+name+'| Email: '+email+'| Phone:'+phone_num+'| Message: '+message
			mail.send_message('New message from '+name, sender=email, recipients=[gmail['user']], body=body)
			body = 'Hi '+name+', this is Shivam Raj Dubey. "admin@theshivam.tech" is my email. You can contact me here for any bussiness related Works.'
			mail.send_message('New message from Shivam Raj Dubey', sender='admin@theshivam.tech', recipients=[email], body=body)
			#enter=Message(name=name,email=email,phone_num=phone_num,message=message,date=str(datetime.now()))
			#print('1')
			#db.session.add(enter)
			#print('2')
			#db.session.commit()
			return redirect('/')
		except:
			return redirect('/error')
	@app.route("/post",methods=['GET','POST'])
	def __index__():
	    if request.method == 'POST':
	        y = request.form.get('longitude')
	        x = request.form.get('latitude')
	        print(str(x) +" | "+ str(y))
	        return str(x) +" | "+ str(y)
	    return render_template('geo.html')
	@app.route('/geo')
	def __geo__():
		return render_template('geo.html')
	@app.route('/error')
	def __error__():
		return render_template('error.html')
	@app.route("/<string>")
	def _redirect_(string):
		return redirect('/')
except:
	@app.route('/error')
	def __error__():
		return render_template('error.html')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8081)
'''
	name = request.form.get('name')
	email = request.form.get('email')
	phone = request.form.get('phone')
	message = request.form.get('message')
	print(name + email + phone + message)
    name = db.Column(db.String(100), unique=False,nullable=False)
    email = db.Column(db.String(100),unique=False,nullable=False)
    phone_num = db.Column(db.VARCHAR(12),unique=False,nullable=False)
    message = db.Column(db.String(200),unique=False,nullable=False)
    date = db.Column(db.String(12),unique=False,nullable=False) '''
