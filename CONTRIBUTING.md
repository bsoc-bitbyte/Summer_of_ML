# Contributing to our projects

A big welcome to BSoC!

Reading and following these guidelines will help us make the contribution process easy and effective for everyone involved. It also communicates that you agree to respect the time of the developers managing and developing these open source projects. In return, we will reciprocate that respect by addressing your issue, assessing changes, and helping you finalize your pull requests.

## Quicklinks

* [Getting Started](#getting-started)
    * [Issues](#issues)
    * [Pull Requests](#pull-requests)
        * [Fork and Clone](#fork-and-clone)
        * [Work on Pull Request](#work-on-pull-request)
        * [Keep Your Fork Updated](#keep-your-fork-updated)
* [Getting Help](#getting-help)

## Getting Started

Contributions are made to this repo via Issues and Pull Requests (PRs). A few general guidelines that cover both:

- Search for existing Issues and PRs before creating your own.
- We work hard to makes sure issues are handled in a timely manner but, depending on the impact, it could take a while to investigate the root cause. A friendly ping in the comment thread to the submitter or a contributor can help draw attention if your issue is blocking.

### Issues

Issues should be used to report problems, request a new feature, or to discuss potential changes before a PR is created. When you create a new Issue, a template will be loaded that will guide you through collecting and providing the information we need to investigate.

If you find an Issue that addresses the problem you're having, please add your own reproduction information to the existing issue rather than creating a new one. Adding a [reaction](https://github.blog/2016-03-10-add-reactions-to-pull-requests-issues-and-comments/) can also help be indicating to our maintainers that a particular problem is affecting more than just the reporter.

### Pull Requests

PRs to our projects are always welcome and can be a quick way to get your fix or improvement slated for the next release. In general, PRs should:

- Only fix/add the functionality in question **OR** address wide-spread whitespace/style issues, not both.
- Address a single concern in the least number of changed lines as possible.
- Be accompanied by a complete Pull Request template (loaded automatically when a PR is created).

For changes that address core functionality or would require breaking changes (e.g. a major release), it's best to open an Issue to discuss your proposal first. This is not required but can save time creating and reviewing changes.

#### Fork and Clone


1. Fork the repository to your own Github account
2. Clone the project to your machine
    ```
    git clone https://GITHUB/USER-FORK/REPO.git
    cd REPO
    git remote add upstream https://GITHUB/UPSTREAM-OWNER/REPO.git
    git remote -v
    ```

Now the remote named `upstream` points to the upstream repository and the remote named `origin` points to your fork.


#### Work on Pull Request

Work on a new pull request in a new branch and commit it to your fork. Remember to use a meaningful name instead of `BRANCH` in the commands below.

1. Create a branch locally with a succinct but descriptive name
    ```
    git checkout -b BRANCH
    ```
2. Commit changes to the branch
    ```
    git add MENTION-FILES
    git commit
    ```
3. Push changes to your fork
    ```
    git push origin BRANCH
    ```
4. Open a PR in our repository and follow the PR template so that we can efficiently review the changes.
    - Go to your fork on GitHub.
    - Switch to the `BRANCH`.
    - Click *Compare & pull request*.
    - Click *Create pull request*.

Wait for an upstream developer to review and merge your pull request.

If there are review comments to be addressed, continue working on your branch, commiting, optionally rebasing, amending, squashing, and dropping them, and pushing them to the `branch` of `origin` (your fork). Any changes to the `branch` automatically become available in the pull request.

In the fork and pull request workflow, a contributor should never commit anything to the main development branch of personal fork. This makes it very easy to keep the main development branch of your fork in sync with that of the upstream repository. This is explained in the next subsection.

#### Keep Your Fork Updated

As new pull requests get merged into the upstream's main development branch, the main development branch of your fork begins falling behind it.

The commands below show how to update your fork's main development branch with the new commits in the upstream's main development branch.
```
  git checkout main
  git pull upstream main
  git push origin main
```

## Getting Help

Join us on [BSoC discord](https://discord.gg/WNDu3SxxFW) and post your questions there in the correct channel with a descriptive tag.