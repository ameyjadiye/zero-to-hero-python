#! /usr/bin/env python
#sudo pip install python-memcached

import memcache
import sys

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
mc.set("key","this is a test value :)")
#for specific ammount of time use third parameter
#mc.set("key","value",2592000) 
print mc.get("key")

mc.delete("key")
print "After deletion!! it says value as a ", mc.get("key")
