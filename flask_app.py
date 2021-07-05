from flask import request,Flask,render_template
import numpy as np
from tensorflow.keras.models import load_model
from pickle import load,dump
import json
import os
with open("disease.pkl","rb") as d:
    disease=load(d)
with open("symptoms.pkl","rb") as s:
    symptoms=load(s)
med_model=load_model("med-classification.h5")


#IMAGE_FOLDER = os.path.join('new folder', 'images')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict', methods = ['GET','post'])
def index():
    if request.method == 'POST':
      print("try")
      print("error")
      multiselect = request.form.getlist('framework[]')
      inp=[]
      if multiselect != [] :
        for i in symptoms:#
            if i not in multiselect:
               #print(i,'0')
               inp.append(0)
            else:
                #print(i,"#######3")
                inp.append(1)
        c=(model.predict(x) > 0.5).astype("int32")#med_model.predict(np.expand_dims(inp,0))
        print("predicted class :",c)
        res=disease[int(c)-1]
        with open('medline2.json',"rb") as jod :
            jod_1=json.load(jod)
            med_1=jod_1[res]
       
        # print({ key.rstrip('[]'):form.getlist(key) if key.endswith('[]') else form.getvalue(key) for key in form.keys() if compare_with.get(key)!=form.getvalue(key) })

        return render_template('flask_result_1.html',cool=multiselect,result=res,medicine_1=med_1)
      else:
          return render_template('index_1.html')    
if __name__ == "__main__":
    app.run()