from openvino import Core

core = Core()
available_devices = core.available_devices
print("Available OpenVINO devices:", available_devices)