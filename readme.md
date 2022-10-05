# SML Portal

This repo contains the build environment and code to generate and upload the Statistical Methods Library (SML) Portal website.

## Build and deploy

### S3 Bucket creation

[Terraform](https://www.terraform.io/intro) is used to deploy the S3 Bucket where the website is hosted. The S3 bucket will be suffixed with the currently checked-out gt branch name.

Fetch your AWS credentials and export them to the terminal. Then:

```shell
./terraform.sh apply
```

This command will output the URL for your new site, and will have the form `https://xxxxxxx.cloudfront.net/`.

### Fetch ONS Design System

Download the release of the ONS Design System, and unpack them into the correct location with this command:

```shell
./get_design_system.sh
```

### Make the site

You will first need to install the python dependencies, including [Frozen-flask](https://pythonhosted.org/Frozen-Flask/), the static website generator:

```shell
pipenv sync
```

With [Jsonnet](https://jsonnet.org/learning/getting_started.html) content in the `content/` directory, you should now be able to run the Flask demo server:

```shell
pipenv run flask --app sml_builder --debug run
```

If this all goes well with no errors, you should now be able to navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the site. And if that all looks good, you can now "freeze" the site, rendering it to HTML, and uploading it to AWS. You will need to have valid AWS credentials exported to the shell for the target environment.

```shell
./freeze-n-load.sh
```

## Destroying your site

When you have merged, or have otherwise finished with your feature branch, you will want to delete the deployed site. Simply run:

```shell
./terraform.sh destroy
```

## Troubleshooting

* __Access denied message when trying to reach CloudFront URL__
  * One common cause of this error message is not having uploaded your site yet.
  * Are you coming from a non-UK IP address, possbly due to a VPN being active? If so, switch this off and try again. Geographical restrictions are in place.

