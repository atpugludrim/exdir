if status is-interactive
    # Commands to run in interactive sessions can go here
end
set PATH $PATH "/home/mridul/bin"
alias pyq="python3 -q"
alias cp="cp -iv"
alias mv="mv -iv"
alias redshift="redshift -m vidmode"
fish_vi_key_bindings
#neofetch
function fish_prompt
    powerline-shell --shell bare $status
end
