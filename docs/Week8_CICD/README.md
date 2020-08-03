# Continuous Integration Continuous Delivery 

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
Before Jenkins| After Jenkins 
-----|------
Developers complete assignments, commit code at same time. Later, build is tested and deployed| Code is built and tested as soon as Developer commits code. Jenkins builds and tests code many times during the day. If the build is successful, Jenkins will deploy the source into the test server and notifies the deployment team. If build fails, Jenkins will notify the errors to the developer team.
Developers wait until other developers finish coding to check their build.| The code is built immediately after any of the Developer commits
Difficult to isolate, detect, fix errors for multiple commits| Code is built after each commit of a single developer, easy to detect whose code caused built to fail.
Code build and test process are manual| Automated build and test process, saving time and reducing defects
Code is deployed once all errors are fixed and tested|Code is deployed after every successful build and test
Dev Cycle is slow| The dev cycle is fast. New Features are more readily available to users. Increase in profit. 

A simple CI pipeline
<img src="https://wpblog.semaphoreci.com/wp-content/uploads/2019/03/golang-ci-pipeline-1024x316.png" alt="Ci-pipeline-example">

# Benefits of pipelines
Having a CI/CD pipeline has more positive effects than only making an existing process more efficient:
- Developers can stay focused on writing code and monitoring the behaviour of the system in production. 
- QA and product stakeholders have easy access to the latest, or any, version of the system. 
- Product updates are not stressful.
- Logs of all code changes, tests and deployments are available for inspection at any time.
- Fast feedback loop helps build an organisational culture of learning and responsibility. 

--- 
[Introduction to CI/CD Pipelines with Jenkins](https://github.com/naistangz/ci-start-code/blob/master/ci_jenkins.md)

**Before:**

<img src="https://cdn.thenewstack.io/media/2018/08/8d8eb43f-codefresh3.png">

**After:**

<img src="https://cdn.thenewstack.io/media/2018/08/cdc82f2b-codefresh2.png">
