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

6. Check that the repo is active:
    
    git status

## Conclusion
By following these steps, a new VM can be set up quickly with the correct Git configuration and project environment. After running the setup scripts and verifying the repo is active, you're ready to start working.

[![Feature Validation](https://github.com/CodeStriker10/2508_DS5111_khb9gd/actions/workflows/validations.yml/badge.svg)](https://github.com/CodeStriker10/2508_DS5111_khb9gd/actions/workflows/validations.yml)
