module "twitter_bot" {
  source = "./module/google_cloud_scheduler_job"
  name   = "twitter_bot"
}