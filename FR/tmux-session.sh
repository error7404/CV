#!/bin/bash

# Start a new tmux session called "CV"
tmux new-session -d -s CV

# Resize the tmux window to simulate A4 aspect ratio
tmux resize-window -x 116 -y 81

# Split the terminal into a grid
tmux split-window -v       # Horizontal split (bottom right)
tmux split-window -h       # Horizontal split (bottom left)
tmux select-pane -t 0
tmux split-window -h       # Vertical split (right)

# Set pane titles for clarity (optional)
tmux select-pane -t 0
tmux select-pane -T "Nom & Coordonnées"

tmux select-pane -t 1
tmux select-pane -T "Photo de Profil"

tmux select-pane -t 2
tmux select-pane -T "Éducation & Expérience"

tmux select-pane -t 3
tmux select-pane -T "Compétences"

# Enable pane titles in the status bar
tmux set-option -g pane-border-status top
tmux set-option -g pane-border-format "#{pane_title}"

# Set the color for selected and unselected pane borders to bright blue
tmux set-option -g pane-border-style fg=brightblue
tmux set-option -g pane-active-border-style fg=brightblue

# Resize the profile picture pane to fit the content
tmux resize-pane -t 1 -x 20 -y 13
# Resize the other panes to fit the content
tmux resize-pane -t 3 -x 44

# Fill in the content for each pane using echo (or use text files)
tmux send-keys -t 0 "clear && cat contact.txt && cat" C-m

# Display the profile picture in the top right pane
tmux send-keys -t 1 "clear && cat Profile_Picture.txt && cat" C-m

tmux send-keys -t 2 "clear && cat education.txt" C-m
sleep 2
tmux send-keys -t 2 "cat experiences.txt && cat" C-m

tmux send-keys -t 3 "clear && cat skills.md && tput civis && cat" C-m

# Attach to the session
tmux attach-session -t CV