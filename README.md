# twitter_bot

## How to deploy Terraform
1. Connect a pass
```
$ cd terraform
```
2. 
```
$ gcloud iam service-accounts create [terraform-serviceaccount_name] --display-name "Account for Terraform"
$ gcloud projects add-iam-policy-binding [PROJECT_ID] --member serviceAccount:[terraform-serviceaccount_name]@[PROJECT_ID].iam.gserviceaccount.com --role roles/editor
```
3. Generate a service account key and set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the service account key.
```
$ gcloud iam service-accounts keys create [gcp/account.json] --iam-account [terraform-serviceaccount_name]@[PROJECT_ID].iam.gserviceaccount.com
$ export GOOGLE_CLOUD_KEYFILE_JSON=[gcp/account.json]
```

```
terraform init
```

```
terraform plan
```

```
terraform apply
```
