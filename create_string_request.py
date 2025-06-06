import base64
import requests
import tensorflow as tf  # Pastikan TensorFlow terinstall

# Contoh data input (disesuaikan dengan fitur model)
input_data = {
    "customerID": "7590-VHVEG",  # Added customerID as required by the model
    "gender": "Female",
    "SeniorCitizen": "No",  # String for SeniorCitizen as per error
    "Partner": "Yes",
    "PhoneService": "No",
    "PaperlessBilling": "Yes",
    "InternetService": "DSL",     # Changed to match the sample data
    "StreamingTV": "No",
    "tenure": 1,            # Int64 for tenure as per error (changed to match sample)
    "MonthlyCharges": 29.85, # Keeping as float (changed to match sample)
    "TotalCharges": 29.85    # Keeping as float (changed to match sample)
}

# 1. Membuat fitur untuk tf.train.Example - dengan tipe data yang tepat
feature_dict = {}
# String features
feature_dict["customerID"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["customerID"].encode()]))
feature_dict["gender"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["gender"].encode()]))
feature_dict["SeniorCitizen"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["SeniorCitizen"].encode()]))
feature_dict["Partner"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["Partner"].encode()]))
feature_dict["PhoneService"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["PhoneService"].encode()]))
feature_dict["PaperlessBilling"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["PaperlessBilling"].encode()]))
feature_dict["InternetService"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["InternetService"].encode()]))
feature_dict["StreamingTV"] = tf.train.Feature(bytes_list=tf.train.BytesList(value=[input_data["StreamingTV"].encode()]))

# Int64 features
feature_dict["tenure"] = tf.train.Feature(int64_list=tf.train.Int64List(value=[input_data["tenure"]]))

# Float features
feature_dict["MonthlyCharges"] = tf.train.Feature(float_list=tf.train.FloatList(value=[input_data["MonthlyCharges"]]))
feature_dict["TotalCharges"] = tf.train.Feature(float_list=tf.train.FloatList(value=[input_data["TotalCharges"]]))

example_proto = tf.train.Example(features=tf.train.Features(feature=feature_dict))

# 2. Serialisasi Example menjadi string biner
serialized_example = example_proto.SerializeToString()

# 3. Encode string biner tersebut ke format base64
b64_example = base64.b64encode(serialized_example).decode('utf-8')

# 4. Membuat payload JSON dengan contoh ter-encode base64
payload = {
    "instances": [
        { "examples": { "b64": b64_example } }
    ]
}

# 5. Mengirim request HTTP POST ke TensorFlow Serving
url = "https://ml-ops-telco-production.up.railway.app/v1/models/cc-model:predict"  # Fix: removed double slash
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=payload, headers=headers)

# 6. Cetak hasil prediksi
print(response.json())
