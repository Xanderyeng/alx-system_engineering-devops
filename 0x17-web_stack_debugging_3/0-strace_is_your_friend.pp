# Using Puppet, create a manifest to fix server problem. Fix typo error in file extension.
exec { 'fix typo error in php extension':
    command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
