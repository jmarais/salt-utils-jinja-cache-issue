# salt-utils-jinja-cache-issue
example of a file client cache issue when instantiating two salt callers with different 'cachedir's 

run:
```
make run
```

version:

```terminal
$ python3 -c "import salt.version; print(salt.version.__version__)"
3004.2
```

```terminal
Salt Version:
          Salt: 3004.2

Dependency Versions:
          cffi: Not Installed
      cherrypy: Not Installed
      dateutil: Not Installed
     docker-py: Not Installed
         gitdb: Not Installed
     gitpython: Not Installed
        Jinja2: 3.1.2
       libgit2: Not Installed
      M2Crypto: Not Installed
          Mako: Not Installed
       msgpack: 1.0.4
  msgpack-pure: Not Installed
  mysql-python: Not Installed
     pycparser: Not Installed
      pycrypto: Not Installed
  pycryptodome: 3.15.0
        pygit2: Not Installed
        Python: 3.8.12 (default, Sep 21 2021, 00:10:52)
  python-gnupg: Not Installed
        PyYAML: 6.0
         PyZMQ: 21.0.2
         smmap: Not Installed
       timelib: Not Installed
       Tornado: 4.5.3
           ZMQ: 4.3.3

System Versions:
          dist: centos 8
        locale: utf-8
       machine: x86_64
       release: 4.18.0-373.el8.x86_64
        system: Linux
       version: CentOS Stream 8
```
