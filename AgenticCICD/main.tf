# main.tf
provider "local" {}

resource "null_resource" "create_vm" {
  provisioner "local-exec" {
    command = "multipass launch --name test-vm-${count.index} --mem 1G --disk 5G --cpus 1"
  }

  count = 2
}

