variable "domain_name_base" {
  type = string
}

variable "email" {
  sml_admin = "SMLAdmin@ons.gov.uk"
}

variable "environment" {
  type = string
}

variable "input" {
  "url" = "https://${var.domain_name_base[var.environment]}"
  "text" = "An open source library for statistical code approved by the ONS"
}