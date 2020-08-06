# Introduction to DevOps

> Topics Covered:
> 1. [What is DevOps](#what-is-devops)
> 2. [Multiple Environments](multiple_environments.md)
> 3. [CICD](../Week8_CICD/README.md)\
>   i. [Jenkins](../Week8_CICD/jenkins_intro.md)
> 4. [Web Servers](../Week7_VM/webservers.md)\
>   i. [Nginx](../Week7_VM/learningNGINX.md)
> 5. [Vagrant](../Week7_VM/README.md)

## What is DevOps 
- Not a job role 
- Combination of cultural philosophies, practices and tools that increase an organisation's ability to deliver applications and services at high velcoity.
- Involves evolving and improving products at a faster pace 
- Speed enables organisations to better serve their customers and compete more effectively in the market.
- A collaboration, a culture, a practice, an approach, an alignment of Dev and IT ops with better communication and collaboration. 

## How DevOps Works
- Under DevOps model, dev and ops teams are no longer 'siloed'.
- Sometimes two teams are merged into single team where engineers work across the entire application lifecycle from **development and test** to **deployment to operations**, and devleop a range of skills not limited to a single function
- In some DevOps models, quality assurance (QA) and security teams may also become more tightly integrated with dev and ops and throughout application lifecycle. (DevSecOps)
- Teams use practices to automate processes that historically have been manual and slow
- One fundamental practice is to perform very **frequent** but **small** updates.
- These updates are usually more incremental in nature than occasional updates performed under traditional release practices. 
- Frequent but small updates make each deployment less risky because they help teams address bugs earlier and faster.

## Why should we use DevOps
- Tech becoming more customer-centric, software does not just support a business, it has become an integral component of every part of a business.
- Companies interact with their customers through software delivered services, DevOps matter to increase the collaboration and deliver products at a higher rate.
    - Software becoming integral in supply chain and transforming every part of the value chain such as logistics, communications, and operations.
- DevOps achieves increased productivity and workflow
- Challenges related to infrastructure and legacy systems have arisen. 
- General lack of central governance and automation impacts productivity and increases time to market. 
- DevOps is a culture and set of processes. When we adopt a methodology that focuses on collaboration, shared goals, test automation, etc, we can increase rate of delivery which improves customer satisfaction.

## Challenges of Devops

**Common recurring Challenges of DevOps:**
1. Development vs Operations 
    - Entire concept of DevOps based on collaboration effort from both teams.
    - This concept can be misunderstood. Devs play with codes in order to build an innovative product. Ops try to achieve the highest level of quality of terms of product features and functionalities which causes friction. Ops assume developers deploy untested code in product. 
    - This means two teams, who are supposed to work together, work on different mind-set and objectives, causing project delays and lesser scope of innovation.

2. Cultural Changes
    - DevOps itself is a culture which can collide with existing work culture. 
    - Cultural change is not a short-term process
    - It takes time for employees to adopt a new culture 
    
3. Tools
    - Open source tools e.g Docker, Jenkins, etc are available 
    - Real challenge comes when there is a lack of knowledge on how to use these tools
    - Data security 

4. Legacy Systems (moving from legacy to microservices)
    - Older infrastructure and applications can be problematic, even if it has served the company for years.
    - Large monolithic structures tend to have many interconnected pieces with one application impacting several other systems.
    - DevOps faces the hurdle of having to validate changes across *all* of these affected systems.
    - The complex 10 or 20 year old architectures make these systems valuable are the very obstacles that impact ability to deliver changes at the pace expected
    
## How DevOps benefits the business 
- DevOps accelerates release of code, product to market, delivery times, greater stability/reliability and freeing up time to focus on value, which leads to higher profitability, market share and productivity goals in comparison to rival businesses who do not implement DevOps.
- **How?**
    - Faster deployment
        - By applying automation () to execute tests at a much faster pace
        - Reducing manual error
        - Releasing in smaller cycles to avoid major failures
    - Improved customer experience capabilities
        - Digital transformation drives the need for the constant delivery of customer experience capabilities 
    - Better office morale
    - More time for innovation
    - Faster problem solving abilities
    
# Four Pillars of DevOps (Key benefits)
- Ease of use
- Flexibility 
- Robustness
- Cost

# DevOps Value 
CAMS Model
- **C**ulture
    - Culture is defined by the interaction of people and groups and is driven by behaviour. 
    - Substantial communication improvement can result when there is a mutual understanding of others and their goals and responsibilities. 
    - Traditional IT business models split developers and operations into two distinct groups.
    - Dev were tasked with innovating, creating and moving fast.
    - Ops were concerned with maintaining stable environments and infrastructure. 
    - These competing goals often cause friction as each group accused the other of preventing them from doing their jobs.
- **A**utomation
    - Automation can save time, effort, and money, just like culture, it focuses on people and processes and not just tools/
    - CI/CD can be magnified after understanding an organisation's culture and goals
- **M**easurement
    - Using measurements help to determine if progress is being made in the intended direction
    - Major metrics include income, costs, revenue, mean time to recovery, mean time between failures, and employee satisfaction
- **S**haring
    - Similar to agile and scrum, place a very high premium on transparency and openness
    - Spreading knowledge helps to tighten feedback loops and enables organisation to continuously improve
    - This makes the team a more efficient unit and allows it to become greater than just the sum of its parts

<img src="https://shadow-soft.com/wp-content/uploads/2017/07/implementing-devops.png" alt='cams model'>

## DevOps Principles
1. Customer-Centric Action
2. End-to-end Responsibility
3. Continuous Improvement
4. Automate everything
5. Work as one team
6. Monitor and test everything

# Risk Register
A typical risk register might look like this:

**Description**|**Change of Occurrence**|**Potential Damage**|**Risk**
-----|------|-----|-----
Dev Env broken| Medium|Develops can not work|Low/Medium
Testing server broken| Medium/High| New code cannot be tested| Low/Medium
Automated testing broke|Medium/High| New code cannot be tested| Low/Medium
Jenkins server broken|Medium|New code cannot be pushed live|Low/Medium
Production server fails|Medium|Loss of Revenue|High 

---

Using [Vagrant](https://github.com/naistangz/Technical_Training/tree/master/docs/Week7_VM)


