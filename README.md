# twitter_bot
Practice Google Cloud Platform and Terraform

## How to deploy Terraform
```
Terraform version 0.14.7.
```
1. Connect a pass
```
$ cd terraform
```
2. Create a service account of Terraform and authorize the account. Name the service accounts "terraform-serviceaccount_name".
```
$ gcloud iam service-accounts create [terraform-serviceaccount_name] --display-name "Account for Terraform"
$ gcloud projects add-iam-policy-binding [PROJECT_ID] --member serviceAccount:[terraform-serviceaccount_name]@[PROJECT_ID].iam.gserviceaccount.com --role roles/editor
```
3. Generate a service account key and set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the service account key. Name the file "account.json".
```
$ gcloud iam service-accounts keys create [gcp/account.json] --iam-account [terraform-serviceaccount_name]@[PROJECT_ID].iam.gserviceaccount.com
$ (win)set GOOGLE_CLOUD_KEYFILE_JSON=[gcp/account.json]
$ (mac)export GOOGLE_CLOUD_KEYFILE_JSON=[gcp/account.json]
```
4. Initialize terraform script.
```
$ terraform init
```
5. Check the differences.
```
$ terraform plan
```
6. Deploy Terraform
```
$ terraform apply
```

### Reference source
https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account
https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference
https://www.devsamurai.com/ja/gcp-terraform-101/

## How to deploy Cloud functions
1. Connect a pass
```
$ cd functions
```
2. Deploy Cloud functions
```
$ (win)gcloud functions deploy twitter_bot --region us-central1 --entry-point main --runtime python37 --timeout 540s --env-vars-file env.yaml --trigger-topic twitter_bot
$ (mac)bash deploy.sh
```
