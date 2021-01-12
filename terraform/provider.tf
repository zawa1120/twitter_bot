provider "google" {
  credentials = "${file("C:/gcp")}"
  project     = "${lookup(var.project_name, "${terraform.workspace}")}"
  region      = "us-central1"
}
