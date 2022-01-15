# berbix-webhook-demo
Dockerized FastAPI application to test Berbix webhooks

## Set Up
- [ ] Start by cloning this repo: `git clone git@github.com:sgsharma/fastapi-docker.git`

- [ ] Login to the Berbix console: https://dashboard.berbix.com/login

- [ ] Enable "Test" mode with the slider in the top right hand corner of the Berbix Dashboard.

- [ ] Generate API keys following these instructions: https://docs.berbix.com/docs/settings#section-api-keys

- [ ] Copy `.env.example` to `.env` and add your API secret to `BERBIX_API_SECRET`

- [ ] On the `Integrations` page in the Berbix console add a webhook and copy the hook secret to `BERBIX_WEBHOOK_SECRET`

- [ ] Add your last name (as on your ID that you'll be testing with) to your list of Test IDs. Go to Settings —> Test IDs -> Add Test ID.


## Docker Set Up
Make sure you have installed Docker to continue with the instructions in this README

### Docker QuickStart

To start the app:

```
$ docker-compose up --build
```

Next, we'll expose the app over the internet using ngrok. You can install ngrok [here](https://ngrok.com/):

```
ngrok http 8000
```

Navigate to the `Integrations` page in the Berbix console again and add the public URL from ngrok to the `Target URL` field: `http://<####-##-###-#-###>.ngrok.io/hook` 

Now, you should be able to test this webhook from the Integrations page by clicking on `Test`
 