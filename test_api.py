import os
import requests
import platform
from dotenv import load_dotenv

load_dotenv()

GTOKEN = os.getenv('GIT_TOKEN')
GUSER = os.getenv('GIT_USER')

headers = {
  "Authorization": f"token {GTOKEN}",
  "Accept": "application/vnd.github.v3+json"
}

main_url = f"https://api.github.com/"

def new_repo():
  data = {
    "name": "test_public_repo_api",
    "description": "Testing repo",
    "private": False
  }
  url = f"{main_url}/user/repos"
  response = requests.post(url, headers=headers, json=data)
  if response.status_code == 201:
    print("Repository succesfully created!")
  else:
    print(f"Failed to create repository: {response.status_code} - {response.text}")
    
def repo_status():
  response = requests.get(f"{main_url}/users/{GUSER}/repos", headers=headers)
  if response.status_code == 200:
    repo_list = response.json()
    names = [repo['name'] for repo in repo_list]
    if "test_public_repo_api" in names:
      print("Repo exists")
    else:
      print('Existing repo "test_public_repo_api" not found')
  else:
    print(f"Failed to load repositories: {response.status_code} - {response.text}")

def delete_repo():
  response = requests.delete(f"{main_url}/repos/{GUSER}/test_public_repo_api", headers=headers)
  if response.status_code == 204:
    print("Test repository successfuly deleted")
  else:
    print(f"Repository wasn't deleted: {response.status_code} - {response.text}")

def menu():
  while True:
    clear()
    print("Choose an option:")
    print("1 - Create test repository")
    print("2 - Check if test repository exists")
    print("3 - Delete test repository")
    print("4 - Exit")
    inp = input()
    if inp == "1": 
      new_repo()
      pause()
    elif inp == "2":
      repo_status()
      pause()
    elif inp == "3":
      delete_repo()
      pause()
    elif inp == "4":
      break
    else:
      print("Such option doesn't exist")
      
def clear():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")

def pause():
  if platform.system() == "Windows":
    os.system('pause')
  else:
    input("Press any key to continue")
      
menu()