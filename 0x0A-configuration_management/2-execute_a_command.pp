# Using Puppet to create a manifest that kills a process named killmenow
exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => ['/usr/bin', '/bin'],  # Add other paths if necessary
  refreshonly => true,
}
