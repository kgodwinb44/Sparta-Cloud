## AWS Instance

### 1 - Launch Instance EC2
- Elastic Computing Cloud
- EC2 instances are VMs that run on Amazons cloud infrastructure
- EC2 allows users to rent servers to run their applications
![](/images/aws_services.PNG)

### 2 - Application and OS Images (AMI)
- An image provides the software required to set up and boot an instance
- e.g. Ubuntu, Windows, macOS
- Way to connect the instance using ssh

### 3 - Instance type (Computational Resources)
- Computing resources you can use, CPU, memory
- e.g. t3.micro, t4.micro

### 4 - Key pair
- Used to securely connect to the instance
- ssh keypair
- public key is stored on the instance and is used to encrypt messages
- messages can only be decrypted by the private key
![](/images/ssh_connection.PNG)

### 5 - Network Settings (Security Groups)
- security group is a set of firewall rules that control the traffic for the instance
- add specific rules such as port availability
- IP addresses allowed to access the instance
- possible to save your security group configurations and add rules

---

## AMIs (Amazon Machine Images) 

### Instances (EC2)
- an EC2 instance is a virtual server in the cloud that allows users to run applications

### Images
- an image is a pre-configured template used to launch instances (virtual servers)
- within EC2 (Amazon elastic computing cloud)