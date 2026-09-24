# Assignment: Text Analyzer

## Overview

Write a Python program that reads a public-domain book from [Project Gutenberg](https://www.gutenberg.org) and prints a statistical report about its text. The report covers word frequencies, common bigrams, sentence length, and how the book's vocabulary grows chapter by chapter.

You may choose any book, provided it is plain text, in the public domain, and divided into chapters (for example, *Pride and Prejudice*, *Alice's Adventures in Wonderland*, *Frankenstein*, or *Dracula*). Download the plain-text (UTF-8) version and save it locally.

## Definitions

Use these definitions exactly so that results are consistent.

- **Word:** a maximal run of letters and apostrophes (e.g. `don't` is one word). Words are compared case-insensitively, so `The` and `the` are the same word. Numbers and standalone punctuation are not words.
- **Sentence:** a stretch of text ending in `.`, `!`, or `?`. Sentence length is the number of words in it.
- **Bigram:** a pair of consecutive words that appear in the same sentence. A bigram never spans a sentence boundary.
- **Chapter:** a section of the book beginning with a heading line such as `CHAPTER I` or `Chapter 1`. Each book will need its own heading pattern.
- **Book text:** only the text between Project Gutenberg's `*** START OF ...` and `*** END OF ...` markers. The license header and footer must not be counted.

## Requirements

Your program must:

1. **Read** the book file given as a command-line argument (or, if you prefer, a path you set at the top of the script).
2. **Report total statistics:** total number of words, number of unique words, and number of sentences.
3. **Report the top N most common words** with their counts, in descending order of frequency. Ties are broken alphabetically. N defaults to 20.
4. **Report the top N most common words excluding stop words.** Use a stop-word list of at least 30 common English words (`the`, `and`, `of`, ...) stored in a set in your program.
5. **Report the top N most common bigrams** with their counts, in descending order, with ties broken alphabetically.
6. **Report the average sentence length** in words (to 2 decimal places), plus the length of the longest sentence and the first 60 characters of that sentence.
7. **Report vocabulary growth across chapters.** For each chapter, print:
   - the number of words in the chapter,
   - the number of unique words in the chapter,
   - the number of *new* words (words that appear in this chapter and in no earlier chapter),
   - the *cumulative* vocabulary size after this chapter.
8. **Report hapax legomena:** the number of words that appear exactly once in the whole book, and the first 10 of them in alphabetical order.

## Constraints

- Use only the Python standard library. You may use `re` and `sys`, but you may not use `collections.Counter` or any external NLP library (such as `nltk`).
- Your program must be organized into functions, each with a docstring stating what it takes and returns. Do not put all logic at the top level.
- The program must run without errors on the book you choose and print the full report in a single run.
- Your code must be your own. You may discuss ideas with classmates, but do not share or copy code.

## Sample Output

The numbers below are for illustration only. Your values and layout may differ slightly, but every item above must be present and clearly labeled.

```
=== Text Analyzer: Alice's Adventures in Wonderland ===

Total words:       26,500
Unique words:       2,600
Sentences:          1,650

--- Top 5 words ---
the        1,630
and          866
to           725
a            631
she          542

--- Top 5 bigrams ---
of the       128
said the      75
in a          70
...

--- Sentence length ---
Average: 16.06 words
Longest: 210 words ("Alice was beginning to get very tired of sitting b...")

--- Vocabulary growth ---
Chapter  Words  Unique  New  Cumulative
1        2,100     700  700        700
2        2,300     780  420      1,120
...
```

## Deliverables

Submit the following:

1. `text_analyzer.py`: your program.
2. The plain-text book file you analyzed (or its Gutenberg URL/ID if the file is very large).
3. `report.txt`: the complete output of one run of your program.
4. `README.md` (a few lines): which book you used, how to run your program, and the chapter-heading pattern you used.

## Grading

| Component | Points |
|---|---|
| Correct total statistics and word frequencies | 20 |
| Correct bigram counts | 15 |
| Correct sentence-length statistics | 15 |
| Correct vocabulary growth table | 20 |
| Hapax legomena and stop-word-filtered list | 10 |
| Code organization, docstrings, and readability | 15 |
| README and report file | 5 |
| **Total** | **100** |

## Extension (Optional, No Extra Credit)

Given a word typed by the user, print the three words that most often follow it in the book. This is the first step toward the next-word prediction model you'll build later in the course.