variable "name" {
  default     = "Test"
  type        = string
}

variable "region" {
  default     = "us-central1"
  type        = string
}

variable "project" {
  default     = "helpful-rope-300817"
  type        = string
}

variable "cron" {
  default     = "0 12 * * *"
  type        = string
}

variable "time_zone" {
  default     = "Asia/Tokyo"
  type        = string
}
