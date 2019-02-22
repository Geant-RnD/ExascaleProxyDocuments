#!/bin/bash -e

: ${FILE:=processes_data.txt}

if [ -n ${1} ]; then FILE=${1}; fi
if [ ! -e ${FILE} ]; then echo "File: '${FILE}' does not exit"; exit 1; fi

cat ${FILE} | egrep -v 'msc_|Ioni|Transportation|Elastic|Inelastic|phot_|compt_|conv_|photonNuclear|Rayl|Nuclear|annihil|Decay|Brem|PairProd|Coulomb|Capture|Killer|^----|^\|  '
