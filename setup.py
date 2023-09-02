import subprocess

try:
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error installing dependencies: {e}")
    exit(1)

try:
    subprocess.run(['python', 'main.py'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running main.py: {e}")
    exit(1)  # Exit the script with an error code

print("Setup completed successfully!")
