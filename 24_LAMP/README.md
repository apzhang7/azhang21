# how-to :: Provisioning LAMP on a Droplet
---
## Overview
Hosting apps on the cloud with DigitalOcean.

### Estimated Time Cost: 2 hour

### Prerequisites:

- A GitHub account (student dev pack recommended for free perks)
- A DigitalOcean account with a payment method (credit/debit card)

## Instructions

### DigitalOcean Setup + Getting Student EduPack $100 (Optional)
1. The GitHub Edu Pack Discount is optional, and you can register for the [GitHub EduPack](https://education.github.com/pack) here. 
2. WHen you are accepted you can proceed.
3. Create a DigitalOcean Account with your GitHub and verify your identity using a card.
4. You will need to scroll down on [this](https://education.github.com/pack/offers) to find DigitalOcean and copy the code.
5. Go to the billing tab once you have the code, and press promo code and paste it in.

### Creating Droplet
1. Go to Projects on the left, press the green Create button at the top, and click Droplets.
2. Click Ubuntu 20.04 (LTS) with the basic plan. This costs about $5 per month. Select the datacenter region (NY) thats closest. 
3. Select "SSH keys" for authentication method because password is not nearly as safe.
4. Your keys will be in your `~/.ssh` directory.
```
ssh-keygen
```
5. Copy and paste the inside of `id_rsa.pub` file and create.

### Installing Apache
```
sudo apt install apache2
```

### Installing MySQL (SQLite3 for us instead)
```
sudo apt install sqlite3
```

### Installing Python  
```
sudo apt install python3
```  

### Sudo User Account Creation
```
ssh root@your_server_ip
```
```
adduser username
```
To mod user to become sudo:
```
usermod -aG sudo my_username
```
To swap user:
```
su - username
``` 
FInd "PermitRootLogin" in sshd and change it from no to yes. 
```
sudo nano /etc/ssh/sshd_config
```
Save it and reload.
```
sudo service sshd reload
``` 

### Resources
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
* https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/how-can-i-disable-ssh-login-for-a-root-user-i-am-the-account-owner

---

Accurate as of (last update): 2022-01-24

#### Contributors:  
Angela Zhang, pd1
