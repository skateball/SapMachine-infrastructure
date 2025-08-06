SapMachine pull requests must fulfill formal requirements before they can be merged.
These formal requirements are checked by the SapMachine Bot.


***
Tl;dr 

- PR title:
  - "**_Issue title_**"
- PR body:
  - Last line must be "**_fixes #Issue-number_**"
- Merging:    
  - 1 commit (squash if needed), 
  - commit message must start with (or be): "**_SapMachine #Issue: Issue Title_**"
Commit message

***

As a first step, an issue must be created. Describe the bug that shall be fixed or the feature that shall be implemented in there. In case you are down-porting an OpenJDK fix from a higher branch, the issue should contain a link to the bug ticket in the OpenJDK bug system.

Now the pull request must reference this issue in its description. This is accomplished by writing `fixes #Issue` in the last line of the description.

Example
```
This line is an optional description of the pull request.
fixes #1234
```

For down-porting changes, the same issue id must be used for both, the original pull request in the sapmachine branch and for the pull request in the sapmachine<version> target branch.

When the pull request is merged, we want to see only one commit in the SapMachine target branch. The commit must reference the issue, that was created for this pull request. The first line of the commit message must be of the following format:

```
SapMachine #Issue: Issue Title
```

Example:
```
SapMachine #1234: Fix the build an ship it

This line is optional and contains a more detailed description of the fix I have done.
```

Unfortunately, GitHub provides no means for checking the commits when merging, so the person that does the merge has to take special care that the format is correct.

If the pull request contains only one commit that already has a correct message, you can chose the merge strategy "rebase". This will apply the commit on top of the target branch via fast-forward. It can be that this does not work out, e.g. when the target branch has diverged from the time the pull request was created.

If the pull request contains multiple commits, the commit message of a single commit does not have the right format or rebasing via fast-forward is not possible, you might chose the strategy "squash". See the 
[Git Help](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History) on how to do that. In that case all commits of the pull request will be merged into one commit and you will get the possibility to edit the commit message in the WebUI.
