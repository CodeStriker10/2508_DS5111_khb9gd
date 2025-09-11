
# 2508_DS5111_khb9gd
Data_Engineering 
Welcome to Software and Automation Skills!
Course DS5111: Streamlining Data Science with Software and Automation Skills

This is a very "hands-on" course.  In essence it's a learning lab.  It's purpose is to compliment your Data Science skills by walking through putting a pipeline together in as close a way as you would in a real work setting.

Our emphasis will be on removing as much of the 'surprise' factor when entering a real work setting, as well as picking up skills that make you efficient.

For efficiency's sake we'll take a close look at using the command line as it is still, after all these years, the backbone of how software is configured, accessed and run remotely.  To that end, we'll work on Ubuntu AWS instances throughout the semester to get comfortable with using the cloud.

Tool-wise, we'll focus heavily on on tools like Github and Github-Actions.  Both of these are both a major pain point and a real boost for productivity, respectively.   You are just about guaranteed to use one or both of these settings in any technical job these days.  We'll also look at a Data Build Tool, (DBT), a very common python package for data manipulation.  Finally we'll also spend some time with Snowflake, a data-lake/store tool that is ubiquitous and usually paired with DBT .

In terms of practices we'll touch on Object Oriented Design,  Testing and Design Patterns.  The primary focus on these is for efficiency.  It is the ideas and experience you gain from learning how to incorporate these practices into your workflow that pay off by saving you time and energy.  This applies regardless of the programming language or environment you eventually end up working on.

Our project will consist of gathering stock market data for our 'startup employer'.  By the end of the course you should have assembled a pipeline in the automatically collects data from Yahoo/Wall-street-journal, processes it with DBT, stores it in Snowflake, and then presents insight data in a report.

 

Syllabus: Fall 2025 

Course Start Date–End Date: August 26–December 9, 2025 

Credit Hours: 3 

Prerequisites: Be Enrolled in UVA MSDS Online Program 

Catalog Description: DS5111 Fall 2025

Live Online Meeting Times: Tuesdays, 8:30PM - 9:30PM EST 

There are no classes on the following days: 

   * October 14 – Reading Days 

   * November 4 – Election Day

 

Link to repository for course materials: 2508_DS5111_materialsLinks to an external site.

 

Learning Outcomes:

By the end of the semester, you will be able to: 

Work in github, (back out a commit, work with branches)
Set up and work in a cloud based linux box on AWS
Use makefiles for quick automation at the command line
Use cron to set up repeating jobs
Supplement your python programming with asserts and tests
Set up Github-Action to auto run  your tests in the cloud
Understand what Object Oriented Programming is and when to use it
Understand what Design Patterns for software are all about
Set up Data Build Tool to process the raw data  with from your cron jobs
Push that data into Snowflake for storage and further processing in SQL
Generate report tables
 

Each week, we'll program in class, (most classes), and then you'll wrap up the remaining work on your own.
=======
=======
# 2508_DS5111_khb9gd Data_Engineering Lab 1

** This repository contains setup instructions for configuring a new VM to run the project environment.  
Follow the steps below to clone the repo, run the provided scripts, and verify everything is ready for development.  


Requirements
- A new VM
- Github user key that is already configured on the VM
- Internet access

1. Clone the repository:
   
   git clone git@github.com:<your-username>/<repo-name>.git
cd <repo-name>

2. Go into the scripts folder:
   
   cd scripts

3. Run the Git config script:
   
   ./init_git_config.sh

      **Quick test:** run `git config --global --list` to confirm email and name are set.

   
4. Verify Git config:
   
   git config --global --list
  
5. Run the init script:
    
    ./init.sh

      **Quick test:** run `git status` — you should see the repo active.

7. Check that the repo is active:
    
    git status

Conclusion 
By following these steps, a new VM can be set up quickly with the correct Git configuration and project environment. After running the setup scripts and verifying with git status, the machine is ready for development and syncing with GitHub. 
