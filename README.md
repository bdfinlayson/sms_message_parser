## Usage
To view highlighted SMS messages tn the terminal in the root of the project, enter your SMS as follows:
```
$ python message_parser.py "Date at Luigis with my family and friends tomorrow at 7?"
> Date at _Luigis_ with my family and friends _tomorrow at 7_?
```

## The Assignment 
The assignment for this microlab is to replicate the SMSLinks to an external site. functionality found in most phones -- the ability to highlight the time and date mentioned in the SMS.

The assignment is to highlight the time and date mentioned in the SMS. You will "highlight" the data and time by placing data and time between two underscores ('_') if they are part of the same expression, including any time-related preposition between them (e.g., "at", "on"). Make sure you account for the names for the time of the day (afternoon, morning, etc.), days, weeks, months, years, and proximal or relative qualifiers (tomorrow, next day, last week, etc.)

For implementation, use only regular expressions supported by core Python 3, reLinks to an external site. package.

Optionally you can highlight the place. The place will earn you a mention in the post-lab class discussion, assuming you completed the time and date underscoring correctly. 

## Submission and grading
You will submit the single python file (message_parser.py), and I will execute it on the command line. Your program should accept a string, delineated by quotes ("..."), on a command line, and it should print the string back out to the command line with underscore highlights. Something like this:

$python> message_parser.py < “How about SoKno tomorrow at 7.”

$ “How about SoKno _tomorrow at 7_.”

or, for place, date and time implementation: 

$ “How about _SoKno_ _tomorrow at 7_.”

## Note
Try not to "overdo" this lab. Keep it very simple, and just pay attention to the correctness and completeness of your implementation. Do not plagiarize the solutions found on the forums, and do not ask LLMs to do it for you. 