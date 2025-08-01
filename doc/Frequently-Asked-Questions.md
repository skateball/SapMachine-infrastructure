1. [What is SapMachine?](#what-is-sapmachine)
2. [What is the release roadmap and maintenance schedule of SapMachine?](#What-is-the-release-roadmap-and-maintenance-schedule-of-SapMachine)
3. [What is the process and schedule for security updates of SapMachine?](#What-is-the-process-and-schedule-for-security-updates-of-SapMachine)
4. [What platforms are supported by SapMachine?](#What-platforms-are-supported-by-SapMachine)
5. [Are SapMachine builds verified by the Java Compatibility Kit (JCK)?](#Are-SapMachine-builds-verified-by-the-Java-Compatibility-Kit-JCK)
6. [What are the differences between SapMachine and the OpenJDK?](#What-are-the-differences-between-SapMachine-and-the-OpenJDK)
7. [Can SAP contribute patches/fixes to the OpenJDK?](#Can-SAP-contribute-patchesfixes-to-the-OpenJDK)
8. [Where can I find SapMachine Debug Symbols](#Where-can-I-find-SapMachine-Debug-Symbols)
8. [Is there a fix link to download the latest stable version of SapMachine?](#Is-there-a-fix-link-to-download-the-latest-stable-version-of-SapMachine)

### What is SapMachine?
SapMachine is a build of the OpenJDK, maintained and supported by SAP. It provides a free and open-source implementation of the Java Platform, Standard Edition (Java SE).
Read this [nice article](https://web.archive.org/web/20191218204100/https://jaxenter.com/sweet-sapmachine-openjdk-155938.html) if you want to know more about the team behind SapMachine, our development processes, and how it all got started. 

### What is the release roadmap and maintenance schedule of SapMachine?
SapMachine follows the release cadence of OpenJDK's long-running [JDK Project](https://openjdk.java.net/projects/jdk/). The project ships a new feature release every six months, update releases every quarter, and a long-term support release every two years. See also SapMachine's [[Maintenance and Support]] roadmap.

### What is the process and schedule for security updates of SapMachine?
SAP is [member](https://openjdk.java.net/census#vulnerability) of the [OpenJDK Vulnerability Group](https://openjdk.java.net/groups/vulnerability/) a secure, private forum in which trusted members of the OpenJDK Community receive reports of vulnerabilities in OpenJDK code bases, review them, collaborate on fixing them, and coordinate the release of such fixes.

Security updates, also known as Critical Patch Updates (CPU), are released every quarter for all active versions of SapMachine. The release is scheduled for the Tuesday closest to the 17th day of January, April, July and October.
 
### What platforms are supported by SapMachine?
The list of the current supported platforms is available on our [[Maintenance and Support|Maintenance-and-Support]] page.

### Are SapMachine builds verified by the Java Compatibility Kit (JCK)?
Yes, long-term support releases of SapMachine are all JCK verified. For short-term releases at least one platform, usually Linux x86 (64bit), is JCK verified. Further information about the process and a complete list of JCK-verified releases can be found on page [[Certification and Java Compatibility]].

### What are the differences between SapMachine and the OpenJDK?
All known differences are detailed in this [[article|Differences between SapMachine and OpenJDK]].

### Can SAP contribute patches/fixes to the OpenJDK?
Yes. The SapMachine team is actively contributing to the OpenJDK. Team individuals are holding different project and group related roles, such as Project Lead, Reviewer or Committer. We contribute new features, but also provide bug fixes and are maintainers of the JDK updates projects. 

### Where can I find SapMachine Debug Symbols? 
SapMachine debug symbols are available as a separate download archive in the release section (e.g. for `SapMachine 21.0.6` on Linux-x64 the correct archive would be [sapmachine-jdk-21.0.6_linux-x64_bin-symbols.tar.gz](https://github.com/SAP/SapMachine/releases/download/sapmachine-21.0.6/sapmachine-jdk-21.0.6_linux-x64_bin-symbols.tar.gz)).
Download the archive matching your architecture, extract it and copy the contents of the `bin` and `lib` folder to the same directory in the root directory of your SapMachine installation. 

### Is there a fix link to download the latest stable version of SapMachine?
Yes, you can access it with https://sapmachine.io/latest/<jdk-number\>/\<os-name\>-\<cpu-arch\>/[jdk|jre] , for example for SapMachine 21 https://sapmachine.io/latest/21/macos-x64/jdk or https://sapmachine.io/latest/21/linux-x64/jre.

| OS | 17 LTS | 21 LTS | 24 |
| -- |:------:|:------:|:--:|
| AIX |  | [JRE](https://sapmachine.io/latest/21/aix-ppc64/jre) / [JDK](https://sapmachine.io/latest/21/aix-ppc64/jdk) | [JRE](https://sapmachine.io/latest/24/aix-ppc64/jre) / [JDK](https://sapmachine.io/latest/24/aix-ppc64/jdk) |
| Linux aarch64 | [JRE](https://sapmachine.io/latest/17/linux-aarch64/jre) / [JDK](https://sapmachine.io/latest/17/linux-aarch64/jdk) | [JRE](https://sapmachine.io/latest/21/linux-aarch64/jre) / [JDK](https://sapmachine.io/latest/21/linux-aarch64/jdk) | [JRE](https://sapmachine.io/latest/24/linux-aarch64/jre) / [JDK](https://sapmachine.io/latest/24/linux-aarch64/jdk) |
| Linux ppc64le | [JRE](https://sapmachine.io/latest/17/linux-ppc64le/jre) / [JDK](https://sapmachine.io/latest/17/linux-ppc64le/jdk) | [JRE](https://sapmachine.io/latest/21/linux-ppc64le/jre) / [JDK](https://sapmachine.io/latest/21/linux-ppc64le/jdk) | [JRE](https://sapmachine.io/latest/24/linux-ppc64le/jre) / [JDK](https://sapmachine.io/latest/24/linux-ppc64le/jdk) |
| Linux x64 (glibc) | [JRE](https://sapmachine.io/latest/17/linux-x64/jre) / [JDK](https://sapmachine.io/latest/17/linux-x64/jdk) | [JRE](https://sapmachine.io/latest/21/linux-x64/jre) / [JDK](https://sapmachine.io/latest/21/linux-x64/jdk) | [JRE](https://sapmachine.io/latest/24/linux-x64/jre) / [JDK](https://sapmachine.io/latest/24/linux-x64/jdk) |
| Linux x64 (musl/alpine) | [JRE](https://sapmachine.io/latest/17/linux-x64-musl/jre) / [JDK](https://sapmachine.io/latest/17/linux-x64-musl/jdk) | [JRE](https://sapmachine.io/latest/21/linux-x64-musl/jre) / [JDK](https://sapmachine.io/latest/21/linux-x64-musl/jdk) |  [JRE](https://sapmachine.io/latest/24/linux-x64-musl/jre) / [JDK](https://sapmachine.io/latest/24/linux-x64-musl/jdk) |
| MacOS aarch64 | [JRE](https://sapmachine.io/latest/17/macos-aarch64/jre) / [JDK](https://sapmachine.io/latest/17/macos-aarch64/jdk) | [JRE](https://sapmachine.io/latest/21/macos-aarch64/jre) / [JDK](https://sapmachine.io/latest/21/macos-aarch64/jdk) |  [JRE](https://sapmachine.io/latest/24/macos-aarch64/jre) / [JDK](https://sapmachine.io/latest/24/macos-aarch64/jdk) |
| MacOS aarch64 Installer | [JRE](https://sapmachine.io/latest/17/macos-aarch64-installer/jre) / [JDK](https://sapmachine.io/latest/17/macos-aarch64-installer/jdk) | [JRE](https://sapmachine.io/latest/21/macos-aarch64-installer/jre) / [JDK](https://sapmachine.io/latest/21/macos-aarch64-installer/jdk) | [JRE](https://sapmachine.io/latest/24/macos-aarch64-installer/jre) / [JDK](https://sapmachine.io/latest/24/macos-aarch64-installer/jdk) |
| MacOS x64 | [JRE](https://sapmachine.io/latest/17/macos-x64/jre) / [JDK](https://sapmachine.io/latest/17/macos-x64/jdk) | [JRE](https://sapmachine.io/latest/21/macos-x64/jre) / [JDK](https://sapmachine.io/latest/21/macos-x64/jdk) | [JRE](https://sapmachine.io/latest/24/macos-x64/jre) / [JDK](https://sapmachine.io/latest/24/macos-x64/jdk) |
| MacOS x64 Installer | [JRE](https://sapmachine.io/latest/17/macos-x64-installer/jre) / [JDK](https://sapmachine.io/latest/17/macos-x64-installer/jdk) | [JRE](https://sapmachine.io/latest/21/macos-x64-installer/jre) / [JDK](https://sapmachine.io/latest/21/macos-x64-installer/jdk) | [JRE](https://sapmachine.io/latest/24/macos-x64-installer/jre) / [JDK](https://sapmachine.io/latest/24/macos-x64-installer/jdk) |
| Windows x64 | [JRE](https://sapmachine.io/latest/17/windows-x64/jre) / [JDK](https://sapmachine.io/latest/17/windows-x64/jdk) | [JRE](https://sapmachine.io/latest/21/windows-x64/jre) / [JDK](https://sapmachine.io/latest/21/windows-x64/jdk) | [JRE](https://sapmachine.io/latest/24/windows-x64/jre) / [JDK](https://sapmachine.io/latest/24/windows-x64/jdk) |
| Windows x64 Installer | [JRE](https://sapmachine.io/latest/17/windows-x64-installer/jre) / [JDK](https://sapmachine.io/latest/17/windows-x64-installer/jdk) | [JRE](https://sapmachine.io/latest/21/windows-x64-installer/jre) / [JDK](https://sapmachine.io/latest/21/windows-x64-installer/jdk) | [JRE](https://sapmachine.io/latest/24/windows-x64-installer/jre) / [JDK](https://sapmachine.io/latest/24/windows-x64-installer/jdk) |


