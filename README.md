# Insurance company ChatBot

This bot has been created using [Bot Framework](https://dev.botframework.com).

## Prerequisites

This samples **requires** prerequisites in order to run.

### Overview

This bot answers client's questions using [QnA Maker Service](https://www.qnamaker.ai), this bot get appointments for clients and saves it in a mysql database hosted on [heroku.com](https://heroku.com). It also informs clients about products and services of [GlobMed Lebanon](globemedlebanon.com/) insurance company and the healthcare providers that are associated with the company, in addition it uses [Google Places API] (https://cloud.google.com/maps-platform/places/). The ChatBot could also check the database to inform clients about their claims.

### Link the bot to the QnA knowledge base and database

In order to run the bot properly, you will need the configuration file that contains the database and knowledge base credentials.
this file should be named **config.py** and placed in the repository main directory.

## Running the sample
- Clone the repository
```bash
git clone https://github.com/Microsoft/botbuilder-samples.git
```
- Bring up a terminal, navigate to `botbuilder-samples\samples\python\11.qnamaker` folder
- Activate your desired virtual environment
- In the terminal, type `pip install -r requirements.txt`
- Add the `config.py` file
- Run your bot with `python app.py`

## Testing the bot using Bot Framework Emulator
[Microsoft Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework emulator from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to bot using Bot Framework Emulator
- Launch Bot Framework Emulator
- File -> Open Bot
- Paste this URL in the emulator window - http://localhost:3978/api/messages

## Deploy the bot to Azure

To learn more about deploying a bot to Azure, see [Deploy your bot to Azure](https://aka.ms/azuredeployment) for a complete list of deployment instructions.

# Further reading

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [QnA Maker Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/qnamaker/overview/overview)
- [Activity processing](https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-concept-activity-processing?view=azure-bot-service-4.0)
- [QnA Maker CLI](https://github.com/Microsoft/botbuilder-tools/tree/master/packages/QnAMaker)
- [Channels and Bot Connector Service](https://docs.microsoft.com/en-us/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)- [Azure 
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Azure CLI](https://docs.microsoft.com/cli/azure/?view=azure-cli-latest)
- [Azure Portal](https://portal.azure.com)
