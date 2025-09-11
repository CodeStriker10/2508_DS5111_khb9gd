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
