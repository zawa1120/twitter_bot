# twitter_bot

## How to deploy Terraform
1. Connect a pass
```
$ cd terraform
```
2. Generate a service account key and set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the service account key.
```
$ gcloud iam service-accounts create [account_name] --display-name "Account for Terraform"
$ gcloud projects add-iam-policy-binding [PROJECT_ID] --member serviceAccount:[account_name]@[PROJECT_ID].iam.gserviceaccount.com --role roles/editor
$ export GOOGLE_CLOUD_KEYFILE_JSON=path_to/account.json
```
