Assuming you have the proper heroku creds and repo setup:

```bash
$> git push heroku master
```

Local usage:

```bash
# set creds
$> echo "AWS_KEY=<YOUR_KEY>" > .env
$> echo "AWS_SECRET=<YOUR_SECRET>" >> .env

# start the listener first
$> ./listen.sh

# start the endpoint
$> foreman start

# send a sample message
$> ./chat.sh

# now you should see it in the listen process
```
