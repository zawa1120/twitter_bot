gcloud functions deploy acplus_accounts --region us-central1 --entry-point main --memory 2048MB --runtime python37 --timeout 540s --env-vars-file env.yaml --trigger-topic acplus_accounts
