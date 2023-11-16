# Puppet script that extend the limit of results from 15 to 1024.
exec { 'limit':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/15/1024/' /etc/default/nginx",
}
-> exec { 'restart':
  path    => '/usr/bin/',
  command => 'service nginx restart',
}
