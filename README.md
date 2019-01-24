# vmsuperhub-smnp
### Virgin Media Superhub 3 SNMP

Uses or abuses(?) the snmp functions from the web interface of the Virgin Superhub 3.

Some useful object identifiers (OIDs):
```
"WPAPreSharedKey","1.3.6.1.4.1.4115.1.20.1.1.3.26.1.2"
"BssSSID","1.3.6.1.4.1.4115.1.20.1.1.3.22.1.2
```

Other OIDs can be captured while browsing the web interface.


#### How to
This assumes the router IP is `192.168.0.1`.
```
git clone https://github.com/alexmartinio/vmsuperhub-smnp.git
cd vmsuperhub-smnp
python3 app.py 
# or just python depending on environment 
```
The app should prompt for the router admin password if it is not already set in the `.env` file.


#### Sources
- https://ninet.org/2018/06/fixing-the-virgin-media-superhub-3/
- https://community.virginmedia.com/t5/Networking-and-WiFi/Internal-network-SNMP/m-p/3726482
- http://hackingandsecurity.blogspot.com/2016/05/arris-cable-modem-backdoor-im.html
