variable "name" {
  type        = string
}

variable "region" {
  default     = "us-central1"
  type        = string
}

variable "project" {
  default     = "practice cloud function"
  type        = string
}

variable "cron" {
  default     = "0 0 * * *"
  type        = string
}

variable "time_zone" {
  default     = "Asia/Tokyo"
  type        = string
}
