# automate the task of creating a custom HTTP header response, but with Puppet.
exec { 'apt-update':
    command => '/usr/bin/apt-get update'
}
package { 'nginx':
    ensure => 'installed',
}
file_line{ 'config nginx':
    path  => '/etc/nginx/nginx.conf',
    line  => "http {\n\tadd_header X-Served-By ${hostname};",
    match => 'http {',

}
exec { 'sudo service nginx restart':
    command => '/usr/sbin/service nginx restart',
}
