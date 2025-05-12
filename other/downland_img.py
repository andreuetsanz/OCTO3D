# !pip install roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="5HYzrdPm6LO8xmXDVn3G")
project = rf.workspace("ai-3d-dvswr").project("3d-39stf")
version = project.version(1)
dataset = version.download("yolov11")
                