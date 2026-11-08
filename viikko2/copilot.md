# GitHub Copilot experience report
I found the code completion suggestions quite useful. It can create the code based on the function's documentation and also from a similar function that was created before. It was really convenient, but I don't want to use it at the moment when I'm trying to learn so I disabled it.

The explanation of the Pylint warning was also correct and tailored to my code.

The solution that the agent came up with was tested and worked perfectly, so was the unit test. The way Copilot created the stubreader was a bit different from the test last week. It created defined the players' info values in the setup function of the class instead of in the stubreader itself. I told it to change the code so that the values were defined in the stubreader because I think it would be less memory-consuming. The code also conformed to the pylint configuration rules.