The agent generated the instructions file copilot-instructions.md inside .github folder. I just had to add the line saying command is run in the form "uv run ...", otherwise the instruction files contain pretty much all that are required.

The agent followed the request to implement the user stories very well. It wrote the tests before the implementation, and everything worked perfectly, I did not have to fix anything. The tests also fail when I broke the implementation on purpose.

I learned about the agent instruction file, which is very helpful. However, I think these are very simple tasks in small scope, for which we can be mostly sure that the agent can implement without a problem or errors. Therefore, I don't think I learned much about responsibility and caution when delegating task to AI through this task, although I am, in fact, always check everything AI produces before approving.
