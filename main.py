
from flask import Flask , render_template , request , jsonify
from  Models.utils import MedicalInsurance
import config

app=Flask(__name__)

@app.route("/")
def hello_flask():
    print("welocome to Medical insurance charges prediction")

    return render_template("index.html")


@app.route("/predict_charges",methods=["GET","POST"])
def get_insurance_charges():

    if request.method=="GET":
        print("we are using GET methiod")



        # data = request.form
        # print("Data ::",data)
        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker']
        # region = data['region']
    

        age = eval(request.args.get("age"))
        sex = request.args.get("sex")
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')
   
        print("age,sex,bmi,children,smoker,region  \n",age,sex,bmi,children,smoker,region)


        med_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges=med_ins.get_predicted_price()

        return render_template("index.html",prediction=charges)

        #return jsonify({"result":f"predicted charges for Medical Insurance is {charges}/- Rs. only"})
    

    else:

        print("we are using post method")

        age = eval(request.form.get("age"))
        sex = request.form.get("sex")
        bmi = eval(request.form.get('bmi'))
        children = eval(request.form.get('children'))
        smoker = request.form.get('smoker')
        region = request.form.get('region')


        print("age,sex,bmi,children,smoker,region  \n",age,sex,bmi,children,smoker,region)



        med_ins=MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges=med_ins.get_predicted_price()

        return render_template("index_html",prediction=charges)
        
        #return jsonify({"result":f"predicted charges for Medical Insurance is {charges}/- Rs. only"})
    
   

       

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)