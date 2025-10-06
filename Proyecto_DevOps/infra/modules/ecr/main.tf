resource "aws_ecr_repository" "this" {
  name                 = "${var.project_name}-repo"
  image_tag_mutability = var.image_mutability

  image_scanning_configuration {
    scan_on_push = var.scan_on_push
  }

  encryption_configuration {
    encryption_type = var.encryption_type
    kms_key         = var.encryption_type == "KMS" ? var.kms_key_arn : null
  }

  tags = var.tags
}

# (Opcional) Política de ciclo de vida: conservar últimas 10 imágenes por tag
resource "aws_ecr_lifecycle_policy" "keep_last_10" {
  repository = aws_ecr_repository.this.name

  policy = jsonencode({
    rules = [{
      rulePriority = 1,
      description  = "Conservar últimas 10 imágenes por tag"
      selection = {
        tagStatus     = "tagged"
        tagPrefixList = ["latest"]
        countType     = "imageCountMoreThan"
        countNumber   = 10
      }
      action = { type = "expire" }
    }]
  })
}
