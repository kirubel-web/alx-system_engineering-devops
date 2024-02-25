# SSH client configuration must be configured to
# use the private key ~/.ssh/school
# SSH client configuration must be configured to
# refuse to authenticate using a password
exec { 'ssh_config':
  path    => '/bin',
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config'
}
