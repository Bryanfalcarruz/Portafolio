data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Role y políticas para SSM y S3
resource "aws_iam_role" "ec2_role" {
  name = "${var.project_name}-ec2-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action    = "sts:AssumeRole"
    }]
  })

  tags = var.tags
}

resource "aws_iam_role_policy_attachment" "ssm_managed" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_role_policy_attachment" "s3_readonly" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

resource "aws_iam_instance_profile" "ec2_profile" {
  name = "${var.project_name}-ec2-profile"
  role = aws_iam_role.ec2_role.name
}

# Script de inicialización
locals {
  user_data = <<-EOF
    #!/bin/bash
    set -e

    # Docker
    yum update -y
    amazon-linux-extras install docker -y
    systemctl enable docker
    systemctl start docker
    usermod -aG docker ec2-user

    echo "Docker OK $(date)" >> /var/log/user-data.log

    # --- Pull & Run desde ECR (solo si se pasó ecr_repository_url) ---
    REPO_URL="${var.ecr_repository_url}"
    IMAGE_TAG="${var.image_tag}"

    if [ -n "$REPO_URL" ]; then
      REGION="$(curl -s 169.254.169.254/latest/dynamic/instance-identity/document | grep region | cut -d '\"' -f4)"
      aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $REPO_URL

      docker pull ${var.ecr_repository_url}:${var.image_tag} || exit 1
      # Detener contenedor previo si existe
      docker rm -f file-organizer || true
      # Ejecutar contenedor
      docker run -d --name file-organizer ${var.ecr_repository_url}:${var.image_tag}
      echo "Contenedor lanzado desde ${var.ecr_repository_url}:${var.image_tag}" >> /var/log/user-data.log
    else
      echo "ECR REPO vacío; no se ejecuta contenedor" >> /var/log/user-data.log
    fi
  EOF
}

# Instancia EC2
resource "aws_instance" "file_organizer_ec2" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = var.instance_type
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [var.sg_id]
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name
  user_data              = local.user_data

  associate_public_ip_address = true
  monitoring                  = true

  tags = merge(var.tags, {
    Name = "${var.project_name}-ec2"
  })
}

resource "aws_iam_role_policy_attachment" "ecr_readonly" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}