#!/bin/bash

# Update and Upgrade packages
sudo apt update -y
sudo apt upgrade -y

# Import MongoDB public GPG key
sudo apt-get install gnupg curl
curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg    --dearmor
 
# Add the MongoDB repository
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list
 
 
# Update packages and install MongoDB
sudo apt update -y
sudo apt-get install mongodb-org -y
 
 
# Enable and start the MongoDB service
sudo systemctl enable mongod
sudo systemctl start mongod

echo "MongoDB started and installed."
 
# Allow connections from all IPs by updating bindIp
sudo sed -i 's/  bindIp: .*/  bindIp: 0.0.0.0/' /etc/mongod.conf
 
# Restart MongoDB to apply changes
sudo systemctl restart mongod

echo "MongoDB is now accessible"