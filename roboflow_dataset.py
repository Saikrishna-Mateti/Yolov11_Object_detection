from roboflow import Roboflow

rf = Roboflow(api_key="KCaSBABRf8G7xiPtu9rA")
project = rf.workspace("university-of-peradeniya-5ywn6").project("final-lmoyv")
version = project.version(1)
dataset = version.download("yolov11")
print(f"Dataset downloaded to: {dataset.location}")