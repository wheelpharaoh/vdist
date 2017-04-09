## How to install
Before installing vdist, it is important that you have the Docker daemon
running. I recommend getting the latest version of Docker to use with vdist.

### Install from Pypi
Installing vdist is as easy as this:
```
$ pip install vdist
```

### Install in Ubuntu using deb package
You can download a deb package from [releases](https://github.com/dante-signal31/vdist/releases)
section of vdist GitHub page. To install it locally resolving dependencies type:
```
$ sudo apt-get update
$ sudo dpkg -i <vdist_deb_package>.deb
$ sudo apt-get -f install
```

### Install in Centos using rpm package
You can download a rpm package from [releases](https://github.com/dante-signal31/vdist/releases)
section of vdist GitHub page. Be aware that vdist depends on docker-ce package
that it is not available in standard centos repositories. So you should add
docker repositories before installing vdist:
```
$ sudo yum install -y yum-utils
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```
Afterwards you can install vdist rpm packages locally resolving dependencies.
Just type:
```
$ sudo yum --nogpgcheck localinstall <vdist_rpm_package>.rpm
```

### Install from GitHub
Alternatively, you can clone the source directly from Github and install its
dependencies via pip. When doing that, I recommend using virtualenv. For
example:

```
$ git clone https://github.com/objectified/vdist
$ cd vdist
$ virtualenv .
$ . bin/activate
$ pip install -r requirements.txt
```
