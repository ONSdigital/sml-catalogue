# SML Catalogue

This repo contains the build environment and code to generate and upload the Statistical Methods Library (SML) Catalogue website.

## Build and deploy

### S3 Bucket creation

[Terraform](https://www.terraform.io/intro) is used to deploy the S3 Bucket where the website is hosted. The S3 bucket will be suffixed with the currently checked-out gt branch name.

Fetch your AWS credentials and export them to the terminal. Then:

```shell
cd terraform
terraform init
terraform apply \
  -var "suffix=`git branch --show-current`"
```

### Make the site

You will first need to install the [Pelican](https://docs.getpelican.com/en/latest/index.html) static website generator:

```shell
pipenv sync
```

With [markdown](https://www.markdownguide.org/basic-syntax) content in the `content/` directory, you should now be able to generate the HTML output with:

```shell
pipenv run make devserver
```

If this all goes well with no errors, you should now be able to navigate to [https//:localhost:8000](https//:localhost:8000) to view the site. And if that all looks good, you can now upload to the S3 bucket (assuming you still have valid AWS credentials exported to the terminal):

```shell
pipenv run make s3_upload
```
