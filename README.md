# TPProfesional

I assume you have installed git. If not, you can easily install using:

sudo apt-get install git

on Ubuntu or Mint distros.

Then, login to your Github account and create a new repository, name the repository and add a readme file.

Open terminal and cd to your project directory (to the root of your project).

If you have already initialized this directory as a git repository and you already have all the changes committed locally then do nothing else in terminal type:

git init

This initializes a git repository in your project folder. Then type:

git add . 

'dot' (.) is used to add all files in a directory to a repository. Then type:

git commit -m "some meaningful message goes here"

messages are used to know about what new changes are committed.

Next type in terminal:

git remote add origin https://github.com/your-user-name/name-that-you-gave-to-repository.git 

This creates a remote, named “origin”pointing at the GitHub repository you just created.

This step is sometimes necessary.
Type in terminal:

git pull origin master

Next type in terminal:

git push -u origin master

Then it will ask for your username and password. After you have given correct username and password, your files will be pushed to your Github repository.

Afterwards, for every change(s) you make, you have to add and commit such changes. Then do:

git push

This will push all your changes to your Github repository.
