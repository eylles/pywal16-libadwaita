#!/bin/sh

. "$HOME"/.cache/wal/qtcolors.sh

build_qt_style() {
sed \
  -e 's/,  /,/g' \
  -e 's/%FG%/'"$FG"'/g' \
  -e 's/%BTN_BG%/'"$BTN_BG"'/g' \
  -e 's/%BRG%/'"$BRIGHT"'/g' \
  -e 's/%L_BRG%/'"$L_BRIGHT"'/g' \
  -e 's/%DRK%/'"$DARK"'/g' \
  -e 's/%L_DRK%/'"$L_DARK"'/g' \
  -e 's/%N_FG%/'"$N_FG"'/g' \
  -e 's/%B_FG%/'"$B_FG"'/g' \
  -e 's/%BTN_FG%/'"$BTN_FG"'/g' \
  -e 's/%N_BG%/'"$N_BG"'/g' \
  -e 's/%WINDOW%/'"$WINDOW"'/g' \
  -e 's/%SHADOW%/'"$SHADOW"'/g' \
  -e 's/%SEL_BG%/'"$SEL_BG"'/g' \
  -e 's/%SEL_FG%/'"$SEL_FG"'/g' \
  -e 's/%LINK%/'"$LINK"'/g' \
  -e 's/%V_LINK%/'"$V_LINK"'/g' \
  -e 's/%A_BG%/'"$A_BG"'/g' \
  -e 's/%DFLT%/'"$DEFAULT"'/g' \
  -e 's/%TT_BG%/'"$TOOLTIP_BG"'/g' \
  -e 's/%TT_FG%/'"$TOOLTIP_FG"'/g' \
  -e 's/%PHLD%/'"$PLACEHOLDER"'/g' \
  -e 's/%D_FG%/'"$D_FG"'/g' \
  -e 's/%D_BTN_BG%/'"$D_BTN_BG"'/g' \
  -e 's/%D_BRG%/'"$D_BRIGHT"'/g' \
  -e 's/%D_L_BRG%/'"$D_L_BRIGHT"'/g' \
  -e 's/%D_DRK%/'"$D_DARK"'/g'\
  -e 's/%D_L_DRK%/'"$D_L_DARK"'/g' \
  -e 's/%D_N_FG%/'"$D_N_FG"'/g' \
  -e 's/%D_B_FG%/'"$D_B_FG"'/g' \
  -e 's/%D_BTN_FG%/'"$D_BTN_FG"'/g' \
  -e 's/%D_N_BG%/'"$D_N_BG"'/g' \
  -e 's/%D_WINDOW%/'"$D_WINDOW"'/g' \
  -e 's/%D_SHADOW%/'"$D_SHADOW"'/g' \
  -e 's/%D_SEL_BG%/'"$D_SEL_BG"'/g' \
  -e 's/%D_SEL_FG%/'"$D_SEL_FG"'/g' \
  -e 's/%D_LINK%/'"$D_LINK"'/g' \
  -e 's/%D_V_LINK%/'"$D_V_LINK"'/g' \
  -e 's/%D_A_BG%/'"$D_A_BG"'/g' \
  -e 's/%D_DFLT%/'"$D_DEFAULT"'/g' \
  -e 's/%D_TT_BG%/'"$D_TOOLTIP_BG"'/g' \
  -e 's/%D_TT_FG%/'"$D_TOOLTIP_FG"'/g' \
  -e 's/%D_PHLD%/'"$D_PLACEHOLDER"'/g' \
  "$HOME"/.config/wal/qtcolorscheme.conf
}

echo "building qt5ct pywal.conf"
build_qt_style > ~/.config/qt5ct/colors/pywal.conf
echo "building qt5ct pywal.conf"
build_qt_style > ~/.config/qt6ct/colors/pywal.conf
echo "copying pywal.kvconfig"
cp ~/.cache/wal/pywal.kvconfig ~/.config/Kvantum/pywal/pywal.kvconfig
echo "copying pywal.svg"
cp ~/.cache/wal/pywal.svg ~/.config/Kvantum/pywal/pywal.svg
