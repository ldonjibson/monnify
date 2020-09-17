# monnify
A Library created for ease of using monnify\'s API to create unique account numbers for your users/members, verify user transaction, generate Bearer Token etc..

This library makes it easy to connect with Monnify API (To create reserve accounts)

It will be updated and maintained as needed

Quick start
-----------
1. `pip install requests monnify`

2. To use:  `from monnify import Monnify`

3. Method includes :
	> **generateToken**: Method generate Token to be used in the subsequent calls

	> **createReserveAccount**: Creates reserve accounts and returns value from monnify's API

	> **createHashFromWebhook**: Generate hash as described on monnify's documentation to compare with transactionsHash

	> **getTranasactionDetails**: Get the status of a transactions e.g success or failed, this return the json values as seen on monnify's docs.
	
4. *USAGE*
	Initiate the class with **api** and **secretkey** from monnify then use a thus:

	**x = Monnify("apiKey", "clientSecretKey")**

	***e.g*** to get the **token**

	**`print(x.generateToken())`**

To contribute, pull the this repo, add your piece and raise a pull request.
	
