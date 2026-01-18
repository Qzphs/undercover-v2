class File:
    """
    Parse and represent a file containing word pairs.

    Word files are .txt files with one word pair on each line. The
    civilian and undercover words within each pair should be separated
    by a single comma (`,`). The `#` character is reserved for
    commenting out lines; both the game and the user are free to use
    this as needed.

    Compared to Undercover v1, this class is more tolerant of malformed
    data (it ignores lines it can't parse), strips whitespace, and
    preserves the contents of the original files.
    """

    def __init__(self, filename: str):
        self.name = filename.removeprefix("words/")
        self.filename = filename
        self.lines: list[str] = []
        with open(self.filename) as file:
            self.lines.extend(file.read().splitlines())

    def _word_pairs(self):
        return (
            (i, line)
            for i, line in enumerate(self.lines)
            if not line.startswith("#") and line.count(",") == 1
        )

    @property
    def n_pairs(self):
        """The number of valid word pairs remaining in the file."""
        return len(list(self._word_pairs()))

    def get(self):
        """
        Return the next valid word pair in the file.

        This method also comments out the word pair by prepending a #.

        If there are no more valid word pairs, return None.
        """
        next_pair = next(self._word_pairs(), None)
        if next_pair is None:
            return
        i, line = next_pair
        c_word, u_word = line.split(",")
        self.lines[i] = "# " + self.lines[i]
        return c_word.strip(), u_word.strip()

    def save(self):
        with open(self.filename, "w") as file:
            file.write("\n".join(self.lines) + "\n")
