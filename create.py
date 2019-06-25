import os
import sys
from github import Github

username = os.environ.get('GIT_USERNAME')
password = os.environ.get('GIT_PASSWORD')
repoName = sys.argv[1];

# Github API
g = Github(username, password)
user = g.get_user()
repo = user.create_repo(repoName)

print("Repository: " + repoName + " has successfully been created!")
print("\n")
print("\n")
print("\n")