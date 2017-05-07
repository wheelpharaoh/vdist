## How to install
Before installing vdist, it is important that you have the Docker daemon
running. I recommend getting the latest version of Docker to use with vdist.

### Install from Pypi
Installing vdist is as easy as this:
```
$ pip install vdist
```
The vdist executable will be placed in /bin folder of python interpreter folder
you used when calling pip (e.g. if you called pip from a virtualenv, vdist
executable will be placed in virtualenv's bin folder).

### Install in Ubuntu using deb package
You can download a deb package from [releases](https://github.com/dante-signal31/vdist/releases)
section of vdist GitHub page. To install it locally resolving dependencies type:
```
$ sudo apt-get update
$ sudo dpkg -i <vdist_deb_package>.deb
$ sudo apt-get -f install
```

Alternatively, you can configure vdist's apt repository and download package
from there. This is the preferred way of installation because using apt
repository has the benefit of continuous updates so you
have not to check vdist website to get updates. To configure vdist's apt
repository and install from there, type:
```
$ sudo apt-get update
$ sudo apt-get install apt-transport-https
$ sudo echo "deb [trusted=yes] https://dl.bintray.com/dante-signal31/deb generic main" | tee -a /etc/apt/sources.list
$ sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 379CE192D401AB61
$ sudo apt-get update
$ sudo apt-get install vdist
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

Alternatively, you can configure vdist's yum repository and download package
from there. This is the preferred way of installation because using yum
repository has the benefit of continuous updates so you
have not to check vdist website to get updates. To configure vdist's yum
repository and install from there, type:
```
$ wget https://bintray.com/dante-signal31/rpm/rpm -O bintray-dante-signal31-rpm.repo
$ sudo mv bintray-dante-signal31-rpm.repo /etc/yum.repos.d/
$ sudo yum install -y yum-utils
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
$ yum update
$ yum install vdist
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
