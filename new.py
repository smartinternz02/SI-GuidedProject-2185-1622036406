import requests

import json

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "NvokqgAR4YeEhYX5rzhIH865PIufQSM91alFNvIG_NcO"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
print("mltoken",mltoken)
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
#payload_scoring = {"input_data": [{"field": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}
payload_scoring = {"input_data": [{"field": ["Year","D.O","Conductivity","B.O.D", "Nitratenen","Total Coliform"], 
                                   "values": [5.500e+00, 7.400e+00, 6.350e+02, 8.800e+00, 5.080e+00, 5.500e+03,2.012e+03,
                                              8.100e+00, 5.690e+02, 8.200e+00, 1.600e+00, 1.028e+00, 6.050e+03,2.003e+03]}]}
response_scoring = requests.post('https://eu-gb.ml.cloud.ibm.com/ml/v4/deployments/f5f78152-d99a-4d7c-9df0-c1074312a69b/predictions?version=2021-06-09', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print("predictions")
predictions=response_scoring.json()

