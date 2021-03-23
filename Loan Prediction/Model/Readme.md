# Loan_Prediction


In this problem, I have used dataset from kaggle - https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset

Dataset Description- There are 12 fields.

1] **Loan ID** -> As the name suggests each person should have a unique loan ID.

2] **Gender** -> In general it is male or female. No offence for not including the third gender.

3] **Married** -> Applicant who is married is represented by Y and not married is represented as N. The information regarding whether the applicant who is married is divorced or not has not been provided. So we don’t need to worry regarding all these.

4] **Dependents** -> the number of people dependent on the applicant who has taken loan has been provided.

5] **Education** -> It is either non -graduate or graduate. The assumption I can make is “ The probability of clearing the loan amount would be higher if the applicant is a graduate”.

6] **Self_Employed** -> As the name suggests Self Employed means , he/she is employed for himself/herself only. So freelancer or having a own business might come in this category. An applicant who is self employed is represented by Y and the one who is not is represented by N.

7] **Applicant Income** -> Applicant Income suggests the income by Applicant.So the general assumption that i can make would be “The one who earns more have a high probability of clearing loan amount and would be highly eligible for loan ”

8] **Co Applicant income** -> this represents the income of co-applicant. I can also assume that “ If co applicant income is higher , the probability of being eligible would be higher 

9] **Loan Amount** -> This amount represents the loan amount in thousands. One assumption I can make is that “ If Loan amount is higher , the probability of repaying would be lesser and vice versa”

10] **Loan_Amount_Term** -> This represents the number of months required to repay the loan.

11] **Credit_History** -> When I googled it , I got this information. A credit history is a record of a borrower’s responsible repayment of debts. It suggests → 1 denotes that the credit history is good and 0 otherwise.

12] 
**Loan_Status** -> If the applicant is eligible for loan it’s yes represented by Y else it’s no represented by N.
The predictions are done using Logistic Regression model. The model has been deployed using Flask and Heroku cloud.


# Screenshots

![Image](https://user-images.githubusercontent.com/60662775/111327628-8e42f780-8693-11eb-994a-d2bee2cece5c.png)
