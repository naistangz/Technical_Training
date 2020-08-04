# Continuous Integration Continuous Delivery 

## What is a pipeline?
- A pipeline consists of a chain of processing elements arranged so that the output of each element is the input of the next. 
- A set of automated processes that allow Developers and DevOps professionals to reliably and efficiently compile, build and deploy their code to their production compute platforms.
 
## What is a CI/CD pipeline?
- CI/CD pipeline automates your software delivery process
- The pipeline builds code, runs tests (CI), and safely deploys a new version of the application (CD).
- Automated pipelines remove manual errors, provide standardised feedback loops to developers, and enable fast product iterations.

## What do CI and CD mean?
- CI (Continuous Integration) is a software development practice in which all developers merge code changes in a central repository multiple times a day. 
- CD (Continuous Delivery), adds practice of automating the entire software release process.
- With CI, each change in code triggers an automated build-and-test sequence for the given project, providing feedback to the developer(s) who made the change. 
- CD includes infrastructure provisioning (e.g using Vagrant as an **Infrastructure as Code** tool) and deployment, which may be manual and consist of multiple stages.

**All these processes are fully automated, with each run fully logged and visible to the entire team**

## Why use CI with Jenkins?
- Open-source governance and community
    - Anyone can inspect, modify and enhance, which enables speed and flexibility, offering mutiple ways to solve problems.
- Stability 
- Extensible
    - Wide range of plugins
    - Extensible in terms of integrating with specific source code management tools, specific development paradigms, or software languages and their respective test frameworks
- Visibility
    - Captures metrics and data from any environment, any kind of logs that get ejected from running a test, or a development process 
- Pipelines
    - Increased visibility through the use of pipelines and pipeline stages that get presented in the user interface.  

Before Jenkins| After Jenkins 
-----|------
Developers complete assignments, commit code at same time. Later, build is tested and deployed| Code is built and tested as soon as Developer commits code. Jenkins builds and tests code many times during the day. If the build is successful, Jenkins will deploy the source into the test server and notifies the deployment team. If build fails, Jenkins will notify the errors to the developer team.
Developers wait until other developers finish coding to check their build.| The code is built immediately after any of the Developer commits
Difficult to isolate, detect, fix errors for multiple commits| Code is built after each commit of a single developer, easy to detect whose code caused built to fail.
Code build and test process are manual| Automated build and test process, saving time and reducing defects
Code is deployed once all errors are fixed and tested|Code is deployed after every successful build and test
Dev Cycle is slow| The dev cycle is fast. New Features are more readily available to users. Increase in profit. 

**A simple CI pipeline**
<img src="https://wpblog.semaphoreci.com/wp-content/uploads/2019/03/golang-ci-pipeline-1024x316.png" alt="Ci-pipeline-example">

# Benefits of pipelines
Having a CI/CD pipeline has more positive effects than only making an existing process more efficient:
- Developers can stay focused on writing code and monitoring the behaviour of the system in production. 
- In an agile environment, QA and Developers can work efficiently together.
- QA and product stakeholders have easy access to the latest, or any, version of the system. 
- Product updates are not stressful.
- Logs of all code changes, tests and deployments are available for inspection at any time.
- Fast feedback loop helps build an organisational culture of learning and responsibility. 
- In comparison to classic models (Software Dev Life Cycle e.g Waterfall, V-Model), Jenkins allows for direct deployment into production environments with descriptive services.

# CI vs CD
- **CI** is process of integrating code into mainline code base
- **CD** is process that takes place after code is integrated for app changes to be delivered to users. 
- **CD** is extension of **CI** 

# Continuous Deployment vs Continuous Delivery 
- "Continuous Delivery" means that you are ready and able to deploy any version to any supported platform at any time.
- "Continuous Deployment" means that you are engaging with actual deployment.
- Continuous Deployment does not mean you must deploy to production or to the customer every time/
    E.g  you can deploy to *QA* or to a deployment slot. 
- A deployment slot is an A/B deployment method that allows you to get valuable information without inconveniencing users if a defect leaks in the testing process.
- One way of deploying to a slot might be to offer an 'opt-in' choice for the customer to get an updated version, providing you with a smaller group of users that can serve as a 'beta'. You always give these users the ability to go back to the former version if they want to do so. 
- Biggest difference is that delivery stops and has potentially some manual steps before we go to production. 
- In Continuous Deployment, the development, test, potential staging, and final production release are all automated.

--- 
[Introduction to CI/CD Pipelines with Jenkins](https://github.com/naistangz/ci-start-code/blob/master/ci_jenkins.md)

**Before:**

<img src="https://cdn.thenewstack.io/media/2018/08/8d8eb43f-codefresh3.png">

**After:**

<img src="https://cdn.thenewstack.io/media/2018/08/cdc82f2b-codefresh2.png">

**Solution Delivery Pipeline:**

<img src="http://techtowntraining.com/sites/default/files/inline-images/solution-s-curve.png">

## Scenario of a CI/CD Pipeline
1. You are building a web application which is going to be deployed on live web servers. 
2. You have a set of developers responsible for writing the code, who will further go on and build the web application. 
3. Code is committed into a version control system (such as git) by the team of developers.
<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/CI-CD-Pipeline-CI-CD-Pipeline-Edureka-1.png" alt="version_control">
4. Next, is the first phase of the pipeline, the build phase, where developers put in their code, code goes into version control system.
<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/CI-CD-Pipeline-CI-CD-Pipeline-Edureka-2.png">
5. Once **build phase** is over, next is the **testing phase**. In this phase, we have various kinds of testing. *Unit test* (testing a chunk/unit of software or for its sanity test).
<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/CI-CD-Pipeline-CI-CD-Pipeline-Edureka-3.png"> 
6. When test is completed, next is the **deploy phase**, where you deploy it into a staging or a test server. Here, you can view the code or you can view the app in a simulator. 
<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/CI-CD-Pipeline-CI-CD-Pipeline-Edureka.png">
7. Once code is deployed, you can run another sanity test. It everything is accepted, then it can be deployed to production. 
<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/CI-CD-Pipeline-CI-CD-Pipeline-Edureka-6.png" alt="deploy_to_production">
8. In every step, if there is an error, you can shoot an email back to the development team so that they can fix it. 
9. Developers can push the updated code into the version control system and goes back into the pipeline.
10. If there is any error reported during testing, the feedback goes to the dev team again, where they fix it and the process reiterates if required. 
<img src="https://www.edureka.co/blog/content/ver.1531719070/uploads/2018/07/CI-CD-Pipeline-CI-CD-Pipeline-Edureka-7.png">
11. Lifecycle continues until we get code/a product which can be deployed to the production server.