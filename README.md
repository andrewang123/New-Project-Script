# Project Title

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)
+ [Usage](#usage)

## About <a name = "about"></a>
The purpose of this project is to be able to automate the process of create a project on GitHub syncing it locally. You can run the command anywhere on the terminal and it will create the project in a hardcoded location.

## Getting Started <a name = "getting_started"></a>


### Prerequisites

1. Installing pygithub (python package used to integrate with the Github API). This will install pygithub globally so you do not have to mess with virtualenv

```
sudo -H pip install pygithub
```
2. Open the terminal and cd to your root directory. Then open up your editor of choice. Add the the following lines in your .bash_profile. **Make sure you change the username and password to your own credentials and the path of the macUsername**
```
export GIT_USERNAME=“username”
export GIT_PASSWORD=“password”
export PATH=$PATH:/Users/[macUsername]/bin
alias create=create.sh
```
3. Ensure you have python 3.6, python 3.7 is does not support pytorch as of the date the script was written.

4. Make a bin folder inside your /Users/[macUsername] directory.

### Steps after Copying Repo

1. Put the create.py file in the folder based on line 3. (Make sure you change the path to match your own file structure)
2. Change line 6 of the python script to match where you put all of your projects
3. Change line 11 to be your git repository name
4. Put the create file inside the /Users/[macUsername]/bin directory
5. chmod u+x create where the shell script is located to change it into an executable.
## Usage <a name = "usage"></a>

```
create [reponame]
```
Now you can create a repository inside your specified project folder!
