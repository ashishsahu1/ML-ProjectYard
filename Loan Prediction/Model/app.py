from flask import Flask,render_template,request
#from sklearn.externals import joblib
import numpy as np
import pickle
import sklearn


app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prediction',methods=['POST'])
def prediction():
    depen = (request.form['Dependents'])
    if depen=='3+':
        depen=3
    else:
        depen=int(depen)
    appl_inc = float(request.form['ApplicantIncome'])
    coappl_inc = float(request.form['CoapplicantIncome'])
    LoanAm = float(request.form['LoanAmount'])
    loan_am_tr = float(request.form['Loan_Amount_Term'])
    cred_hist=request.form['Credit_History']
    
    if cred_hist=='Yes':
        cred_hist=1
    else:
        cred_hist=0
    gen=request.form['gender']
    
    if gen=='Male':
        gen=1
    else:
        gen=0
        
    
    marr = request.form['Married']
    
    if marr=='Yes':
        marr=1
    else:
        marr=0
        
    edu = request.form['Education']
    
    if edu=='Not Married':
        edu=1
    else:
        edu=0
    self_emp= request.form['Self_employed']
    
    if self_emp=='Yes':
        self_emp=1
    else:
        self_emp=0
        
    prop_ar = request.form['Property_Area']
    
    if prop_ar=='Semi Urban':
        Semiurban=1
        Urban=0
    if prop_ar=='Urban':
        Semiurban=0
        Urban=1
    else:
        Semiurban=0
        Urban=0
    
    input=np.array([depen,appl_inc,coappl_inc,LoanAm,loan_am_tr,cred_hist,gen,marr,edu,self_emp,Semiurban,Urban])
    print(input)
    input=input.reshape(1,-1)
    predict = model.predict(input)
    if predict==1:
        output="Yes"
    else:
        output="No"
    return render_template('index.html',pred_text="Loan Approved? "+ output)
if __name__ == "main":
    app.run(debug=True)

    