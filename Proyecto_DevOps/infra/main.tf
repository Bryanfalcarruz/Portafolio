module "network" {
  source             = "./modules/network"
  project_name       = var.project_name
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
  tags               = var.tags
}

module "compute" {
  source      = "./modules/compute"
  project_name = var.project_name
  subnet_id    = module.network.public_subnet_id
  sg_id        = module.network.sg_base_id
  tags         = var.tags
}