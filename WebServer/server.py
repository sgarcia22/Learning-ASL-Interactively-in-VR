from flask import Flask, jsonify, render_template, request
import onnxruntime as rt
import urllib.request
import numpy as np

sample = [
  52.56806946, 40.84261703,	45.27545929,	54.09841919,	30.32644272,	44.74907684,	39.30120087	,33.68500519,	21.95171738	,41.67057037,	37.61446762,	33.2915802,	22.98773384,	37.55997467	,34.66792297	,32.11828232	,33.86571503,	39.50741577	,34.69207764,	30.40076637
]

app = Flask(__name__)

#Get Model
url = 'https://cdn.glitch.com/4a066ef1-9c42-4c50-88b6-f259c389a9d3%2Fleap_asl_model.onnx?v=1572718269098'
response = urllib.request.urlopen(url)
sess = rt.InferenceSession(response.read())

#Get Input and Output Names
input_name = sess.get_inputs()[0].name
output_name = sess.get_outputs()
output_label = output_name[0].name
output_probability = output_name[1].name

#Run Predition - Example
#pred_onx = sess.run(None, {input_name: np.array([sample]).astype(np.float32)})
#print(pred_onx[1])

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_bone_data():
    js_data = request.json
    print(list(js_data['data'])) #TODO - FIX
    return jsonify(js_data)


# listen for requests
if __name__ == "__main__":
    app.debug = True
    app.run()