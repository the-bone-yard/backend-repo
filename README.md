# The Bone Yard -- backend-repo

## Purpose
This repo is meant to serve as the backend portion of The Bone Yard application.

## Contributors

Judtih Pillado
[<img align="left" alt="Judith's GitHub" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />][git-jud]
[<img align="left" alt="Judith's linkedIn | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin-jud]
<br />
<br>
Roberto Rodriguez
[<img align="left" alt="Roberto's github" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />][git-rob]
[<img align="left" alt="Roberto's linkedin' | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin-rob]
<br />
<br>
Travis McKinstry
[<img align="left" alt="Travis github" width="22px" src="https://raw.githubusercontent.com/iconic/open-iconic/master/svg/globe.svg" />][git-trav]
[<img align="left" alt="Travis linkedin' | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />][linkedin-trav]
<br />
<br />
<br />


---
## Set-up

**1.** First decide where you’ll want to keep this project. cd into that directory and make sure you have both Python3 & Django installed (steps **1a** & **1b**).

   **1.a** To check whether or not you havce Python3 installed, type the following commands in the terminal: `python3 --version`. If Python 3.9.1 isn’t what you see, move onto step 1b. If you see that message, move onto step 2.

  **1.b** It’s first best to establish a virtual environment inside which we’ll install both Python and Django. To set this virtual environment up, you’ll need to type the following commands in the same directory where you want this project to live (the one you created in step 1): `python3 -m venv venv`. Whis will create a folder inside your projet which contains the following folders; `bin`, `include`, `lib` and a file called `pyvenv.cfg`. The lib folder contains the standard Python library. The bin folder contains mostly scripts or executable files. The bin is what we’ll use to start a virtual environment. <br>
Now that we have a bin/source file, we’ll start the virtual environment by typing the following command into your terminal: `source venv/bin/activate` or `source env/bin/source`. You should see (venv) behind your normal bash profile (what I see: `(venv) /Users/travisgm/general_coding_practice/practice-python-django-setup)` <br>
Now to install Python3 go to the following link in your choosen internet browser and download whichever version of Python3 fits your system. Python is an open sourced programming language, so downloading it should always be free. A side note: this application uses Python3, not Python.

**2.** Now we’ll install Django. While your virtual environment is running (should still see (venv) in your terminal), type the following command: `pip install django`. This will install Django and you should now be ready to pull this repo down into that same directory. To exist the virtual environment, type the following commands into the terminal: `deactivate`. Note: you don’t need to be in the virtual environment to pull this repo down successfully.

**3.** Lastly, we’ll check to make sure both Django and Python3 have been installed correctly.
Type `ls` in your terminal and you should see: `README.md`, `daboneyard`, `manage.py`, `boneyard`, `db.sqlite3`, `venv`. If you don’t, either exist that directory (cd ..) and look again, or cd into the backend repo that you just pulled down.
Once you are in the right directory, type the following in your terminal: `python3 manage.py runserver`. You might see an error stating that you have pending or unapplied migrations. If that’s the case, you can type the following in the terminal: `python3 manage.py migrate`, but this isn’t necessary to check that the server is working. Either way, if you typed `python3 manage.py runserver`, you should be able to navigate to your preferred web browser and type in the following URL: http://localhost:8000/. You should see an animation and the following message: “The install worked successfully! Congratulations!“.

**4.** Optional testing set-up: In order to test properly you’ll need to make sure you’re first in the right directory on the terminal. First navigate to the `backend/daboneyard` in your terminal. Next, open the project up in your choosen text editor. Make sure the file tree structure looks something like this: `daboneyard/tests/test_first.py`. You don’t need to navigate to that file, just make sure daboneyard has a folder inside called tests and that has a file in there called `test_first.py`. From your terminal, run the following command: `python3 ../manage.py test tests/`. This should give you a series of passing and a few not passing tests.

**5. Running the local host server**
Make sure you’re in backend. If you type ls you should see `README.md`, `daboneyard`, `manage.py`, `boneyard`, `db.sqlite3`, `venv`. If you’re in the right directory, start the virtual environment by typing the following in your terminal: `source venv/bin/activate`, once your virtual environment is running, type the following command: `python3 manage.py runserver`. If you’ve done it all correctly, you should be able to navigate to `http://localhost:8000/` and see your application running.

---
<br />
<br />

## To-Do
- ~~Switch projet from using SQLite to Postgresql(?)~~





[git-jud]: https://github.com/judithpillado
[linkedin-jud]: https://www.linkedin.com/in/judith-pillado/

[git-rob]: https://github.com/robertorodriguez12
[linkedin-rob]: https://www.linkedin.com/in/roberto-j-rodriguez12/

[git-trav]: https://github.com/TravisGM92
[linkedin-trav]: https://www.linkedin.com/in/travis-mckinstry/
