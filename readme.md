# SML Portal

This repo contains the build environment and code to generate and upload the Statistical Methods Library (SML) Portal Web Application.

## Prerequisites

Before continuing, install the following tools:

[**Homebrew**](https://brew.sh/): Follow the instructions on this page

[**Python**](https://www.python.org/downloads/macos/): To install the correct version of python on your local system, check the pipfile and then install the relevant version.

You will need to install [pipenv](https://pypi.org/project/pipenv/) to install the python dependencies. If you want to manage multiple versions of python you will need to install `pyenv`.

Refer to the [confluence page](https://confluence.ons.gov.uk/display/ESD/Guide+on+using+pipenv%2C+pyenv+and+venv) for guidance installing and using pipenv and pyenv.

You will also need to have installed [wget](https://formulae.brew.sh/formula/wget) to fecth the `ONS Design System`.

## Build and Deploy

### Fetch the ONS Design System

Download the release of the ONS Design System, and unpack them into the correct location with this command:

```bash
./get_design_system.sh
```

## Make the site

You will need to install the python dependencies, including `Frozen-Flask`, the static website generator:

```bash
pipenv sync
```

With Jsonnet content in the content/ directory, you should now be able to run the Flask demo server:

```bash
pipenv run flask --app sml_builder --debug run
```

If everything runs without errors, you should now be able to navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the site.

## Troubleshooting

### Access denied message when trying to reach CloudFront URL

- One common cause of this error message is not having uploaded your site yet.
- Are you coming from a non-UK IP address, possibly due to a VPN being active? If so, switch this off and try again. Geographical restrictions are in place.

If you have any errors running the pipenv sync command and running the web app or any other errors, it maybe because of issues relating to your latest macOS version and Xcode command line tools installed. You can try the command below where you will remove and reinstall Xcode command line tools:

```bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
/usr/bin/xcodebuild -version
```

If you experience any problems launching the application check the version of macOS installed, as problems can arise if you are using macOS Monterey and following versions uses port 5000 for its control center causing a conflict.

If another program is already using port 5000, you may see the error ```OSError: [Errno 98] or OSError: [WinError 10013]``` when the server tries to start.

In this case run the following command, replacing it with the port you want the web app to run on, so that the application is launched on a different port.

```bash
pipenv run flask --app sml_builder --debug run --port=8000
```
