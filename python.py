response = requests.post("https://detect.roboflow.com/safetyobjectdetection/1?api_key=AB2PH7hlm0Wcfyii4x72}", data=m, headers={'Content-Type': m.content_type})
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
