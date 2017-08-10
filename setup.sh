#!/bin/sh

echo "alias pingg='ping -c 1 google.co.jp'" >> $HOME/.bashrc
echo "alias curlg='curl google.co.jp'" >> $HOME/.bashrc

echo 'export PATH=$PATH:$HOME/ponpontools/commands/' >> $HOME/.bashrc
echo -e "\e[33mplease exec\e[m: source $HOME/.bashrc"

