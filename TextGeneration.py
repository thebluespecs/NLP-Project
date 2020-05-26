import subprocess

# Instaling requirements 
Requirments = subprocess.run(["pip3", "install", "-r", "requirements.txt"])
print("The exit code was: %d" % Requirments.returncode)

# Tensorflow version
TfVersion = subprocess.run(["pip3", "install", "tensorflow==1.13.1"])
print("The exit code was: %d" % TfVersion.returncode)

# Download pretraied GPT-2
DownPretrained = subprocess.run(["python3", "download_model.py", "345M"])
print("The exit code was: %d" % DownPretrained.returncode)

UTF = subprocess.run(["export", "PYTHONIOENCODING=UTF-8"])
print("The exit code was: %d" % UTF.returncode)

# Finetuning the model
Training = subprocess.run(["PYTHONPATH=src", "./train.py", "--dataset", "./data/ASOIAF.txt", "--model_name", "'345M'"])
print("The exit code was: %d" % Training.returncode)

# Testing
TestScript = 'python3 src/generate_unconditional_samples.py --temperature 0.8 --top_k 50 --model_name "345M"  | tee /tmp/samples' #enter the test command with args here.
Testing = subprocess.run(TestScript.split(" "))
print("The exit code was: %d" % Testing.returncode)