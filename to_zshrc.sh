function fixcomm() {
    BUFFER=$(python ~/projects/terminalgpt/test_prefill.py --message $BUFFER)
    zle end-of-line
}
zle -N fixcomm
bindkey '^N' fixcomm

