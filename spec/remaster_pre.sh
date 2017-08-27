#!/bin/sh

mkdir -p "${CHROOT_DIR}/dev"
mount -o bind /dev "${CHROOT_DIR}/dev"
exit 0 
