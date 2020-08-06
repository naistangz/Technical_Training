# Development, Test, QA, and Production Environments

## What is an environment?
- Where your code and test runs
- If using virtual machine, environment will be consistent for all developers

## Multiple Environments 
<img src="https://deploybot.com/assets/blog/Deploybot_Multiple-Environments_illustrations_previewchanges-1.png"alt="deploy_image">

An example setup could have **development**, **staging** and **production** environments:
- **Development:** The **dev** environment is first line of defense against bugs. Here developers deploy their code and test any newly implemented features. Any bugs found are dealt with before re-deploying for further testing. 
Process is iterated until the code is ready for the next stage of testing. 

- **Staging**: Once developers are satisfied with their code and consider it fairly stable, it is then deployed to the staging environment for further testing. Here, Quality Assurance (QA) is performed. Testers access the staging servers and ensure that the application works as it should. They run test cases to detect bugs and run performance tests to find areas that could be improved. 
Any bugs or enhancements are reported back to the developers and the process is repeated until the code passes the staging phase. 

- **Production:** Once code tested, it is pushed to production where it is made available to end-users. 

## Using Virtual Machine Solutions 