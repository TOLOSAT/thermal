# Thermal Team Repository

This repository is used by the Thermal Control team of the Tolosat project.  
Its main goal is to store and share the Systema Thermica® files that we use to model the satelitte's thermal exchanges with its environment. 

## Organization of the Repository

Former files that are obsolete to our current models are stored in the "Archives" file.  
Types of files that may change during the study (depending on the goal/precision of the simulation) are stored in their respective files (Kinematics, Materials, Meshings and Models, Missions, Processings, Trajectories, USR Files)  

## Guide for Thermal Members
### How to use the Thermal GitHub

GitHub is a versioning software. Basically, it saves and stores any version of any file you ask it to keep.  
If you realise you made a mistake working on a file, you can go on the GitHub archives to find the previous version of the file and restore it.  

#### GitHub specific vocabulary

***Organization :*** The project/ Root of the tree. "TOLOSAT" is the organization in our case.  
***Repository :*** A section of the project. In our case, the TOLOSAT organization contains one repository per subsystem. You are currently in the repository called "thermal".  
***Branch :*** A big bloc of the team's work. In tolosat, most team's repository contains only the "main" branch.  

#### Procedures

All files from each of your repositories are stored on your PC in a file called GitHub.  
This file contains one file for each repository.
All files from a repository are stored in the corresponding file.  

All changes you make on any of these files will be kept by GitHub.  
When you open the GitHub Desktop app, they'll be listed on the left of the screen.  
On the bottom left of the screen, you have a fram with a "commit to *name of the branch*". You will need to click this button to synchronise the local changes on your computer with the files stored on GitHub.  
**ALWAYS** give information about what your committing (title + short paragraph of explanations). It will make everything clearer if someone ever needs to browse through the history of the changes.

After commiting your changes to the "main" branch (you could potentially commit to any other branch but we only have the "main" branch yet), you have to click the "Push" button on the top of the screen.  
Then, the "current correct" version of the files is the one you just pushed, and the other versions are stored in the GitHub archives.

If you want to use the files someone else commited to the main, use GitHub desktop and click "Pull" or "Create a Pull request" at the top of the screen. It will then modify the files from your GitHub file and replace them with the one stored in the GitHub.  

#### IMPORTANT INFORMATION

When you create a "Meshing" file on systema (.sysmsh), it will be automatically associated with a model file (.sysmdl). Thus, when you open the meshing on systema, it will "call" the corresponding model and open it too.  
Sadly, this call only works if the access pas is exactly the same (C:/mathi/GitHub/thermal... in my case). But logically, we all have different names so we have different acces paths for the same file.  

As a consequence, **everytime you pull a meshing file from GitHub** you'll have to run a Python code to modify the acces path accordingly.  
The code is stored in the *models and meshings* file. You can open it with any Python Idle environment (Spyder, Anaconda, Idle...).  

1. Open the code
2. Replace the Meshing and Model names in the corresponding places with the name of the files you'll be working with (pictures will be added later to clarify)
3. Run the code

Then everything should be working well on Systema
