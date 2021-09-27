from flask import Flask , request, render_template
import numpy as np
import tensorflow as keras
import tensorflow as tf
model = tf.keras.models.load_model('abc.h5')

# Check its architecture
model.summary()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/infoo', methods=['GET', 'POST'])
def info():
    if request.method =="GET":
        pass
    elif request.method == "POST":
        print(model.summary)
        print(request.form['height'])
        integer= np.int64([[request.form['height']]])
        a = model.predict(integer)
        # return 'Data is showing in post method and the predction for height {}and the predicted weight is  <br> {}  '.format( request.form['height'],a) 
        dic = {'Height':integer, 'Prediction-of-Weight':a}
        return render_template('pred.html',pred=dic )

app.run(debug=True)
 