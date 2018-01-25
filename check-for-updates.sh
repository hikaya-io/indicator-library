[ $(git rev-parse HEAD) = $(git ls-remote $(git rev-parse --abbrev-ref @{u} | \
> sed ‘s/\// /g’) | cut -f1) ] && echo up to date || $HOME/indicator-library/deploy.sh