As issues using our methods are raised we will update this section with relevant information to resolve said issue. Providing a resource to help fix these issues as they occur in the future.  
  
#### Issues accessing a method on GitHub:  
When following the links to the projects stored on GitHub you may receive a 404 error. Please ensure you are logged into
GitHub and if you still see the error please ensure that you have the correct access to the project. GitHub will show a
404 error to a user if they attempt to access the project but don't have the correct permissions.  
  

#### Pip install issues:  
  
Please note all commands in this section should be run in either a terminal(Linux/Mac) or a command prompt(Windows).  
  
If you get an error when running pip install and can't immediately see the error try to add the --verbose flag to the
command to see if that offers any more useful information, this can be done by running the command like so:  
"pip install {package} --verbose"  
  
If multiple versions of python are installed on your machine it may also be the case that you need to run the command as
such:  
"pip3 install {package}"  
  
Some other common errors include:  
  
1. Package name is incorrect, double check that the file path and name that you are giving to the command is correct.
2. If you have an outdated version of pip this can occasionally cause an issue, try running the below commands:  
"python -m pip install --update pip"  
"python -m pip install --update wheel distutils"  
3. Permission errors, options here include running as admin/sudo where allowed or run:  
"pip install {package} --user"  
This will run pip install defaulting the install location to the users home directory, as opposed to a system directory
like it normally would.
4. Failure during install, on Windows in particular a library can have issues installing due to packages it relies on,
try running:  
"pip install {package} --prefer-binary"  
This will cause pip to try install binary packages where possible as windows can sometimes throw errors compiling from
source
  
#### Alternatives to pip for installation:  
  
Some users may be in the scenario that due to user privileges that they are not allowed to use pip on their machines.
As an alternative to the .whl file, within a given release there will also be a tar.gz file in the format of
{LibraryName-version.tar.gz}. Download this file and extract it:  
  
- On a Unix system (linux/OSX) run the following command in a terminal: "tar -xf archive.tar.gz". Substituting archive.tar.gz
with the path to the tar.gz file downloaded
  
- On a Windows system open the file within 7Zip or a similar file archive program and follow the interface to extract the
folder.  
  
Navigate to the extracted folder within a terminal or command prompt and run the following command:    
"python setup.py install".  
  
Once this completes the library should now be installed on your machine. Please note on the above command to ensure
that you use the correct python command. Particularly for unix users, python V3.0 and higher will often be run as python3
within the terminal. If the previous command failed, it may be that you need to instead substitute it with: 
"python3 setup.py install".  
Alternatively on Windows machine python may sometimes be installed as py so:  
"py setup.py install".