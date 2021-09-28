# order-pay-backend
Backend API service for Order and Pay Menu

# TODO:
+ Create backend api for menu sections/items/item options (GET)
- Fix item option binary model -- it should return a list of all such options
- Create shopping cart backend (sessions?)
	- need to be able to recieve every shopping cart update and modify user data accordingly (POST)
	- get the current shopping cart for a specified user (close tab, reopen it, shopping cart shouldn't reset) (GET)
- Create checkout backend (iyzico?)
	- How and what to pass to online POS?
		- Decide:
			- Send request to our server (list of items and price check) THEN our backend sends payment data to POS
			- OR: Front end sends request to POS and us (so that we have record of it) simultaneously. Which is better?
	- Implement necessary backend
- Create Accounts Backend
	- Instead of guest sessions, create accounts with email/password (google/apple/facebook sign in?)
- Sessions are on Database -- check performance switch to cookie ONLY IF ABSOLUTELY NECESSARY
- Create react project for front-end
