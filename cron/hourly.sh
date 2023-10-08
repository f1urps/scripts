#! /bin/bash

# Log the script location and time of execution.
echo "$(realpath $0) $(date +'%D %I:%M %p')"

# Change .jfif files in my porn directory to .jpeg
function fix_jfif_porn {
    PORN_DIR=/home/vivian/Dropbox/Pictures/Porn
    for f in $(ls $PORN_DIR/*/*.jfif 2>/dev/null); do
        echo "Fixing jfif file: $f"
        [ -f "$f" ] && mv -v "$f" "${f%jfif}jpeg"
    done
}

fix_jfif_porn

# Some component of Gnome keeps creating these.
rmdir /home/vivian/Desktop
rmdir /home/vivian/Documents
rmdir /home/vivian/Downloads
rmdir /home/vivian/Pictures
rmdir /home/vivian/Videos
rmdir /home/vivian/Music
rmdir /home/vivian/Templates

