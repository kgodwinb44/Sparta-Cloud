#!/bin/bash

# Update
sudo apt update -y

# Upgrade
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y

# Restart nginx
sudo systemctl restart nginx

# Enable nginx
sudo systemctl enable nginx