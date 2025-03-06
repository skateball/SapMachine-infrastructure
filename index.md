---
layout: default
title: SapMachine
---

**SapMachine** is a distribution of the [OpenJDK (external Link)](https://openjdk.org/) maintained by <a href="https://sap.com">SAP (external Link)</a>. It is designed to be free, cross-platform, production-ready, and [Java SE certified](https://github.com/SAP/SapMachine/wiki/Certification-and-Java-Compatibility). This distribution serves as the default Java Runtime for SAP's numerous applications and services.

<p align="left"><img width="240" src="assets/images/logo_circular.svg" alt="The SapMachine Logo image, a OpenJDK-distribution from SAP"></p>

SapMachine supports all major operating systems.
It comes with long-term support releases that include bug fixes and performance updates; you can learn more about support and maintenance in our [Wiki](https://github.com/SAP/SapMachine/wiki/Maintenance-and-Support).

Our goal is to keep SapMachine as close to OpenJDK as possible,
only adding additional features when absolutely necessary; you can find a list of these in the [Wiki](https://github.com/SAP/SapMachine/wiki/Differences-between-SapMachine-and-OpenJDK).

Our team's many contributions to the OpenJDK and the ecosystem include the [PowerPC/AIX support](http://openjdk.java.net/projects/ppc-aix-port/), [elastic Metaspace](https://openjdk.org/jeps/387),
 [helpful NullPointerExceptions](https://openjdk.org/jeps/358), a [website for JFR events](https://sap.github.io/SapMachine/jfrevents/) and more.

## Download

In the following, you find downloads of SapMachine and our build of [JDK Mission Control (JMC)](https://openjdk.org/projects/jmc/):

<select id="sapmachine_major_select" class="download_select" aria-label="Select the major version of the SapMachine you want to download"></select>

<select id="sapmachine_imagetype_select" class="download_select" aria-label="Select either JDK or JRE of SapMachine you want to download"></select>

<select id="sapmachine_os_select" class="download_select" aria-label="Select the target Operating System of the SapMachine you want to download"></select>

<select id="sapmachine_version_select" class="download_select" aria-label="Select the version of SapMachine you want to download"></select>

<button id="sapmachine_download_button" type="button" class="download_button" aria-label="Download SapMachine in the configured release, type, OS and version">Download configured SapMachine release</button>

<div class="download_label_section">
  <div id="download_label" class="download_label"></div>
  <button id="sapmachine_copy_button" type="button" class="download_button" aria-label="Copy the download URL of the SapMachine release configured by release, type, OS and version">Copy Download URL of configured SapMachine release</button>
</div>

<div class="download_filter">
  <input type="checkbox" id="sapmachine_lts_checkbox" name="lts" aria-label="If checked, Long Term Support Releases (LTS) of SapMachine will offered in the list for download (default)" checked>
  <label for="lts">Long Term Support Releases (LTS)</label>

  <input type="checkbox" id="sapmachine_nonlts_checkbox" name="nonlts" aria-label="If checked, Short Term Support Releases of SapMachine will be offered in the list for download (default)" checked>
  <label for="nonlts">Short Term Support Releases</label>

  <input type="checkbox" id="sapmachine_ea_checkbox" name="ea" aria-label="If checked, Pre-Releases of SapMachine will be offered in the list for download">
  <label for="ea">Pre-Releases</label>
</div>

## Documentation

[Check out our Frequently Asked Questions (FAQ)](https://github.com/SAP/SapMachine/wiki/Frequently-Asked-Questions) and [SapMachine Documentation](https://github.com/SAP/SapMachine/wiki) for more information about:

* [Installation Manual](https://github.com/SAP/SapMachine/wiki/Installation), [List of available Container Images on Docker Hub](https://github.com/SAP/SapMachine/wiki/Docker-Images),  [List of available Container Images on Github](https://github.com/orgs/SAP/packages/container/sapmachine/versions)
* [Maintenance and Support Statement](https://github.com/SAP/SapMachine/wiki/Maintenance-and-Support)
* [Certifications and Java Compatibility document](https://github.com/SAP/SapMachine/wiki/Certification-and-Java-Compatibility)
* [List of Differences between SapMachine and OpenJDK](https://github.com/SAP/SapMachine/wiki/Differences-between-SapMachine-and-OpenJDK)
