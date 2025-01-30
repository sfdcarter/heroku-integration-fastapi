# Heroku Integrations - FastAPI Example App

This repository contains an example Python/FastAPI app that works with [Heroku Integration](https://devcenter.heroku.com/articles/getting-started-heroku-integration) to talk to a connected Salesforce instance.


## On OAS 3.1.0 v 3.0.0
FastAPI generates OAS3.1 compatible specs. Unfortunately, Salesforce External Services supports 3.0.0 as the highest version. When spec version is set to 3.1.0, strange things happen during parsing. FastAPI allows overriding the generated OAS version, but doing so does not actually change the generated spec to not use 3.1 features. When developing with FastAPI, make sure the generated spec is only using features supported by Salesforce External Services.