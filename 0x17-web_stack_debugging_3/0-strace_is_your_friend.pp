# A puppet scipt to change a line in a file on a server
$filetoedit = '/var/www/html/wp-settings.php'
# Replace the line in the wp-settings.php file containing "phpp" with "php"
exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${filetoedit}",
  path    => ['/bin','/usr/bin']
}
