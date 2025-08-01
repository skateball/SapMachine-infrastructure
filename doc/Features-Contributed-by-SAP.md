**This page is currently unmaintained.**


This page lists features of SapMachine that were crafted by SAP to enhance the enterprise-readiness of SapMachine. In general, we contribute these directly upstream to OpenJDK. We might downport these to an earlier version of SapMachine, though. If a feature is not accepted by the OpenJDK community, but considered essential by us, it might only appear in SapMachine. This listing omits bug fixes, work on our platform ports, work on the build and test infrastructure etc. we do directly in OpenJDK. 

# Functional Improvements

## Memory Management

### Metaspace
The Metaspace memory region contains metadata for loaded Java classes. It may cause an abnormally high memory footprint when using many class loaders, lots of class unloading, reflection, or lambdas.
 
SAP improved the Metaspace allocator significantly over the years, reducing its memory footprint, making it more predictable and easier to monitor. The work culminated in a complete rewrite of the Metaspace with JDK 16. This work went under the flag of [JEP 387 "Elastic Metaspace"](https://openjdk.java.net/jeps/387).

Individual patches are too numerous to count, but two significant milestones stick out:

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8198423: Improve metaspace chunk allocation](https://bugs.openjdk.java.net/browse/JDK-8198423) | **11** | **11** |
| [8251158: Implementation of JEP 387: Elastic Metaspace](https://bugs.openjdk.java.net/browse/JDK-8251158) | **16** | **16** |

Publications:
- [JEP 387 “Elastic Metaspace”](https://blogs.sap.com/2021/07/16/jep-387-elastic-metaspace-a-new-classroom-for-the-java-virtual-machine/)
- [Ein neues Klassenzimmer (Java Magazin 7/21, German)](https://entwickler.de/java/ein-neues-klassenzimmer)
### Java in Containers

Applications run in Containers or the Cloud need to be optimized for small footprint.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8198510: Enable UseDynamicNumberOfGCThreads by default](https://bugs.openjdk.java.net/browse/JDK-8198510) <br/> We saw the VM starting too many GC threads. | **11** | **11** |
| [8198756: Lazy allocation of compiler threads](https://bugs.openjdk.java.net/browse/JDK-8198756)  <br/> We saw the VM starting too many compiler threads.| **11** | **11** |
| [ 8213086: Compiler thread creation should be bounded by available space in memory and Code Cache](https://bugs.openjdk.java.net/browse/JDK-8213086)  <br/> We saw the VM starting too many compiler threads.| **11.0.3, 12** | **11.0.2, 12** |
| [8196062: Enable docker container related tests for linux ppc64le](https://bugs.openjdk.java.net/browse/JDK-8196062) <br/> This also needed some functional improvements. | **11** | **11** |
| [8197412: Enable docker container related tests for linux s390x](https://bugs.openjdk.java.net/browse/JDK-8197412) | **11** | **11** |
| [8220787: Create new switch to redirect error reporting output to stdout or stderr](https://bugs.openjdk.java.net/browse/JDK-8220787) | **11.0.7, 13** | **11.0.7, 13** |


### Files and Network



|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8170868: DefaultProxySelector should use system defaults on Windows, MacOS and Gnome](https://bugs.openjdk.java.net/browse/JDK-8170868) | **9** | **9** |
| [8213082: (zipfs) Add support for POSIX file permissions](https://bugs.openjdk.java.net/browse/JDK-8213082) | **14** | **11.0.2** |
| [8191521: handle long relative path specified in -Xbootclasspath/a on windows](https://bugs.openjdk.java.net/browse/JDK-8191521) | **11.0.6, 14** | **11.0.6, 14** |


### Threads and Stack sizes

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8215962: Support ThreadPriorityPolicy mode 1 for non-root users on linux/bsd](https://bugs.openjdk.java.net/browse/JDK-8215962) |  **11.0.3**, **13** | **11.0.2** |

Configuring stack sizes used to depend strongly on the system page size and was optimized for 4K pages. We made stack configuration less dependent on the page size wrt. overflow detection and minimal stack sizes.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8170655: [posix] Fix minimum stack size computations](https://bugs.openjdk.java.net/browse/JDK-8170655) | **10** | **10** |
| [8139864: Improve handling of stack protection zones.](https://bugs.openjdk.java.net/browse/JDK-8139864) | **10** | **10** |

## Exception messages

Many exceptions thrown in OpenJDK 10 and earlier don't give detailed information about the underlying problem, although it's known when the exception is thrown. We improve these messages step by step.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8197405: Improve messages of AbstractMethodErrors and IncompatibleClassChangeErrors.](https://bugs.openjdk.java.net/browse/JDK-8197405) | **11** | **10** |
| [8204268: Improve some IncompatibleClassChangeError messages.](https://bugs.openjdk.java.net/browse/JDK-8204268) | **11** | **11** |
| [8199852: Print more information about class loaders in LinkageErrors.](https://bugs.openjdk.java.net/browse/JDK-8199852) | **11** | **11** |
| [8201593: Print array length in ArrayIndexOutOfBoundsException.](https://bugs.openjdk.java.net/browse/JDK-8201593),  [8217628](https://bugs.openjdk.java.net/browse/JDK-8217628) | **11** | **11** |
| [8203881: Print erroneous size in NegativeArraySizeException](https://bugs.openjdk.java.net/browse/JDK-8203881) | **11** | **11** |
| [8199940: Print more information about class loaders in IllegalAccessErrors](https://bugs.openjdk.java.net/browse/JDK-8199940) | **11** | **11** |
| [8204943: Improve message of ArrayStoreException.](https://bugs.openjdk.java.net/browse/JDK-8204943) | **11** | **11** |
| [8205525: Improve exception messages during manifest parsing of jar archives.](https://bugs.openjdk.java.net/browse/JDK-8205525) | **12** | **12** |
| [JEP 358: Helpful NullPointerExceptions](https://openjdk.java.net/jeps/358) This feature is off per default in OpenJDK 14. In SapMachine, it is on. See also [8233014: Enable ShowCodeDetailsInExceptionMessages per default.](https://bugs.openjdk.java.net/browse/JDK-8233014) | 14 | **11.0.6**, **13.0.2** |
| java.util.zip: [8239351: Give more meaningful InternalError messages in Deflater.c](https://bugs.openjdk.java.net/browse/JDK-8239351) | **11.0.8, 15** | **11.0.8, 15** |
| [] () | **11.0., 15** | **11.0., 15** |


## Size of Image, Installation and Download

In Cloud Environments the size of the JVM package, of it's Installation and of the running image matter. We do improvements to reduce these sizes. 

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8234525: Enable link-time section-gc for linux s390x to remove unused code](https://bugs.openjdk.java.net/browse/JDK-8234525) | **11.0.7, 14** | **11.0.7, 14** |
| [8233078 fix minimal VM build on Linux ppc64(le)](https://bugs.openjdk.java.net/browse/JDK-8233078) [8233328 fix minimal VM build on Linux s390x](https://bugs.openjdk.java.net/browse/JDK-8233328) The minimal VM is a build-time variant of the JVM native library. It excludes a row of algorithms. It can be used in apps that execute very few Java code over time and need to be very small. | **11.0.7, 14** | **11.0.7, 14** |
| [8237192 Generate stripped/public pdbs on Windows for jdk images](https://bugs.openjdk.java.net/browse/JDK-8237192) This reduces the size of files containing debug Information while assuring stacks are properly printed. | **11.0.8, 15** | **11.0.8, 15** |
| Remove unused code [8238602](https://bugs.openjdk.java.net/browse/JDK-8238602) [8237819](https://bugs.openjdk.java.net/browse/JDK-8237819) | **11.0.7ff, 15** | **11.0.7ff, 15** |


# Servicability Extensions

## Debugging on Demand 

SAP JVM was known for its debugging on demand. This means you could attach at any time to an application running on SAP JVM and start debugging it. We want to enhance OpenJDK with similar features.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8214892: Delayed starting of debugging via jcmd](https://bugs.openjdk.java.net/browse/JDK-8214892) | **11.0.3** | **11.0.2** |
| These changes improve the VM performance if debugging is enabled: | |
| [8214352: C1: Unnecessary "compilation bailout: block join failed" with JVMTI](https://bugs.openjdk.java.net/browse/JDK-8214352) | **11.0.3**, **13** | **11.0.2** |
| [8216556: Unnecessary liveness computation with JVMTI](https://bugs.openjdk.java.net/browse/JDK-8216556) | **11.0.4, 13** | **11.0.4, 13** |
| [8227680: FastJNIAccessors: Check for JVMTI field access event requests at runtime](https://bugs.openjdk.java.net/browse/JDK-8227680) | **14** | **14** |


## Jcmd improvements

Jcmd allows to request information from a running Java VM. SAP JVM knows similar tools. We add the commands known in the SAP JVM tools to Jcmd.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8189864: Provide an ascii map to visualize metaspace fragmentation](https://bugs.openjdk.java.net/browse/JDK-8189864) | **10** | **10** |
| [8198691: CodeHeap State Analytics](https://bugs.openjdk.java.net/browse/JDK-8198691) <br> Print information about the memory containing Java methods compiled to native code. | **11** | **11** |
| [8198553: jcmd: separate Metaspace statistics from NMT](https://bugs.openjdk.java.net/browse/JDK-8198553)  <br> Introduces new command VM.metaspace. | **11** | **11** |
| [8201572: Improve Metaspace Statistics](https://bugs.openjdk.java.net/browse/JDK-8201572) | **11** | **11** |
| [8203219: VM.metaspace jcmd should optionally show loaded classes for loaders](https://bugs.openjdk.java.net/browse/JDK-8203219) | **11** | **11** |
| [8203455: jcmd: VM.metaspace: print loader name for anonymous CLDs](https://bugs.openjdk.java.net/browse/JDK-8203455) | **11** | **11** |
| [8203682: Add jcmd "VM.classloaders" command to print out class loader hierarchy, details](https://bugs.openjdk.java.net/browse/JDK-8203682) | **11** | **11** |
| [8200720: Print additional information in thread dump (times, allocated bytes etc.)](https://bugs.openjdk.java.net/browse/JDK-8200720) | **11** | **11** |
| [8203682: Add jcmd "VM.classloaders" command to print out class loader hierarchy, details](https://bugs.openjdk.java.net/browse/JDK-8203682) | **11** | **11** |
| [8203343: VM.{metaspace\|classloaders\|classhierarchy...} jcmd should show invocation targets for Generated{Method\|Constructor}AccessorImpl classes](https://bugs.openjdk.java.net/browse/JDK-8203343) | **11** | **11** |
| [8224601: Provide VM.events command](https://bugs.openjdk.java.net/browse/JDK-8224601) to view the Events Log.| **13** | **13** |
| [8233790: Forward output from heap dumper to jcmd/jmap](https://bugs.openjdk.java.net/browse/JDK-8233790) | **14** | **14** |
| [8234510: Remove file seeking requirement for writing a heap dump](https://bugs.openjdk.java.net/browse/JDK-8234510) | **15** | **15** |


## Java Flight Recorder (JFR)

We will improve Java Flight Recorder and Mission Control as a replacement of SAP JVM Profiler.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8207392: [PPC64] Implement JFR profiling.](https://bugs.openjdk.java.net/browse/JDK-8207392) | **11** | **11** |
| [8211768: [s390] Implement JFR profiling.](https://bugs.openjdk.java.net/browse/JDK-8211768) | **11.0.2, 12** | **11.0.2, 12** |
| [8223438: add VirtualizationInformation JFR event](https://bugs.openjdk.java.net/browse/JDK-8223438) | **11.0.6, 13** | **11.0.6, 13** |
| [8224230: [PPC64, s390] Support AsyncGetCallTrace](https://bugs.openjdk.java.net/browse/JDK-8224230) needed for external profiling tools as [async](https://github.com/jvm-profiling-tools/async-profiler). | **11.0.5, 13** | **11.0.5, 13** |

## A History of vitals as memory and heap usage

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8212618: A low-cost, always on statistical value history](https://bugs.openjdk.java.net/browse/JDK-8212618) The information is viewable with jcmd and printed to the hs_err file. | not accepted | **11.0.3, 12** |


## Add more information to Event Log. 

The OpenJDK JVM has internal event logs. Events happening in the VM that might be relevant for 
error analysis are written to these logs that store the #n last entries. The event logs 
can be viewed by jcmd and are printed to the hs_err file.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8224221: add memprotect calls to event log](https://bugs.openjdk.java.net/browse/JDK-8224221) | **11.0.5, 13** | **11.0.5, 13** |
| [8224958: add os::dll_load calls to event log](https://bugs.openjdk.java.net/browse/JDK-8224958) | **11.0.6, 13** | **11.0.6, 13** |

## Retaining information in case of a crash / hs_err file

If OpenJdk crashes, it writes a collection of basic information into a file named hs-err_\<process id\>.log.
This information is very useful to analyze the crash post-mortem. We enrich this printout with information we found useful for SAP JVM support.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8191101: Show register content in hs-err file on assert](https://bugs.openjdk.java.net/browse/JDK-8191101) | **11** | **11** |
| [8203292: Print complete set of flags in the hs_err file](https://bugs.openjdk.java.net/browse/JDK-8203292) | **11** | **11** |
| [8202427: Enhance os::print_memory_info on Windows](https://bugs.openjdk.java.net/browse/JDK-8202427) | **11** | **11** |
| [8204476: Add additional statistics to CodeCache::print_summary](https://bugs.openjdk.java.net/browse/JDK-8204476) | **11** | **11** |
| [8204477: Count linkage errors and print in Exceptions::print_exception_counts_on_error ](https://bugs.openjdk.java.net/browse/JDK-8204477) | **11** | **11** |
| [8204598: Add more thread-related system settings info to hs_error file on Linux](https://bugs.openjdk.java.net/browse/JDK-8204598) | **11** | **11** |
| [8210964: Add more ld preloading info to hs_error file on Linux](https://bugs.openjdk.java.net/browse/JDK-8210964) | **11.0.2** | **11.0.2** |
| [8211852: Inspect stack during error reporting](https://bugs.openjdk.java.net/browse/JDK-8211852) Besides this functional improvement, we contributed [8210754](https://bugs.openjdk.java.net/browse/JDK-8210754) to make printing register content more reliable.  | **11.0.2** | **11.0.2** |
| [8219241: Provide basic virtualization related info in the hs_error file on linux/windows x86_64](https://bugs.openjdk.java.net/browse/JDK-8219241) | **11.0.5, 13** | **11.0.5, 13** |
| [8222720: Provide extended VMWare/vSphere virtualization related info in the hs_error file on linux/windows x86_64: ](https://bugs.openjdk.java.net/browse/JDK-8222720) | **11.0.5, 13** | **11.0.5, 13** |
| [8219746: Provide virtualization related info in the hs_error file on linux ppc64 / ppc64le](https://bugs.openjdk.java.net/browse/JDK-8219746) | **11.0.4, 13** | **11.0.4, 13** |
| [8217786: Provide virtualization related info in the hs_error file on linux s390x](https://bugs.openjdk.java.net/browse/JDK-8217786) | **11.0.4, 13** | **11.0.4, 13** |
| [8222280: Provide virtualization related info in the hs_error file on AIX](https://bugs.openjdk.java.net/browse/JDK-822280) | **11.0.5, 13** | **11.0.5, 13** |
| [8225345: Provide Cloud IAAS related info on Linux in the hs_err file](https://bugs.openjdk.java.net/browse/JDK-8225345) | not accepted | **11.0.4, 12.0.2** |
| [8219584: Try to dump error file by thread which causes safepoint timeout](https://bugs.openjdk.java.net/browse/JDK-8219584) (Off by default) | **11.0.4, 13** | **11.0.4, 13** |
| [8221535: Add steal tick related information to hs_error file [linux]](https://bugs.openjdk.java.net/browse/JDK-8221535) | **11.0.4, 13** | **11.0.4, 13** |
| [8223574: add more thread-related system settings info to hs_error file on AIX](https://bugs.openjdk.java.net/browse/JDK-8223574) | **11.0.5, 13** | **11.0.5, 13** |
| [8221325: Add information about swap space to print_memory_info() on MacOS](https://bugs.openjdk.java.net/browse/JDK-8221325) | **11.0.5, 13** | **11.0.5, 13** |
| [8234397: Add OS uptime information to os::print_os_info output](https://bugs.openjdk.java.net/browse/JDK-8234397) | **11.0.7, 14** | **11.0.7, 14** |
| [8234741: Enhance os::get_core_path on macOS](https://bugs.openjdk.java.net/browse/JDK-8234741) Print the path to the core properly. | **11.0.7, 14** | **11.0.7, 14** |
| [8227031: Print NMT statistics on fatal errors](https://bugs.openjdk.java.net/browse/JDK-8227031) | **11.0.6, 14** | **11.0.6, 14** |




## Other

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8204539: improve error messages in matchJavaTZ [windows]](https://bugs.openjdk.java.net/browse/JDK-8204539) | **11** | **11** |
| [8220570: Additonal trace when native thread creation fails](https://bugs.openjdk.java.net/browse/JDK-8220570) | **11.0.5, 13** | **11.0.5, 13** |
| [8226238: Improve error output and fix elf issues in os::dll_load](https://bugs.openjdk.java.net/browse/JDK-8226238) | **14** | **14** |
| [8227441 Enhance logging when reading the fontconfig info file](https://bugs.openjdk.java.net/browse/JDK-8227441) | **14** | **14** |
| [8237962: Give better error output for invalid OCSP response intervals in CertPathValidator check](https://bugs.openjdk.java.net/browse/JDK-8237962) | **11.0.8, 15** | **11.0.8, 15** |



## Documentation

We improve the documentation, be it Javadoc, the tools etc.

|    | OpenJDK | SapMachine |
| --- | --- | --- |
| [8200384: jcmd help output should be sorted](https://bugs.openjdk.java.net/browse/JDK-8200384) | **11** | **11** |
| [8189102: All tools should support -?, -h and --help](https://bugs.openjdk.java.net/browse/JDK-8189102) | **11** | **11** |
| [8203014: jcmd should output command list if no command is given](https://bugs.openjdk.java.net/browse/JDK-8203014) | **11** | **11** |

