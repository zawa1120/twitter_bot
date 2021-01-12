provider "google" {
  project     = var.project
  region      = "us-central1"
}

resource "google_pubsub_topic" "topic" {
  name = var.name
}

resource "google_cloud_scheduler_job" "pubsub_scheduler" {
  name        = var.name
  region      = var.region
  project     = var.project
  schedule    = var.cron
  time_zone   = var.time_zone

  pubsub_target {
    topic_name = google_pubsub_topic.topic.id
    data       = base64encode(var.name)
  }
}
