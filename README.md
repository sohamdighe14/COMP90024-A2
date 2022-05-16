# COMP90024-A2
Assignment 2 for Cloud Computing course 

This projects can be separated in two main usage. First the deployment of a database a tweet harvester and a website on the university of Melbourne Research Cloud; and second the use of the said website.
---

## Deployment guide

### Creating the instances
The deployment of all these elements requires first an access t the MRC. If you have an account linked to a project, you will need to select the said project and download the associated RC file like shown below.

![Alt text](/assets/ScreenRCfile.png)

Replace `SamyOpenrc.sh` in the MRC directory and in `run_nectar.sh` with the file you just downloaded.
Make sure you have your MRC password noted somewhere, if you don't know it, you can reset it in the MRC users settings.

![Alt text](/assets/userSettingsMRC.png)

Finally you will need to create a key pair. You can do it on the MRC in the "key pairs" section :

![Alt text](/assets/keyPairsScreen.png)

This action will automatically download a `<key name>.pem` file in your Downloads folder. You want to replace `slave1samy.pem` by the one you've just downloaded in the MRC folder. Once this is done, you will need to use the command line :
>`chmod 600 <key name>`
to change the access permission of the key file.

Now, to first create the instances, you will need to comment out everything but the `#Generates the MRC instances` in `MRC/nectar.yaml`.

To create the instances, you will either need to be located at the university using eduroam or using the cisco VPN. Once this set up, you can use the command line :

>`bash run_nectar.sh`

You will then need to enter your MRC password and the script will create 4 instances.

### Deploying the couchDB database, the twitter harvester and the website

You will first need to put a file named `config.ini` in the TweetHarvestor directory. This file will contain the set of API keys you want to use to harvest tweets. It should have the following format

>`[key1]`
>
>`api_key = <your api key>`
>`api_key_secret = <your api key secret>`
>
>`access_token = <your access token>`
>`access_token_secret = <your access token secret>`
>
>`bearer_token = <your bearer token>`
>
>`[key 2]`
>`.`
>`.`
>`.`

These credentials are available when you create an API project on the developper twitter website : https://dev.twitter.com

Once the config file created, you will need to replace the ip adresses in the `host` file by these new adresses, uncomment everything in `MRC/nectar.yaml` and run the same command :
>`bash run_nectar.sh`

You will once again be asked your password, but after that, you should have a couchDB database accessible on `<Masternode ip adress>:5984`, a twitter harvester running on `slave1` and a website running on `<Webapp ip adress>:5984`.

---

## End user usage