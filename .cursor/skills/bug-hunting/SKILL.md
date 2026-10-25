---
name: bug-hunting
description: Looks up and find bugs in a codebase. The goal is not only to fix them, but to understand why they appeared, which is the scope of the bug and which is the whole vertical and horizontal feature that is affecting - from end to end in the system. Invoke when the user tells you to "hunt a bug", "go hunting" or "hunt this".
argument-hint: "What are we fixing chief?"
license: free of use
---

The user has asked you to fix a bug. 

## Understand the bug
The first step is to locate and understand the bug. This will be done by inspecting the code base.
- If there are missing pieces of understanding or feature knowledge that you don't have directly from the codebase, ask the user throughly until you have the full understanding of the feature - or what the feature should be doing.
- Inspect the codebase horizontally: don't just understand the feature vertically, take a look to other parts of the application close to the feature so you can have a full picture of that part of the product to make sure we are not adding more bugs in the fix process.

At this point, you should have a clear understanding of the codebase, of the bug, of why is it appearing and how to fix it without breaking anything.

## Fix the bug
Once you have a clear understanding of the bug, fix it step by step.
- Make sure that you are editing the least amount of lines of code, in the cleanest and most secure way possible to fix the bug.
- Never edit things without knowing the full impact. If you are not 100% sure of the impact the changes could have in other files, return to the previous phase.
- After the bug is fixed, take a look at the test suit to see if there already are tests that cover that part: if so, update them to cover the bug. If there are not, create them to just cover the bug.

## Report the bug
Once you have this understanding, save it into a bug report inside a `/product/bug-hunting/<today's_date>/<rememberable_name_of_the_bug>.md` file. This report will have the following schema
``` markdown
## a name or title so we can pinpoint and search the bugs. it can be the same one as the file.
**Description:** a short but detiled description of what the bug was causing.

**Steps to reproduce:** steps to reproduce the bug.
**Expected results:** the expected results from the product/feature point of view.
**Actual results:** the actual behavior observed by the user.

## Fix
a detailed fix of the bug, step by step, explaining which files have been touched, why those specific files, why it related to the bug and a detailed explanation for future developers.
```