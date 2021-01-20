# GIT BASICS AND WORKFLOWS:

This repository contains the basics of utilizing git, as well as a selection of git workflows utilized in Skatteetaten projects used for collaborations, code-sharing, code-improvement and code-deployment.

The basics are covered in the **Getting Started** section below, whereas the workflows are covered in the attached word document. There is a troubleshooting section below too, once you have set up git on your system.

The Git Workflow consists of sections on Getting Started, Basic Collaboration, Synchronous and Full Collaboration, and Troubleshooting. The other files are referred to in that workflow, and used for visualization of the workflow word document.

To use this project, please clone this project (see instructions below).

# **Table of Contents** 

- [GETTING STARTED](#getting-started)
	- [NECESSARY AND RECOMMENDED READING](#necessary-and-recommended-reading)
	- [GETTING ACCESS](#getting-access)
	- [SOME BASIC INFO ON BITBUCKET](#some-basic-info-on-bitbucket)
	- [SOME BASIC INFO ON THIS REPOSITORY](#some-basic-info-on-this-repository)
	- [USING GIT FROM A COMMAND PROMPT](#using-git-from-a-command-prompt)
	- [CONFIGURING GIT FOR THE FIRST TIME](#configuring-git-for-the-first-time)
	- [PUTTING CODE INTO A REPOSITORY](#putting-code-into-a-repository)
	- [CLONING A GIT REPOSITORY ON BITBUCKET](#cloning-a-git-repository-on-bitbucket)
	- [GIT BASICS](#git-basics)
	- [IMPORTANT COMMANDS](#important-commands)
- [TROUBLESHOOTING AND OTHER ACTIONS (under development)](#troubleshooting-and-other-actions)

#  

<a name="getting-started"></a>
# GETTING STARTED:

<a name="necessary-and-recommended-reading"></a>
## NECESSARY AND RECOMMENDED READING:

Very important to read these articles, as they will save you substantial time:

1.  *(Necessary reading)* [Introduction to Git](https://medium.com/@itswisdomagain/git-101-introduction-to-git-for-newbies-bb14f6f9fc1)
2.  *(Necessary reading)* [Introduction to GitHub](https://medium.com/@itswisdomagain/github-101-introduction-to-github-for-newbies-efaf46c88406) (very similar to Bitbucket which is Skatteetaten\'s internal version control web-based hosting service)
3.  *(Recommended reading)* To understand the idea of **Basic Collaboration -- Section A**, the first workflow in this repository, read [this](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/)
4.  *(Recommended reading)* To understand the idea of **Synchronous Collaboration -- Section B**, the second workflow in this repository, read [this](https://www.atlassian.com/git/articles/simple-git-workflow-is-simple)

## GETTING ACCESS:

-   You must apply for access to **UTV: Utvikler \[L1\] via ISIM Selvbetjening (Produksjon)** to get access to Bitbucket.
-   Once approved to access Skatteetaten's Bitbucket (you will receive an e-mail), you can start using Bitbucket.
<img align="left" src="https://github.com/EdSaiediSkatt/git-workflow/blob/master/media/image1.png">

<a name="some-basic-info-on-bitbucket"></a>
## SOME BASIC INFO ON BITBUCKET:

Let's cover a few basics about Bitbucket:

-   To the left is a snapshot of an expanded side panel of Bitbucket, which is full of great options. You can expand or collapse the side panel at any time by clicking the \<\< arrow at the bottom of it. Best to start learning with an expanded side panel however.
-   Explore these, but do not worry if you do not know what each does. [This webpage](https://bitbucket.org/product/guides/basics/bitbucket-interface) below and this workflow guide will help a little:
-   **Some jargon:** Repo is short for repository

<a name="some-basic-info-on-this-repository"></a>
## SOME BASIC INFO ON THIS REPOSITORY:

-   The workflow inside this repository is meant to standardize collaboration across Innsikt and Analysts in Skatteetaten. **It is not foolproof** and **is a work-in-progress**, so better workflows may exist and your feedback is appreciated. It was written as a collaborative initiative intended to help and maintaining it is not the author(s)' responsibility. When you run into problems, first consult the trouble-shoot section, next google and if you find a better solution please do inform us.
-   Color-guide to this document: This guide uses a code blocks around commands you shall type (and execute by pressing enter).  It uses **`code block in bold`** or often \<\> around characters you must substitute for yourself.
```js
It uses some randomally-colored syntax highlighting as in here in code block style for terminal (e.g. Git Bash)'s output. 
```

<a name="using-git-from-a-command-prompt"></a>
## USING GIT FROM A COMMAND PROMPT:

Git Bash is a command prompt tool in Windows for using Git. There is a Git GUI or Graphical User Interface, however most Git users do use command prompt terminals, such as Git Bash. Follow the procedure below:

1.  Install Git Bash from your Software Centre in your VDI Sikker (recommended) or Intern
2.  Open it once installed
3.  The interface is just as in most interpreters/powershells/terminals, DOS, anaconda prompt, etc. Meaning that your usual DOS **or** Unix commands of `pwd`, `dir`, `ls`, `mkdir`, `cd`, `cd ..`, all work. To learn the basics of navigating in a terminal, read <https://www.digitalcitizen.life/command-prompt-how-use-basic-commands>
4.  By typing cd \$Home, you will navigate to your C:/Brukere/\<your-6-character-user-id, e.g. m87450\>; Note that at any point in time you can type `pwd` to see which directory you are in.
5.  Type `cd Documents` to navigate there
6.  Type `mkdir Git`, to **m**a**k**e a **dir**ectory called Git
7.  (Optional) Get rid of MINGW64 by typing:
```
export PS1=”${PS1/\$TITLEPREFIX:}”; export PS1=”${PS1/\$MSYSTEM }” >> ~/.bashrc
```
8.  Configure Git (explanation below) and then start Gitting

<a name="configuring-git-for-the-first-time"></a>
## CONFIGURING GIT FOR THE FIRST TIME:

You would need to configure Git by running the commands below (writer your own first and last name):
```
git config --global user.name "Surname, Firstname"
git config --global user.email "Firstname.Surname@skatteetaten.no"
```
<a name="putting-code-into-a-repository"></a>
## PUTTING CODE INTO A REPOSITORY:

The person who will host the repository on their Bitbucket account, will follow these steps:

1.  Create a folder where you place all the code, input files and output files into.
*Note: Best practice would be to place the input files in an input folder, and the output files in an output folder. The folder names could simply be INPUT or OUTPUT, but often names such as RAW DATA, ER (for EnhetsRegister), KLADD, etc make sense for input folders, and names such as VISUELLISERING, PRESENTAJSONER, can make sense for output files.*
2.  Go onto your Bitbucket profile (<https://git.aurora.skead.no/profile>) and click on the \"Create repository\" rectangle. Then give it a Name and a Description. Best to leave default branch name empty so the default branch is called \"master\". Click on Create respository.
3.  Find the repository\'s HTTP link. See the webpage popping up after the last step --snapshot below-, in which, there are four places from which to copy the repository\'s HTTP link. The left-hand pop-up window seen below will always exist for any repository, from which you can copy the highlighted HTTP link:
![](https://github.com/EdSaiediSkatt/git-workflow/blob/master/media/image2.png)
4.  Once you are ready to push (\"upload\") your data to the repository, ensure you are in that folder by typing: cd existing-project and follow with the steps below (you can also find these commands above under \"My code is ready to be pushed\":
5.  `git init`
6.  Create a .gitignore file (which will help git ignore backup files created by editors, or intermediate files or any files you would like to keep private on your local Git folder), by following steps:

    a.  `touch .gitignore` (this creates a .gitignore text file)
    b.  `nano .gitignore` (this launches a text editor called Nano within Git Bash)
    c.  Type appropriate file or folder names you would like Git to ignore, each on a line (for folders, you type ignoredfolder/ and for files you type file_to_ignore.extension; depending on what software your team codes in, here are great sample gitignore files: <https://git.aurora.skead.no/users/m87450/repos/gitignore/browse> e.g. for Python:  <https://git.aurora.skead.no/users/m87450/repos/gitignore/browse/Python.gitignore>)

d.  Press CNTR+S to save and CNTR+X to quit (hint: \^means control in nano). ***Tip:** You can edit the text file after creating it in step a) by opening your file explorer and editing the file in notepad too.*
e.  **NOTE:** Once any file is added and tracked --i.e. included in `git add`, see next step-, it will be tracked and will not be ignored for anyone using the repository. So include files and folders you want ignored WHEN creating a depository OR for new files added or created, include them in the .gitignore file BEFORE running `git add --all`.
f.  **NOTE:** If you or someone HAD ADDED a file or folder, BEFORE it was included in the .gitignore text file, and you want to tell git to untrack it locally --i.e. untrack it for you only- then you can type `git update-index --skip-worktree \<path-name\>`. Each user will have to run this, to untrack it locally.
g.  **NOTE:** If you want to untrack the file for everyone using the repo, you can use option 1 of this stackexchange answer, but caution as it will delete files for others: <https://stackoverflow.com/questions/936249/how-to-stop-tracking-and-ignore-changes-to-a-file-in-git/40272289#40272289>
h.  **NOTE:** If you want to ignore select subfolders inside a shared (i.e. non-ignored) folder in a repository, you can specify the sharedfolder/subfolder/ inside the gitignore at the root of your directory, or you can place a .gitignore file within the sharedfolder where you add subfolder/ to it. This latter choice may be preferred in some cases.

```
7.  git add --all
8.  git commit -m "Initial Commit"
9.  git remote add origin <COPY HTTP LINK HERE\>
10. git push -u origin HEAD:master
```
11. Refresh the Bitbucket page, you should now see your folder uploaded in the remote repository called origin, on a branch called master.

<a name="cloning-a-git-repository-on-bitbucket"></a>
## CLONING A GIT REPOSITORY ON BITBUCKET:

For the person who is not the main host of the repository, cloning the repository is the first action they take, so they can start collaborating on the project.

Although it\'s not a precise comparison, you can think of \"Cloning a repository\" as \"Downloading the repository **for the first time**\". The procedure for that is simply by copying the HTTP link that appears in photo above and typing:
```
git clone <COPY HTTP LINK HERE>
```
<a name="git-basics"></a>
## GIT BASICS

As a version control system, git takes your working directory (i.e. what you see in your file explorer or what you can see by typing ls in a terminal) and it will start tracking changes you make to it locally, but only if you add the changes! git add takes changes you save in your working directory into a "staging area", and `git commit --m "commit message label"` takes your staged changes into your local repository and puts a label on it. Graphically speaking it looks like this:

![](https://github.com/EdSaiediSkatt/git-workflow/blob/master/media/image3.png)

The above graphic shows the staging and repository areas. The shaded .git rectangle in the graphic above, shows that a hidden folder in your working directory (created after you wrote `git init`), is now keeping an eye on the file you put into your staging area and what you then put into your repository. If you had multiple files, the graphic would look like this:

![](https://github.com/EdSaiediSkatt/git-workflow/blob/master/media/image4.png)

Why do we need a staging area before folders are in our local repository? Let's take the answer from this [webpage](https://dev.to/sublimegeek/git-staging-area-explained-like-im-five-1anh):

> *"Imagine a box. You can put stuff into the box. You can take stuff out of the box. This box is the staging area of Git. You can craft commits here. Committing is like sealing that box and sticking a label on it. The contents of that box are your changes. So, why not have the label mean something? You wouldn't label a moving box with kitchen items as simply "stuff."*
>
> *As you make changes locally, Git can \"see\" them. However, figuratively speaking, they\'re out of the box. If you were to try and make a commit at this point, Git wouldn\'t have anything to commit."*

<a name="important-commands"></a>
## IMPORTANT COMMANDS

-   At any point in time, in your Git Bash (or terminal) you can type **`git status`**, which will show you at what stage of the staging and committing process you are in, and give you guidelines on what to do next.
-   You and your collaborators would and should add many different commits for changes you make. In order to see these from latest to earliest, just type `git log`, which will show you the commit names, hash codes (a unique number that git uses for each commit), date and author. When these grow long, your terminal will not show all until you press enter to scroll further down or press q to exit them.
-   At any point in time, you can see which branch you are on, by looking at the (blue) colored branch name, which is by default always set to be (master). In Section A, you will see how you create new branches.
-   You can always type **`git diff HEAD\~1`** to see the differences between the latest commit (called HEAD of the branch) and the change committed prior to that in the git branch you are in. Type **`git diff HEAD\~2`** to go see differences between the version going backwards two committed changes from the HEAD.
-   You can use **`git diff`** to see differences between two branches too, e.g. **`git diff master..feature_branch`**. **Hint:** For comparing to branches on the remote, when remote is called origin, then just type: **`git diff master..origin/master`**


<a name="troubleshooting-and-other-actions"></a>
# TROUBLESHOOTING AND OTHER ACTIONS (under development)

![](https://github.com/EdSaiediSkatt/git-workflow/blob/master/media/image12.png)

**The above meme may look like a joke, but in fact when every other troubleshooting issue below fails, the solution ´stated above (saving your work elsewhere, deleting the project and downloading (i.e. `git clone` ing) a new project, works wonders!**

**Possible errors:**

If during any of the process in **WINDOWS**, you encounter this error: 
```js
LF will be replaced by CRLF in git
```
, use this:
```
git config --global core.autocrlf true
```
If you encounter this in **Linux or MacOS**, type this:
```
git config --global core.autocrlf input
```
(link with explanation is here: <https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important>)

Hint: If it just gives a warning and not an error, then you may not have to run these, and may be able to continue your work without disruptions. The reason why this happens could be due to the git repo being pushed to by a Unix-user and a Windows-user, where end of sentences use different LF (Line Feeds) or CR (carriage returns). The stackoverflow link explains it best.

If you get the error:
```
git push origin master
```
```js
fatal: Authentication failed for 'https://git.aurora.skead.no/scm/~m87450/git_workflow.git/'
```
, it means that you had not configured properly OR your password was changed, then this is what to do:
```
git remote set-url origin https://<USERNAME>:<PASSWORD>@<COPY HTTP LINK WITHOUT https:// HERE, e.g. git.aurora.skead.no/scm/~m87450/git-workflow.git>
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

If you want to merge two remote branches, use the following:
```
git push origin feature_branch:master --force
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

In case there are multiple merge conflicts when you are on the local master branch and you do a `git pull origin master` (remember that `git pull` is a `git fetch` plus a `git merge`), then run this to update your local master branch to the origin master branch by force:
```
git reset --hard origin/master
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

To simply merge a specific file from a branch (A) to another branch (B), ensure you are on the branch you want to merge to (i.e. B), then simply type:
```
git checkout branch_a UpdatedFileOnBranchA
```
Afterwards, just `git add --all` and `git commit --m "message"` as you wish.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

If you try to do a `git pull` and get the following error:

Error:
```js
Please commit your changes or stash them before you merge.
```
If you want to stash them, you can execute:
```
git stash -u
```
If you want to delete all your changes, you can type:
```
git reset --hard origin/master
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

To force pull from merge and overwrite local files:
```
git fetch --all
git reset --hard origin/master
git pull origin master
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

If you get an error that some of your files will be overridden, but you don't mind that, run this:
```
git reset --hard origin/master
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

If you run into an error of this type:
```js
error: RPC failed; curl 56 OpenSSL
```
And you believe it is because the repository you are pulling was too large, then run this to increase the bandwidth:
```
git config http.postBuffer 524288000
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Checklist A. Step 7.a)

As a rule of thumb, you must only checkout another branch, after having committed any changes on your current branch. If you don't you can get this error:
```
git checkout add_simple_collab_workflow
```
Please commit your changes or stash them before you merge.

In these cases, you may wish to discard (i.e. get rid of permanently) or stash (i.e. put them aside for potential future retrieval) your changes.

If you want to discard them, you can execute:
```
git checkout -- .
```
If you want to stash them, you can execute:
```
git stash -u
```
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Checklist A. Step 12.a)

If your feature branch is ahead of your local master for any reason and the changes ahead are not integrated, you may get this error:
```
git branch -d feature_branch
```
error: The branch \'feature_branch\' is not fully merged.

If you are sure you want to delete it, run **`git branch -D feature_branch`**.

Simply follow their instructions if you want to delete the branch, otherwise checkout if you had intended to merge your branch changes ahead of deleting it.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

# DEVELOPERS:
This Git Workflow is developed by Ed Saiedi, with valuable feedback from colleagues in the Innsikt and Utvikling divisions of Skatteetaten. As a collaborative git repository, we hope other users will update this repository.

