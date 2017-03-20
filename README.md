# dup-music

Check for duplicate entries in my iTunes library.  Very naive implementation as all I am looking for are files with the pattern '01 Some Awesome Song 1.mpa' which usually suggests it is a copy.

Will iterate on and utilize to test out `async` and `await` and other concurrency methodologies in Python.  `os.walk` may already provide all I need.

Want to also think about building up some form of hash to compare file names as well as metadata to better identify duplicates rather than just regular expressions.

