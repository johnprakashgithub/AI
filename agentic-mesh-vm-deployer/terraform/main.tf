# Placeholder: assumes use of local-exec with Multipass
provider "local" {}
resource "null_resource" "launch_vm" {
  count = 1
  provisioner "local-exec" {
    command = "multipass launch --name agentic-vm-${count.index}"
  }
}
