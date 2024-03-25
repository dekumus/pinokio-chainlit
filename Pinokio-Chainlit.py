# Pinokio One-Click Install Script for Chainlit

# This script will install Chainlit using the provided GitHub repository URL

import os
import subprocess

def install_chainlit():
    # Define the GitHub repository URL
    repo_url = "https://github.com/Chainlit/chainlit.git"
    
    # Clone the repository
    subprocess.run(["git", "clone", repo_url])
    
    # Change directory to the cloned repository
    os.chdir("chainlit")
    
    # Install dependencies (you can customize this part if needed)
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    
    # Print success message
    print("Chainlit has been successfully installed!")

# Call the install_chainlit function
install_chainlit()
