#!/bin/sh

myname="${0##*/}"

gradience_dir="${HOME}/.var/app/com.github.GradienceTeam.Gradience/config/presets/user"
kvantum_dir="${XDG_CONFIG_HOME:-~/.config}/Kvantum"

wal_template_dir="${XDG_CACHE_HOME:-~/.cache}/wal"

# template name
# default: pywal
template=pywal

# theme name
# default: pywal
theme=pywal

settheme=0

_help () {
    printf 'usage: %s [OPTION]\n' "$myname"
    printf 'options:\n'
    printf '\t-n theme\tname for theme if not defalt. default: pywal\n'
    printf '\t-t template\tname for template if not default. default: pywal\n'
    printf '\t-s \t\tset themes with gradience and kvantum\n'
    printf '\t\t\tthis assumes gradience is installed through flatpak\n'
}


while getopts "n:t:sh" opt; do case "${opt}" in
  n)
    theme="$OPTARG"
    ;;
  t)
    template="$OPTARG"
    ;;
  s)
    settheme=1
    ;;
  h)
    _help
    exit 0
    ;;
  *)
    printf '%s: invalid option %s\n' "$myname" "$opt" >&2
    _help
    exit 1
    ;;
esac done


# copy gradience theme
ln -s "$wal_template_dir/${template}.json" "${gradience_dir}/${theme}.json"

# kvantum theme dir
kvtheme_dir="$kvantum_dir/${theme}"

# check if kvantum theme directory exists
if [ -d "$kvtheme_dir" ]; then
  mkdir -p "$kvtheme_dir"
fi

# copy kvantum theme
ln -s "$wal_template_dir/${template}.kvconfig" "$kvtheme_dir/${theme}.kvconfig"
ln -s "$wal_template_dir/${template}.svg" "$kvtheme_dir/${theme}.svg"

# do we actually set the themes?
if [ "$settheme" -eq 1 ]; then
  flatpak run --command=gradience-cli com.github.GradienceTeam.Gradience apply -n "$theme" --gtk both
  kvantummanager --set "$theme"
fi
