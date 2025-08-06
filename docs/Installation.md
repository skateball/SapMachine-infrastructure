# Contents
* [Linux](https://github.com/SAP/SapMachine/wiki/Installation#-linux)
* [macOS](https://github.com/SAP/SapMachine/wiki/Installation#-macos)
* [Windows](https://github.com/SAP/SapMachine/wiki/Installation#-windows)
* [SDKMAN](https://github.com/SAP/SapMachine/wiki/Installation#-sdkman)

## [](#Linux) Linux

### Debian or Ubuntu

1. Add the SapMachine GPG key

```
wget -qO- https://dist.sapmachine.io/debian/sapmachine.key | sudo tee /etc/apt/trusted.gpg.d/sapmachine.asc > /dev/null
```

2. Add the SapMachine repository

```
echo "deb https://dist.sapmachine.io/debian/$(dpkg --print-architecture)/ ./" | sudo tee /etc/apt/sources.list.d/sapmachine.list >/dev/null
```

3. Install the desired SapMachine version(s)

```
apt-get update
apt-get install sapmachine-21-jdk
```

### Alpine

1. Add the SapMachine RSA key

```
wget -qO /etc/apk/keys/sapmachine-apk.rsa.pub https://dist.sapmachine.io/alpine/sapmachine-apk.rsa.pub
```

2. Add the SapMachine APK repository

```
echo "https://dist.sapmachine.io/alpine" >> /etc/apk/repositories
```

3. Install the desired SapMachine version(s)

```
apk add sapmachine-21-jdk
```

### RPM

On RPM-based systems, e.g. Fedora, CentOS, or OpenSUSE, you can use our `.rpm` packages.

#### Using yum

To use SapMachine RPM repositories with the yum package manager, you need to import the public key and add the repository to the system list. E.g. run the following commands:

```sh
sudo rpm --import https://dist.sapmachine.io/rpm/sapmachine.key
sudo curl -L -o /etc/yum.repos.d/sapmachine.repo https://dist.sapmachine.io/rpm/sapmachine.repo
sudo yum install -y sapmachine-21-jdk
```

#### Using zypper

```sh
sudo zypper addrepo https://dist.sapmachine.io/rpm/sapmachine.repo; sudo zypper refresh
sudo zypper install sapmachine-21-jdk
```


### [](#linux-download) Direct download

* Download the archive and unpack it to an arbitrary location in the file system 
* Set environment variable `JAVA_HOME` to the root directory of the extracted archive (e.g. `/<...>/sapmachine-jdk-21.0.8`)
* Add `$JAVA_HOME/bin` to the environment variable `PATH` 

## [](#macOS) macOS

### SapMachine Manager

A very convenient way to install SapMachine versions and keep them up to date is to use the [SapMachine Manager](https://github.com/SAP/sapmachine-manager-for-macos). Install it from GitHub, then install the SapMachine version you need (default is the latest LTS) and SapMachine Manager will keep it up to date for you from there on. You can as well opt out from the autoupdate.

<img width="693" alt="sapmachine" src="https://github.com/SAP/SapMachine/assets/26298889/dcc3ee1c-becd-4aa3-9715-b71ef13a0cec">

### Homebrew

[Homebrew](https://brew.sh/) is another way to install SapMachine. Homebrew is a package manager for Mac. When you are familiar with it and maybe even use it already, you can manage your SapMachine installations with it as well.

At first, if you have not already done it, [install Homebrew](https://brew.sh/):  
`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

In case you did not just install it, you should update its contents:  
`brew update`

Homebrew supports the installation of the latest released SapMachine by default:  
`brew install sapmachine-jdk`

To install other versions of SapMachine you can use our tap.

Tap via:
`brew tap sap/sapmachine`

List available casks or versions of SapMachine to choose from:  
`brew search sapmachine`

Install a cask by name:  
`brew install --cask <cask>`

#### Available casks

| Version | JDK | JRE |
|--|--|--|
| SapMachine <MAJOR>  Released | `sapmachine<MAJOR>-jdk` | `sapmachine<MAJOR>-jre` |
| SapMachine <MAJOR> Early Access | `sapmachine<MAJOR>-ea-jdk` | `sapmachine<MAJOR>-ea-jre` |

Examples:

```sh
brew install --cask sapmachine17-jre
brew install --cask sapmachine21-jre
brew install --cask sapmachine25-ea-jdk
```

### Direct download

Alternatively, you can download and unpack (double-click in finder) the SapMachine archive for macOS to an arbitrary location in the file system. You may want to move the resulting directory to `/Library/Java/JavaVirtualMachines` (admin privileges required). If you do so, `/usr/libexec/java_home -V` will show SapMachine. Moreover, if SapMachine is the most recent JDK, the `java` command in the shell will use it. You can try this with `java -version`.

If you prefer not to have SapMachine integrated in macOS' Java Framework, make sure to set `JAVA_HOME` to the root directory of the extracted archive (e.g. `/<...>/sapmachine-jdk-21.0.8`) and `PATH` (i.e. `$JAVA_HOME/bin`) environment variables.

## [](#Windows) Windows

Using the Windows Installer (download the MSI package) is the simplest way to install SapMachine on Windows.

Alternatively, you can:

* Download the zip archive and unpack it to an arbitrary location in the file system
* Add the System variable `JAVA_HOME` and set it to the root directory of the extracted archive (e.g. `C:\<...>\sapmachine-jdk-21.0.8`)
* Edit the System variable `PATH` and add `%JAVA_HOME%\bin` to the `PATH`variable separated from the previous path by a semicolon.

## [](#sdkman) SDKMAN!

[SDKMAN!](https://sdkman.io/) now supports SapMachine. Because of the current length limit in the SDKMAN! version string, SapMachine has to be abbreviated as `sapmchn`. Installing with SDKMAN! is as simple as:

```sh
### install SapMachine17
sdk install java 17.0.16-sapmchn
### install SapMachine21
sdk install java 21.0.8-sapmchn
```
