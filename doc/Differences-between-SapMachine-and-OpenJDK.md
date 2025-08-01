# Differences between SapMachine and OpenJDK

It is the goal of the SapMachine team to keep SapMachine as close to OpenJDK as possible. Therefore features identified as required by SAP applications should be developed _in_ and contributed _to_ OpenJDK. Only if this is, for what ever reason, not possible, differences between SapMachine and OpenJDK are considered acceptable. However, they have to be kept as small as possible.

Features not accepted via the OpenJDK reviewing process may still find their way into OpenJDK code when switched off by default. It is generally considered acceptable to switch on such features by default in SapMachine.

Features which require functional changes in the code may still be acceptable. However, this will have to be decided for each particular case.

## Additionally Included Software

We started including [async-profiler](https://github.com/jvm-profiling-tools/async-profiler) in our distribution.

## Version numbers

You can easily identify SapMachine from the output of the `java -version` command (see below). Although the version information of SapMachine and OpenJDK/OracleJDK are slightly different, the SapMachine version output still fully conforms to the format specified in the [JEP 322: Time-Based Release Versioning](http://openjdk.java.net/jeps/322) and [JEP 223: New Version-String Scheme](http://openjdk.java.net/jeps/223).

### SapMachine version information

```shell
$ ./sapmachine-11/bin/java -version
openjdk version "11.0.2" 2019-01-16 LTS
OpenJDK Runtime Environment (build 11.0.2+0-LTS-sapmachine)
OpenJDK 64-Bit Server VM (build 11.0.2+0-LTS-sapmachine, mixed mode)
```

In addition to the original OpenJDK version output (see below), SapMachine adds an optional part (i.e. `LTS-sapmachine`) to the version number. This optional part (defined as [optional build information](http://openjdk.java.net/jeps/322#Version-strings) in JEP 322) starts with `LTS` for long term support releases followed by the name `sapmachine`. If we will do an additional SapMachine specific release for this version, the fifth element of the
version number will be increased and looks as follows `11.0.2.0.1+0-LTS-sapmachine`. Once we pull and merge the next upstream release, this number will be reset to zero (e.g. `11.0.3+0-LTS-sapmachine`). We are currently not using the build number part of the version string and always set it to `0`.

The version date, as defined in JEP 322, will be set to the date, the SapMachine is generally available (GA).
This date is never before the OpenJDK GA but may be set to a date after the OpenJDK GA.

### OpenJDK version information

```shell
$ ./jdk-11-openjdk/bin/java -version
openjdk version "11.0.2" 2019-01-15
OpenJDK Runtime Environment 18.9 (build 11.0.2+9)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.2+9, mixed mode)
```

## System properties

The following listing shows the differences in the Java system properties between SapMachine and OpenJDK. Besides the version differences already discussed above that's mostly the different values for the various `vendor` properties:

```diff
-    java.runtime.version = 11.0.2+9
+    java.runtime.version = 11.0.2+0-LTS-sapmachine
-    java.vendor = Oracle Corporation
-    java.vendor.url = http://java.oracle.com/
-    java.vendor.url.bug = http://bugreport.java.com/bugreport/
-    java.vendor.version = 18.9
+    java.vendor = SAP SE
+    java.vendor.url = https://sapmachine.io
+    java.vendor.url.bug = https://github.com/SAP/SapMachine/issues/new
-    java.version.date = 2019-01-15
+    java.version.date = 2019-01-16
-    java.vm.vendor = Oracle Corporation
-    java.vm.version = 11.0.2+9
+    java.vm.vendor = SAP SE
+    java.vm.version = 11.0.2+0-LTS-sapmachine
```

## Other behavioral differences

* Extended thread dumps [`-XX:+PrintExtendedThreadInfo`](https://bugs.openjdk.java.net/browse/JDK-8205604) are enabled in SapMachine. See also [8200720](https://bugs.openjdk.java.net/browse/JDK-8200720).

* SapMachine enables output of additional information in exception messages by setting jdk.includeInExceptions in the [java security configuration file](http://hg.openjdk.java.net/jdk/jdk/file/1ddf9a99e4ad/src/java.base/share/conf/security/java.security). SapMachine 11 sets this property to ['hostinfo'](https://github.com/SAP/SapMachine/blob/sapmachine11/src/java.base/share/conf/security/java.security), SapMachine 12 and later set ['hostinfo,jar'](https://github.com/SAP/SapMachine/blob/sapmachine/src/java.base/share/conf/security/java.security). See also [8204622](https://bugs.openjdk.java.net/browse/JDK-8204622) and [8207768](https://bugs.openjdk.java.net/browse/JDK-8207768).

* SapMachine enables output of code snippets in exception messages: [8233014: Enable ShowCodeDetailsInExceptionMessages per default.](https://bugs.openjdk.java.net/browse/JDK-8233014). Since 11.0.6 / 13.0.2

* SapMachine enables [-XX:+ExtensiveErrorReports](https://bugs.openjdk.java.net/browse/JDK-8211846). Since 11.0.3 / 12.

* Added root certificate "SAP Global Root CA" used by the SAP Global PKI infrastructure [http://www.pki.co.sap.com/](http://www.pki.co.sap.com/).

* SapMachine has Vitals: [8212618: A low-cost, always on statistical value history](https://bugs.openjdk.java.net/browse/JDK-8212618). Since 11.0.3 / 12.

* SapMachine handles `xxxOnOutOfMemoryError` switches differently than stock OpenJDK to be more useful in cloud scenarios. For details, see [Handling of OnOutOfMemoryError switches in the SapMachine](https://github.com/SAP/SapMachine/wiki/Handling-of-OnOutOfMemoryError-switches-in-the-SapMachine). Since 11.0.12 / 16.0.2.

* SapMachine prints all flags in hs_err files, not just the default ones. Comments are omitted, though. Since 11.0.13 / 17.0.1.

* SapMachine has two additional JFR configurations, especially for GC profiling(gc.jfc and gc_details.jfc). Since 11.0.19 / 17.0.7.
