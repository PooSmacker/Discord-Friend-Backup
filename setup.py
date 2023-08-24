import subprocess

# Install dependencies using pip
try:
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error installing dependencies: {e}")
    exit(1)  # Exit the script with an error code

# Run main.py
try:
    subprocess.run(['python', 'main.py'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running main.py: {e}")
    exit(1)  # Exit the script with an error code

# If everything succeeded, you can optionally print a success message
print("Setup completed successfully!")
