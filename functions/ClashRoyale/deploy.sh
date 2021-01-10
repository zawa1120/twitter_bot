gcloud functions deploy twitter_bot --region us-central1 --entry-point main --memory 30MB --runtime python37 --timeout 540s --env-vars-file env.yaml --trigger-topic twitter_bot
