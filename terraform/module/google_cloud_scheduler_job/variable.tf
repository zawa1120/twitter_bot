variable "name" {
  description = "Cloud Functions Function name"
  type        = string
}

variable "cron" {
  description = "Cloud Scheduler Cron"
  default     = "0 0 * * *"
  type        = string
}

variable "time_zone" {
  description = "Cloud Scheduler Timezone"
  default     = "Asia/Tokyo"
  type        = string
}

variable "region" {
  description = "Cloud Scheduler Region"
  default     = "us-central1"
  type        = string
}
