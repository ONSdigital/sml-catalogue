# Features File

 The feature.json file is used for easily managing code that we want to opt in or opt out of, such as code involving the Content Management System (CMS).

 ## Purpose

 The purpose of the feature.json file is to provide a centralized location where developers can enable or disable specific code features based on their requirements. This allows for greater flexibility and control over the functionality of the software.

 ## How to Use

 To use the features file, follow these steps:

 1. Open the features file located at `config/feature.json`.
 2. Locate the section related to the specific feature you want to enable or disable.
 3. Set the corresponding flag to `true` or `false` to opt in or opt out of the feature.
 4. Save the file.

 By using the feature.json file, developers can integrate new functionality in a controlled way, earlier in the development cycle. This functionality can be enabled once appropriate testing and acceptance has been performed.
 
 Please note that changes made in the feature.json file  will require a rebuild and re-deploy of the website to take effect.