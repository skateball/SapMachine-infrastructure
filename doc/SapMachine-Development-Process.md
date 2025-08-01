# Repository and Branches

## jdk/jdk and jdk/jdk\<version\>
All changes in the mercurial repositories [jdk/jdk](http://hg.openjdk.java.net/jdk/jdk/) and [jdk/jdk\<version\>]( http://hg.openjdk.java.net/jdk/jdk10/) are imported using the tool [git-hg-again](https://github.com/abourget/git-hg-again).
The branches jdk/jdk and jdk/jdk\<version\> are mirrors of the mercurial repositories. We do not add changes in these branches. If a jdk version is in maintenance mode, we also import jdk-updates/jdk\<version\>u into a branch of it's own. The import to the branches is discontinued if maintenance of OpenJDK for this release ends. 

Starting with jdk12, there will be active branches for several java versions. For jdk/jdk, the latest jdk version 
in development (e.g. jdk/jdk14), the latest released jdk version (jdk-updates/jdk13u) and the "long term supported" java versions (jdk-updates/jdk11u).

## sapmachine and sapmachine\<version\>
We build and deliver the  branches sapmachine and sapmachine\<version\>. We merge the OpenJDK mirror branches into these branches on a regular basis. We make changes to these branches to add features and bug fixes that won't make it into OpenJDK, as quick as we need them. If a Java version is in maintenance mode, the jdk-updates/jdk\<version\>u branch is merged into sapmachine\<version\>.

### Merging of mirror branches
For new build tags (e.g jdk-10+42) in the mirror branches, our CI creates Pull Requests (PR) to merge the corresponding branch to that tag. The PR automatically triggers test builds on our CI system. In order to merge the PR, a contributor of the SapMachine repository has to review the build and test results and have a look at the changes for plausibility. Additionally, possible merge conflicts have to be resolved. After merging the PR, the CI system creates a corresponding sapmachine tag (e.g. sapmachine-10+42-0) and starts the builds for the new tags.
If we urgently need changes from a jdk branch, before there is a new build tag, we manually create a PR. A test run of the PR will automatically start in this case. 

Other changes to sapmachine and sapmachine\<version\> should be done by opening a PR.

For each new tag on the sapmachine branches, we build and test binaries and publish them as new (pre-) releases in the GitHub repository.

### Tests

* Snapshot build and test: We build the head of sapmachine and sapmachine\<version\> branches and run gtests and jtreg tests. The gtests are run as part of the build job. Afterwards, the Jtreg tests for the *hotspot*, *jdk* and *langtools* test suites are run in separate jobs.

* Release build and test: sapmachine and sapmachine\<version\> branches are scanned for new tags. With each new tag, a release build and the corresponding jtreg tests are started. Again the three test suites *hotspot*, *jdk* and *langtools* will be started in separate jobs. The build result is published as GitHub release. Additionally, new Debian packages are build and deployed and docker images are build and published via https://hub.docker.com/u/sapmachine/.



# Scope of SapMachine changes

Our guiding development principle is to bring missing features directly into the OpenJDK if that's possible. Currently our major focus is on improving the serviceability of OpenJDK/SapMachine.

As our customers will use the LTS releases of SapMachine (currently SapMachine 11) for a long time, we're especially interested to improve the serviceability of these releases. Therefore, it might be necessary to manually down-port such features into the SapMachine LTS version if they do not get accepted in the corresponding upstream OpenJDK update project. We may also down-port additional bug fixes (compared to the corresponding up-stream OpenJDK project) into the SapMachine LTS versions if they won't be approved for inclusion in the up-stream updates project but are nevertheless important for our customers.

Basically, there are two scenarios of bringing changes to an LTS SapMachine. The first and preferred one is to contribute them to the up-stream OpenJDK project and consume them automatically as OpenJDK down-stream project. Only if that's not possible, we will integrate the changes right into the SapMachine branches.

## Contributing through the OpenJDK

If a new Java version is already in [rampdown phase](http://openjdk.java.net/jeps/3), try to bring your change to the corresponding OpenJDK jdk/jdk\<version\> repository as long as possible. If successful, such changes will be automatically merged to jdk/jdk. Only if you can't bring them into the rampdown repository any more, contribute them to the OpenJDK jdk/jdk repository.

After your change was accepted in OpenJDK bring it to SapMachine:

1. Try to downport your change to the jdk-updates repository of the long term support release (jdk-updates/jdk11u).  Only in special cases (e.g., severe bug fixes) try to downport to non-LTS releases. If this succeeds the change will be automatically merged into the corresponding SapMachine release.

2. If 1. failed, downport your change directly to the long term support branch of SapMachine (currently sapmachine11).  Only in special cases downport it to non-LTS releases. Use git cherrypick to move the change from sapmachine to sapmachine\<version\>. These changes must not be tagged by "// SapMachine YYYY-MM-DD".

Eventual merge conflicts with upstream changes introduced by the automatic merge process must be dealt with on-demand. The risk for such conflicts and the associated merge effort depends on the number and nature of changes in the update repositories which again depends on the future release maintainers.

If the downported change is a feature listed in [Features Contributed by SAP](https://github.com/SAP/SapMachine/wiki/Features-Contributed-by-SAP) add the version of SapMachine to which you downported the feature.

No further maintenance of this very change will be necessary.  

In rare cases, e.g. urgent bug fixes, it can be necessary to first bring a change to a sapmachine\<version\> repository and then submit it to OpenJDK.

[[/images/SapMachine_merge_downport.png|SapMachine downports and merges]]

## SapMachine-only changes.

If a change is not accepted in OpenJDK at all, think twice whether it is necessary. There should be a clear business case for it. Try to implement it in a way that is easy to merge and robust wrt. upstream changes.

1. Open an issue in the git issue system. See [Formal Requirements of Pull Requests](https://github.com/SAP/SapMachine/wiki/Formal-Requirements-of-Pull-Requests)  Submit your change to branch sapmachine. The changes in the source code should be tagged similar as in SAP JVM, but without developer name: // SapMachine YYYY-MM-DD

2. Then downport your change to long term supported branches (currently sapmachine11) and branches not yet released.  Only in special cases downport it to released non-LTS branches.

3. Document your change in the wiki page [Differences between SapMachine and OpenJDK](https://github.com/SAP/SapMachine/wiki/Differences-between-SapMachine-and-OpenJDK)

When a new sapmachine branch is set up, what will be the case every half year, the person setting up this branch will merge all our SapMachine-only changes from branch sapmachine into this new branch.

All SapMachine-only changes will be maintained 'forever' in up to four sapmachine branches. This means we will resolve conflicts in the automatic merges with upstream changes. Especially maintaining the main sapmachine repository will be tedious, as here the rate of changes is high and many changes are essential. Thus be very careful in submitting such changes. If this can not be avoided, try to replace the change with one accepted in OpenJDK in the long run.

Once we run into many merge conflicts we might have to re-think how to handle SapMachine-only changes.

## Changes affecting the Java standard.

Changes affecting the Java standard or breaking the jck test suite can not be downported as-is. Either refrain from downporting them, or implement a suitable replacement.





# Contributing - Step by Step

* Clone the repository and checkout the branch to which you want to add your changes. Alternatively you can fork the SapMachine repository and work in your fork. This is required if you don't have the permission to work on the SapMachine repository (e.g. push new branches) or don't want to pollute the master repository with development branches.

```
    git clone http://github.com/SAP/SapMachine
    cd SapMachine
    git checkout sapmachine
```

* Create a new branch for your development.
```
    git checkout -b my-feature-branch
```
* Make your changes - In case you have a patch file you can apply it:
```
    git apply --verbose --whitespace=fix --reject my-changes.changeset
```
* Check your changed files using `git status`. 
  You might need to stage untracked files using `git add`. 

* Commit your changes:
``` 
    git commit -a
```
* Alternative: instead of patching or editing and then commiting a change, you can cherry-pick it if it is already somewhere in our git repository:
```
    git cherry-pick -x 82a4d39b0e6e21061bfd30b34eeea7805f5a9056
```
* Push your branch to github.
```
    git push --set-upstream origin my-feature-branch
```
* Create a pull-request. Visit the [repository](https://github.com/SAP/SapMachine/) with your browser. Using the web UI, create a new PR to merge your branch into sapmachine or sapmachine\<version\>.  See also [creating a pull request](https://help.github.com/articles/creating-a-pull-request/). Once the PR is created an automatic build and verification job is started. The PR can be merged if two reviewers approve the change and the test build and verification finished successfully. The PR verification will run some jtreg regression tests, especially from areas where SapMachine has different behaviour compared to OpenJDK.
