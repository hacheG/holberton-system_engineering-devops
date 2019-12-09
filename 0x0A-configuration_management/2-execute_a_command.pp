#process has been terminated
exec {'killmenow':
command  => 'pkill -f killmenow',
provider => 'shell',
}
