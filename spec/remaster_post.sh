#!/bin/sh

rm -rf "${CHROOT_PKGS_DIR}"{,-nonfree,-restricted}/*
#cp /spin/background/sabayon-forensic.png "${CHROOT_DIR}/usr/share/backgrounds/sabayonlinux.png"
#cp /spin/background/sabayon-forensic.jpg "${CHROOT_DIR}/usr/share/backgrounds/sabayonlinux.jpg"
is_64=$(file "${CHROOT_DIR}"/bin/bash | grep "x86-64")
if [ -n "${is_64}" ]; then
    echo "equo cleanup" | chroot "${CHROOT_DIR}"
else
    echo "equo cleanup" | linux32 chroot "${CHROOT_DIR}"
fi




umount "${CHROOT_DIR}/dev"

