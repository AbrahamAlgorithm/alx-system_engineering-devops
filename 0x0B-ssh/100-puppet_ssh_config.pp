# Client configuration file (w/ Puppet)
include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  path    => '/home/your_username/.ssh/config', # Replace 'your_username' with your actual username
  line    => 'IdentityFile ~/.ssh/school',
  ensure  => present,
  replace => true,
}

