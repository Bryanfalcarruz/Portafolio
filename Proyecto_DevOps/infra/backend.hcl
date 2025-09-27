bucket               = "tfstate-file-organizer-bs79xp"
region               = "us-west-2"
dynamodb_table       = "tf-lock-file-organizer"
key                  = "terraform.tfstate"
workspace_key_prefix = "infra"
encrypt              = true