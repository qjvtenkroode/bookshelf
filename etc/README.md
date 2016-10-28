# ?!?
All files stored within *etc* are either *config files* or a *passwd* file.

## How does the passwd file work?
The *passwd* file is use to authenticate users to the REST api. To add an entry to the *passwd* file *bookshelf.qkroode.authentication* is used. This piece of code is used to actually authenticate the users but also contains a *main* method which requires some flags. To add an user execute the following: 

`python bookshelf/qkroode/authentication.py --add <username>` 

This will prompt for a password which will be stored in a hashed form.

To delete an user execute the following:

`python bookshelf/qkroode/authentication.py --del <username>`
