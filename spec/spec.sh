#!/bin/sh

rm -rf /home/sabayonuser/projects/my_custom_sabayon_livedvd/livedvd/molecule_
mkdir -p /home/sabayonuser/projects/my_custom_sabayon_livedvd/livedvd/molecule_
export MOLECULE_TMPDIR=/home/sabayonuser/projects/my_custom_sabayon_livedvd/var/tmp
molecule /home/sabayonuser/projects/my_custom_sabayon_livedvd/spec/sabayonmodif.spec

