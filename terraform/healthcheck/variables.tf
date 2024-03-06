variable "domain_name_base" {
  type = string
}

variable "environment" {
  type = string
}

variable "link" {
  link = "https://${var.domain_name_base[var.environment]}"
}

variable "expected_string" {
  expected_string = "An open source library for statistical code approved by the ONS"
}

variable "email" {
  email = "SMLAdmin@ons.gov.uk"
}