# tests/config_check.tftest.hcl
run "check_file" {
  command = "apply"
  assert {
    condition = fileexists("/tmp/hello.txt")
    error_message = "Config file not found"
  }
}

