# SML Portal

This repo contains the build environment and code to generate and upload the Statistical Methods Library (SML) Portal Web Application.

## Prerequisites

Before continuing, install the following tools:

[**Homebrew**](https://brew.sh/): Follow the instructions on this page

[**Python**](https://www.python.org/downloads/macos/): To install the correct version of python on your local system, check the pyproject.toml and then install the relevant version.

You will need to install [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) to install the python dependencies. If you want to manage multiple versions of python you will need to install `pyenv`.

Refer to the [confluence page](https://confluence.ons.gov.uk/display/ESD/Guide+on+using+pipenv%2C+pyenv%2C+poetry+and+venv) for guidance on installing and using pyenv and poetry.

You will also need to have installed [wget](https://formulae.brew.sh/formula/wget) to fetch the `ONS Design System`.

## Build and Deploy

### Fetch the ONS Design System

Download the release of the ONS Design System, and unpack them into the correct location with this command:

```bash
./get_design_system.sh
```

## Make the site

You will need to install the python dependencies, including `Frozen-Flask`, the static website generator:

```bash
poetry install
```

You can activate your virtual environment with the following command:

```bash
poetry shell
```

With Jsonnet content in the content/ directory, you should now be able to run the Flask demo server:

```bash
poetry run flask --app sml_builder --debug run
```

If everything runs without errors, you should now be able to navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the site.

## Linters & Security Scan

To run the linters (`Pylint & Flake8`) and security scan (`Bandit`):

```bash
sudo ./run_py_tools.sh
```

## Troubleshooting

### Access denied message when trying to reach CloudFront URL

- One common cause of this error message is not having uploaded your site yet.
- Are you coming from a non-UK IP address, possibly due to a VPN being active? If so, switch this off and try again. Geographical restrictions are in place.

If you have any errors running the web app or any other errors, it maybe because of issues relating to your latest macOS version and Xcode command line tools installed. You can try the command below where you will remove and reinstall Xcode command line tools:

```bash
sudo rm -rf /Library/Developer/CommandLineTools
xcode-select --install
/usr/bin/xcodebuild -version
```

If you experience any problems launching the application check the version of macOS installed, as problems can arise if you are using macOS Monterey and following versions uses port 5000 for its control center causing a conflict.

If another program is already using port 5000, you may see the error ```OSError: [Errno 98] or OSError: [WinError 10013]``` when the server tries to start.

In this case run the following command, replacing it with the port you want the web app to run on, so that the application is launched on a different port.

```bash
poetry run flask --app sml_builder --debug run --port=8000
```

## Behaviour tests

The selenium behaviour tests can be run using the following command. If you are running the web app on a different port than port 5000, please change the port number below before running the command.

```bash
behave -D host=http://127.0.0.1:5000/
```

This will run the behaviour test locally in a headless state. If you want to see the GUI browser tests running then go to the setupSelenium.py file and comment the headless boolean.

Note: Investigation was undertaken to automate the behavior tests as part of the pipeline github action workflows.

However, we discovered the github agents are hosted in the United States and when visiting our services url, the runner routed to our 'page not found' webpage.

Hence as the page can only be accessed from within the uk we cannot automate the tests in the pipeline.

## Concourse Setup

Prod and preprod are served as one pipeline which runs main

```shell
fly set-pipeline \
-t aws-sml \
-p live-sml-catalogue \
-c ci/live-pipeline.yml
```

While Dev is set as another

```shell
fly set-pipeline \
-t aws-sml \
-p dev-sml-catalogue \
-c ci/dev-pipeline.yml
```

To delete these run the commands

```shell
fly destroy-pipeline -t aws-sml -p live-sml-catalogue
```

and

```shell
fly destroy-pipeline -t aws-sml -p dev-sml-catalogue
```

When running the production pipeline we need to run it via fly execute in order to pass the tag version
to deploy to production, this can be done as so:

```shell
fly execute \
-t aws-sml \
-p live-sml-catalogue \
-v RELEASE_CANDIDATE="tag_version, e.g 1.1.0_rc.1" \
-c ci/live-pipeline.yml
```
