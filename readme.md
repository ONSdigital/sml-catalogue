# SML Portal

This repo contains the build environment and code to generate and upload the Statistical Methods Library (SML) Portal Web Application.

## Prerequisites

Before continuing, install the following tools:

[**Homebrew**](https://brew.sh/): Follow the instructions on this page

[**Python 3.10.0**](https://www.python.org/downloads/macos/): To install python on your local system, you can visit this link and install the relevant version (Python 3.10.0)

You will need to install pipenv to install the python dependencies and pyenv if you want to manage multiple versions of python. Refer to the [confluence page](https://confluence.ons.gov.uk/pages/viewpage.action?pageId=14902311) for guidance on this.

## Build and Deploy

### Fetch the ONS Design System

Download the release of the ONS Design System, and unpack them into the correct location with this command:

```bash
./get_design_system.sh
```

## Make the site

You will need to install the python dependencies, including Frozen-Flask, the static website generator:

```bash
pipenv sync
```

With Jsonnet content in the content/ directory, you should now be able to run the Flask demo server:

```bash
pipenv run flask --app sml_builder --debug run
```

If everything runs without errors (If you have the latest macOS version this app may crash or not run as of now macOS Monterey control center uses port 5000. In this case give a another port number), you should now be able to navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the site.

## Troubleshooting

### Access denied message when trying to reach CloudFront URL

- One common cause of this error message is not having uploaded your site yet.
- Are you coming from a non-UK IP address, possibly due to a VPN being active? If so, switch this off and try again. Geographical restrictions are in place.

**If you have any errors running the pipenv sync command and running the web app or any other errors, it maybe because of issues relating to your latest macOS version and xcode command line tools installed. You can try the command below where you will remove and reinstall Xcode command line tools:**

```bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
/usr/bin/xcodebuild -version```
