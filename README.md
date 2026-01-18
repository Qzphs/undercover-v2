GUI for playing Undercover. This program replaces Undercover v1 (its
predecessor) and [monabgames.com](https://monabgames.com/undercover).

You need to create the words yourself and feed it into the program.


## Run this code

You will need [Python](https://www.python.org/downloads/) installed.

On the GitHub page, click the green **Code** button, then click
**Download ZIP**. Unzip this on your computer.

The folder should contain a file called **main.py**. Open it using **IDLE**
(this is Python's code editor) and select **Run > Run Module**.


## File format for words

Write each pair of words (civilian word + undercover word) on its own line,
separated by a comma (`,`).

The hash symbol is reserved for comments (`#`). The program will use this to
'remove' (without actually deleting) your words after they are used. You may
use `#` at the start of a line to add comments if you wish.

Blank lines are okay anywhere in the file. You are encouraged to add several
blank lines at the beginning of the file so that your words don't get spoiled
by Discord's preview feature.

Your filename must end with **.txt**.

This is an example of what a valid file looks like:

```
bell, salmon
angry, red face
# this is a comment
```


## Add files to program

Add the file to the **words** folder.

When the program is run, it looks for any .txt files in that folder and reads
words from those files.
