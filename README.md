#npserverlist.py

##NAME

`npserverlist.py`


##SYNOPSIS

    npserverlist.py ZONE-NAME


##DESCRIPTION

`npserverlist.py` is a command-line tool that gets the NTP pool server list by
the given zone-name.

The zone-name is either the name of a continent (such as "asia" or
"north-america"), or a two-letter country code (such as "uk", "fr", or "jp").
An unrecognized zone-name will either be rejected before querying the web
source, or result in an error after querying the web source and failing.

Error messages, if any, are written to the standard error.


##EXIT CODE

* 0:  The program exits successfully.
* 1:  Error retrieving server list from ntp.org website.
* 2:  Invalid input.


##ENVIRONMENT

* `http_proxy`: HTTP proxy server.


##EXAMPLE

* `npserverlist.py hk`:  Get NTP servers for the zone "HK" (Hong Kong).
* `npserverlist.py hk | sed -e "s/$/ iburst/g" | cat - ntp-boilerplate >
  /etc/ntp.conf`:  Create `/etc/ntp.conf` (or `/etc/chrony.conf`) from a
  template file `ntp-boilerplate`, adding `iburst` option to the `server`
  directives.


##SEE ALSO

* NTP Pool Project: [http://www.pool.ntp.org/](http://www.pool.ntp.org/ "NTP
  Pool Project")


## COPYRIGHT

Copyright © 2014 Cong Ma.  License BSD: See the COPYING file.

This is free software: you are free to change and redistribute it.  There is NO
WARRANTY, to the extent permitted by law.


##AVAILABILITY

[https://github.com/congma/npserverlist.py/](https://github.com/congma/npserverlist.py/)
