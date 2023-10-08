#! /bin/bash

# Log the script location and time of execution.
echo "$(realpath $0) $(date +'%D %I:%M %p')"

# Change .jfif files in the target directory to .jpeg
function fix_jfif {
    local target_dir='/home/vivian/Dropbox/pictures/porn'
    for f in $(ls $target_dir/*/*.jfif 2>/dev/null); do
        echo "Fixing jfif file: $f"
        [ -f "$f" ] && mv -v "$f" "${f%jfif}jpeg"
    done
}

fix_jfif

# Some component of Gnome keeps creating these.
rmdir /home/vivian/Desktop
rmdir /home/vivian/Documents
rmdir /home/vivian/Downloads
rmdir /home/vivian/Pictures
rmdir /home/vivian/Videos
rmdir /home/vivian/Music
rmdir /home/vivian/Templates

