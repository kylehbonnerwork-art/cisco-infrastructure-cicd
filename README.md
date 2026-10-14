# cisco-infrastructure-cicd
CI/CD pipeline for cisco IOS XE infrastructure automation using GitHub actions python and ansible  

project overview:

This project demonstrates infrastucture automation for a cisco IOS XE using github actions python and ansible. 
The goal is to build a repeatable workflow for validating network configuration, deploying approved changes to a cisco catalyst 8000v sandbox and verifying the resulting device state 

objectives:

Manage network automation code using Git. 
build continuous integration CI pipeline with GitHub actions. 
validate configuration inputs before deployment. 
automate cisco IOS XE device checks using ansible and python. 
verify device configuration and operational status. 
apply controlled deployment and recovery procedures. 
document testing results and infrastucture changes. 

Planned architecture 

GitHub: source control and configuration managment. 
GitHub action: automated workflow exection.
Python: configuration validation and test logic. 
Ansible: network device automation. 
Cisco Devnet Sandbox: isolated IOS EX test enviroment. 
Verification: confirm device state after approved changes.

Implementation Roadmap
Create GitHub repository 
Add project documentation and directory structure. 
Implement automated configuration validation. 
Create the GitHub actions CI workflows. 
Connect to cisco IOS XE sandbox.
Run read only device verification. 
Implement controlled configuaration deployment.
Add deployment verification and recovery documentation. 

safety and secruity 

Never commit passwords API tockens or private ssh keys. 
Store required credentials in protected GitHub secrets. 
Validate configuaration changes before deployment. 
Test changes in the sandbox before considering production use. 
Require explict approval before making device configuartion changes. 

project status 
Initial setup. automated validation and device connectivity are planned and have not yet been implemented

technologies 
Git, GitHub actions, python, ansible and cisco IOS XE 




