## BetterAutomateOlympicCoding

Based on [AutomateOlympicCoding](https://github.com/epsilon573/AutomateOlympicCoding).

I wanted to write a crawler to implement the function of crawling **Codeforces** and **AtCoder** samples to the SublimeText plug-in FastOlympicCoding, and then I found the project above. Unfortunately, my system environment is **Linux** and the project does not work properly now. So this project was born.

### How to use?

- Make sure you have installed **SublimeText** and **FastOlympicCoding** extension.
- Install Python3.
- `pip install bs4`
- `pip install numpy`

Notice that you **must** put your cpp file like this:

+ Codeforces: `.../codeforces/1145/a.cpp`
+ AtCoder: `.../atcoder/arc114/a.cpp`

Then download this project.

+ Put `automate.py` to `/home/yourdir/`

+ Open `automate.sublime-build`, change `/home/zlxfth/automate.py` into `/home/yourdir/automate.py`

Open a cpp file, press `Ctrl+Shift+B` and choose `automate`, the samples will be crawled.

`Ctrl+Alt+B`  to check!

### Windows?

If you want to make it work on **Windows**, press `Ctrl+Shift+P`, input `FastOlympicCoding` and `Open Settings`, write:

```json
"tests_file_suffix": "__tests"
```

After that you should open `automate.py` and change the 8th line to:

```python
filename = sys.argv[1] + ".cpp__tests"
```
