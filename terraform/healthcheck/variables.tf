variable "domain_name_base" {
  type = string
}

variable "environment" {
  type = string
}

variable "url" {
  type = string
  default = "https://${var.domain_name_base[var.environment]}"
}

variable "expected_string" {
  type = string
  default = "An open source library for statistical code approved by the ONS"
}

variable "email" {
  type = string
  default = "SMLAdmin@ons.gov.uk"
}