As issues using our methods are raised we will update this section with relevant information to resolve said issue. Providing a resource to help fix these issues as they occur in the future.  
  
#### Alternatives to pip for installation:  
  
Some users may be in the scenario that due to user privileges that they are not allowed to use pip on their machines.
As an alternative to the .whl file, within a given release there will also be a tar.gz file in the format of
{LibraryName-version.tar.gz}. Download this file and extract it:  
  
- On a Unix system (linux/OSX) run the following command in a terminal: "tar -xf archive.tar.gz".  
  
- On a Windows system open the file within 7Zip or a similar file archive program and follow the interface to extract the
folder.  
  
Navigate to the extracted folder within a terminal or command prompt and run the following command:    
"python setup.py install".  
  
Once this completes the library should now be installed on your machine. Please note on the above command to ensure
that you use the correct python command. Particularly for unix users, python V3.0 and higher will often be run as python3
within the terminal. If the previous command failed it may be that you need to instead substitute it with: 
"python3 setup.py install".