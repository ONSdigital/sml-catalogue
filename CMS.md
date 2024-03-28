# SML Portal - Content Management System using Contentful

This markdown document contains relevant information on the content management system (CMS), Contentful.

Below are key information regarding setup and usage of the CMS.

## Prerequisites

Before continuing, please make sure you know/ have already installed the prerequisites for the SML Portal website project, you can build and deploy the site locally. If not you can find instructions on how to do this here: [**SML Website Project README**](https://github.com/ONSdigital/sml-catalogue/blob/main/README.md)

Now you will have installed the required packages including the `Contentful Python SDK` which is required to work with Contentful.

## Local setup

For the Contentful API to work on your local machine, you also need to ensure that you have the API key and space ID defined in your zsh or bash profile.

These are accessible directly through the Contentful website if you have the correct permissions for the space you are working in.

You can access the API key by navigating to Settings > API keys.

If you don't have access to these, you likely don't have the right permissions and should contact the space owner.

Open up your zsh or bash profile in an editor of your choice and define two variables:

ZSH:

```zsh
export SPACE_ID = "your_space_ID"
export CDA_KEY = "your_cda_key"
```

BASH:

```bash
SPACE_ID = "your_space_ID"
CDA_KEY = "your_cda_key"
```

## Build and deploy

You can find instructions on how to build and deploy the SML Portal website here: [**SML Website Project README**](https://github.com/ONSdigital/sml-catalogue/blob/main/README.md)

Now when you navigate to the Contentful web interface, create new content or make any content changes, it should reflect the changes locally on the SML Portal website.

## Key information regarding the CMS

[**Contentful Overview**](https://www.contentful.com/help/contentful-101/): Contains guidance on getting started with setting up Contentful, content models, managing content, managing users etc.

[**Contentful API Reference**](https://www.contentful.com/developers/docs/references/): Guidance on Content Delivery API (used to retrieve published content to display in your application), Content Management API, Content Preview API and various other APIs.

[**Contentful Python SDK**](https://github.com/contentful/contentful.py): This Python SDK client library interacts with the Content Delivery API, a read-only API for retrieving content from Contentful. All content, both JSON and binary, is fetched from the server closest to a user's location using our global CDN.

## Other Useful Links

[**Python Client Libraries (SDK)**](https://www.contentful.com/developers/docs/python/sdks/)

[**Python Tutorials/ Demos using Contentful**](https://www.contentful.com/developers/docs/python/tutorials/)

[**Contentful Concepts**](https://www.contentful.com/developers/docs/concepts/)

## Troubleshooting

### Having issues when trying to pull down published content using the Content Delivery API (CDA)

- This can occur when the owner of the workspace hasn't given you the correct roles and or permissions.
- CDA Key and or Space ID are incorrect in your bash or zsh profile.
