#!/usr/bin/python

"""Create a gratitude journal directory, and then year and month subdirectories. 
If they already exist, create a new day file in the appropriate place 
and open it in your editor of choice."""

import datetime
import pathlib
import os
import subprocess

def make_todaypath():
    """Make a path for a 'today' gratitude file."""
    year = str(datetime.datetime.timetuple(datetime.datetime.today()).tm_year)
    todaypath = os.environ["HOME"] + "/gratitude/" + year + "/"

    return todaypath


def make_todayfilename():
    """Make a filename for a 'today' gratitude file."""
    year = str(datetime.datetime.timetuple(datetime.datetime.today()).tm_year)
    month = str(datetime.datetime.timetuple(datetime.datetime.today()).tm_mon).zfill(2)
    day = str(datetime.datetime.timetuple(datetime.datetime.today()).tm_mday).zfill(2)
    todayfilename = year + month + day + "_gratitude.txt"

    return todayfilename


def check_gratitude_file():
    """See if there is a 'gratitude' file for today already."""
    todaypath = make_todaypath()

    if os.path.exists(todaypath):
        #print("yay!")
        pass
    else:
        #print("boo!")
        pathlib.Path(todaypath).mkdir(parents=True, exist_ok=True)
        check_gratitude_file()


def make_gratitude_file():
    """Check to be sure that there is gratitude file structure, and then make a file for today."""
    check_gratitude_file()
    todaypath = make_todaypath()
    todayfilename = make_todayfilename()
    if os.path.exists(todaypath + todayfilename):
        pass
    else:
        with open(todaypath + todayfilename, "w", encoding="utf-8") as grats:
            line = f"{todayfilename[0:4]}/{todayfilename[4:6]}/{todayfilename[6:8]}"
            line = line + " - Things to be grateful for:\n\n\n"
            grats.write(line)
    return todaypath + todayfilename


def open_gratitude_file(path):
    """Open the gratitude file in the default editor."""
    default_editor = "/usr/bin/vi"
    editor = os.environ.get("EDITOR", default_editor)
    subprocess.call([editor, path])


if __name__ == "__main__":
    open_gratitude_file(make_gratitude_file())
