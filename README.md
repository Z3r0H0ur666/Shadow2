# Shadow Traffic
 #       v.1.1
This small tool will help you to increase your blog view traffic with Differnet IP for each request with different User-agent.


# Requirements 

1) Tor
2) stem library
3) Python3

# Tested on kali Linux,Ubuntu,Debian

works only on Linux

# ! Installation !

Linux

`apt-get install tor`

Now open tor configuration file it is usually located in /etc/tor/torrc and uncomment following lines.

`ControlPort 9051`

`HashedControlPassword "your password"`

Save the file and exit.


`pip install stem`

`pip install pysocks`
`install selenium`
`install firefox webdrive and add the path`

`service tor restart`

If you are using both python version on single machine use pip3 for python3

# How to use

`git clone https://github.com/c0d3l3ss/shadow-traffic.git`

`cd Shadow-Traffic`

`chmod 744 shadows.py`
`python3 shadows.py`

`enter your tor password from torrc file`

`enter blog address with protocol`

`enter number of views you want`

`Now blog will be visited with different ip and User-Agent`

# Support

https://twitter.com/c03d3lss

This is in beta version and support for this is minimal.

# Disclaimer

Author will not take any responsibility of your activity using this tool.
For Educational purpose only.

# Credits
@c0d3l3ss

# License

MIT License
