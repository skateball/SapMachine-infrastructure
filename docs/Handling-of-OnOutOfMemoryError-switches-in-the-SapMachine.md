Handling of `ExitOnOutOfMemoryError`, `CrashOnOutOfMemoryError`, `OnOutOfMemoryError` and `HeapDumpOnOutOfMemoryError` in SapMachine differs from upstream OpenJDK.

Behaviorial changes to stock OpenJDK *highlighted with italics*:

- `ExitOnOutOfMemoryError`
   - *also works for thread exhaustion OOMs*
   - *also works for direct memory OOMs with system property -Djdk.nio.reportErrorOnDirectMemoryOom=true. Since 17.0.15/21.0.7*
   - *prints stack to stdout*
   - prints "Terminating due to java.lang.OutOfMemoryError" to stdout
   - Exits the VM
- `CrashOnOutOfMemoryError`
   - *also works for thread exhaustion OOMs*
   - *also works for direct memory OOMs with system property -Djdk.nio.reportErrorOnDirectMemoryOom=true. Since 17.0.15/21.0.7*
   - *prints stack to stdout*
   - Writes an error report (hs_err_pid..)
   - prints "Aborting due to java.lang.OutOfMemoryError" to stdout
   - exits the VM
   - *will **NOT** write a core file unless `+CreateCoredumpOnCrash` was explicitly specified on the command line*
- `HeapDumpOnOutOfMemoryError`
   - *also works for thread exhaustion OOMs*
   - *also works for direct memory OOMs with system property -Djdk.nio.reportErrorOnDirectMemoryOom=true. Since 17.0.15/21.0.7*
   - *prints stack to stdout*
   - generates heap dump
- `OnOutOfMemoryError=command`
   - *also works for thread exhaustion OOMs (but note that whatever resource exhaustion caused thread creation errors may cause the subsequent fork for `command` to fail as well)*
   - *prints stack to stdout*
   - invokes the given command

Notes:
- Avoiding core file creation with `CrashOnOutOfMemoryError` is intentional. `CrashOnOutOfMemoryError` is by default tuned to shut the VM down with a minimum of fuzz while still giving us a useful error report. If a core file is wanted for post analysis, specify `-XX:+CreateCoreDumpOnCrash`.
- For thread creation errors, `xxxOnOutOfMemoryError` switches are handled before the JVMTI ResourceExhausted event is posted. This means that JVMTI agents monitoring this event (e.g. CloundFoundry's `jvmkill`) may *not* get invoked. This is intentional.
- The SapMachine-specific flag `ExitVMOnOutOfMemoryError` (note the "VM" in the name, not to be confused with `ExitOnOutOfMemoryError`) is an alias to `CrashOnOutOfMemoryError` and provided for backward compatibility reasons.
