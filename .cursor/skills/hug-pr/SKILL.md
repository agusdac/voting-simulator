---
name: hug-pr
description: invoke when the user asks to "hug a PR", "give love to a PR" or "check this PR"
---

# Hug a PR - What to do
Your goal is to periodically check the assinged PR that the user told you to hug.
Hugging a PR means grabbing it so thighly that each time a contributor or a code review tool leaves a comment, an inquery, a doubt or any kind of information that can improve the code or the mergeability of the PR you will address it as a senior software engineer.
You will update the code only or the structure only if it makes sense.

## There is no PR - create a normal PR (no draft)
This skill grants you the permission to create a PR. If the user tells you to "hug the PR" but no PR exists, you can create it and then hug it.
Create a PR in all origins that you have access to. If there is an auth problem or a doubt, state it to the user.

# What not to do
- Only assume that what the comment states is correct if you can check it, verify it or reproduce it.
- Always ask questions if the comment is not clear, you don't understand something or there is some place (both code or product docs) that contradicts or rejects an idea.

# When fixing a comment
When you fix a comment you should always output in chat a summary of the fix, with this format:
**Title of the comment or fix**
- what was the comment (or the idea behind id)
- the proposed fix, if any
**One liner with what you found and if it makes sense to fix**
- what you found once you looked up
- what is the fix you applied
Two or three lines of your human-personal opinion about the finding and the way it integrates to the software.
