import os

os.environ["LD_PRELOAD"] = os.environ["PWD"] + "/customFormatFunctions.so";
print os.environ["LD_PRELOAD"]
del os.environ["LD_PRELOAD"]
print os.environ["LD_PRELOAD"]

