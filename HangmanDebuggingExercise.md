# Hangman debugging exercise
When your code doesn't do what you expect, you might find yourself staring at your code, hoping you'll just find the bug, or littering your code with `print` statements to see what's happening. Debuggers are designed to help you find bugs faster: easy bugs become trivial, and hard bugs become find-able. This exercise will help you learn to use a debugger. There are multiple debuggers available for nearly every programming language, but this tutorial will explain the basics using Python and PyCharm.

## Get the code
[Follow this link](https://github.com/mehaKumar/hangman-debug) and click the green 'Clone or download' button. Download and unzip the .zip file, or if you're familiar with git, clone the repository by running `git clone <url provided in the box>` from a terminal.

## Install and set up PyCharm
* [Follow this link](https://www.jetbrains.com/pycharm/download/#section=windows) to download and install PyCharm for your OS.
* Open PyCharm, and open `hangman.py` (in the directory from the last step).
* Go to the bottom right corner and click on ``<No Interpreter>``. You need to tell PyCharm which version of Python to use to run this program. Click `Add Interpreter...` and you should be in the `Virtualenv Environment` section. In the location box, replace `/hangman.py` with `/venv`. This exercise should be run with Python 3.

## Debugging time
To run the program, use the `Run` menu at the top. This is equivalent to running `python hangman.py` from a terminal. At the bottom, you'll be able to play the game. As you play, you may notice some bugs:
1. When you guess a letter you've guessed before, it doesn't tell you. The game is supposed to ask you for another guess.
2. There's always one blank at the end you can't seem to guess, even when you think you know the word.
3. It won't let you play another game, even when you type `Y` when it prompts you at the end of a game.

#### Let's solve these bugs with the help of a debugger!
We need to set a breakpoint in our code and then run the code in the debugger.
* A **breakpoint** tells your code to stop on a certain line. Setting a breakpoint on the first line of `main()` is a good way to start debugging. Click just to the right of a line number to set a breakpoint, which will appear as a red circle.
* A **debugger** lets you run your code and hit the breakpoints you set (running the code like normal will ignore breakpoints). To run your code in the debugger, go to `Run`>`Debug 'hangman'`.

While you are in debug mode, you will be able to see the values of variables and explore your program more easily than with `print` statements. Here are some useful tools:

* **Step around**: Once you hit a breakpoint, you may want to reach other lines.
  - Step over: runs to the next line of code.
  - Step into: runs to the next line of code, or if the line contains a function, it will enter that function.
  - Step out: runs the rest of this function, stopping on the line that called it.
  - Continue: runs the rest of the program until it finishes, or until another breakpoint is hit.
* **View variables**: The debugger window at the bottom will have a panel named `Variables`. Here, the current defined variables should be listed-- if anything you want to see is missing, you can right-click on the variable in the code view window and click `Add to Watches`
* **Evaluate expression**: see the value of an expression rather than a variable.
* **Find Usages**: right-click on a function name or variable and click `Find Usages`. This is more useful for larger projects where you might want to see where a variable is changed or where a function is called.
