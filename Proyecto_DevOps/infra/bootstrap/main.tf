resource "random_string" "suffix" {
  length  = 6
  upper   = false
  special = false
}

locals {
  tags = {
    Project = var.project_name
    Env     = "global"
    Owner   = "bryan"
  }

  # S3: nombre único global, cumple reglas de bucket
  tfstate_bucket = "tfstate-${var.project_name}-${random_string.suffix.result}"
  lock_table     = "tf-lock-${var.project_name}"
}

# S3 bucket para state
resource "aws_s3_bucket" "tfstate" {
  bucket = local.tfstate_bucket
  tags   = local.tags
}

# Dueño de objetos forzado al bucket (evita problemas con ACLs)
resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.tfstate.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
# Bloqueo de acceso público
resource "aws_s3_bucket_public_access_block" "this" {
  bucket                  = aws_s3_bucket.tfstate.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
  depends_on = [aws_s3_bucket_ownership_controls.this]
}

# Versionado
resource "aws_s3_bucket_versioning" "this" {
  bucket = aws_s3_bucket.tfstate.id
  versioning_configuration { status = "Enabled" }
}

# Cifrado en servidor
resource "aws_s3_bucket_server_side_encryption_configuration" "this" {
  bucket = aws_s3_bucket.tfstate.id
  rule { apply_server_side_encryption_by_default { sse_algorithm = "AES256" } }
}

# DynamoDB: locking del state
resource "aws_dynamodb_table" "lock" {
  name         = local.lock_table
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = local.tags
}
