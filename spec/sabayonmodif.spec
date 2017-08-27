# ARQUIVO DE ESPECIFICAÇÕES PARA O USO DO PACOTE 
# REMASTERIZADOR DE SABAYON, O MOLÉCULE.
# LEIA COM ATENÇÃO E MODIFIQUE AS OPÇÕES ABAIXO, 
# ADEQUANDO-AS AO SEU USUÁRIO. A ISO A SER 
# REMASTERIZADA, ESTE ARQUIVO "sabayonmodif.spec" E
# A ISO A SER GERADA DEVEM ESTAR NO MESMO DIRETÓRIO,
# E COM NOMES ADEQUADOS.
# DETALHES VEJA EM:
# www.vivaolinux.com.br/artigo/Sabayon-Linux-5.3-versoes-futuras-
# e-seu-potencial-+-remasterizacao/
# sabayonbrasil.org/planet/?p=4
# wiki.sabayon.org/index.php?title=HOWTO:_Using_Molecule_Example

# Sabayon Linux 64 bits modified Molecule remaster spec file
# The aim of this spec file is to add applications
# for making a remasterized ISO of Sabayon Linux
# By The Sabayon Team and modified by Joost Ruis, 2010,
# further modified by Alberto Federman Neto, Brazil, 2010.

# to an already built ISO image
# via scripting (providing hooks that call
# user-defined scripts).
# squashfs, mkisofs needed as installed dependencies

# MOLECULE, REMASTERIZADOR SABAYON:

# INSTALE O PACOTE MOLECULE 
# ("sudo equo install --verbose molecule")
# LEIA COM ATENÇÃO, EDITE AS LINHAS ADEQUADAMENTE, GRAVE # A ISO QUE QUER REMASTERIZAR E SALVE ESTE ARQUIVO 
# (EX. COMO sabayonmodif.spec), 
# TUDO NO MESMO DIRETÓRIO, DEPOIS NESSE DIRETÓRIO, 
# EXECUTE O COMANDO: 
# "molecule sabayonmodif.spec", COMO ROOT.

& misc stuff

# Não necessário mudar aqui:
# Define an alternative execution strategy, in this case, the value 
# must be
# "iso_remaster"
execution_strategy: iso_remaster

# 1. Somente para fazer ISO de 32 Bits em comp. de 64 Bits,   
# descomente. Outros casos, deixe assim mesmo:

# pre chroot command, example, for 32bit chroots on 64bit system
# you always
# have to append "linux32" this is useful for inner_chroot_script
# prechroot: linux32

# 2. Modifique aqui para o caminho, pastas, onde estiver gravada a # ISO que quer remasterizar (renomeie para sabayon.iso)
# Deve ser o mesmo diretorio onde vc quer montar, gravar a sua ISO do Sabayon. Mudar para o seu usuário:

# Path to source ISO file (MANDATORY)
source_iso: /home/sabayonuser/projects/my_custom_sabayon_livedvd/livedvd/Sabayon_Linux_DAILY_amd64_GNOME-dev.iso

# 3. Nao precisa editar, são linhas apenas para casos de erros de 
# compilação e remasterização:

# Error script command, executed when something went wrong and molecule has  # to terminate the execution
# environment variables exported:
# - CHROOT_DIR: path to chroot directory, if any
# - CDROOT_DIR: path to livecd root directory, if any
# - SOURCE_CHROOT_DIR: path from where chroot is copied for final handling
# error_script: /path/to/script/to/be/executed/outside/after

# Outer chroot script command, to be executed outside destination chroot 
# before
# before entering it (and before inner_chroot_script)
outer_chroot_script: /home/sabayonuser/projects/my_custom_sabayon_livedvd/spec/remaster_pre.sh

# Inner chroot script command, to be executed inside destination chroot 
# before packing it
# - kmerge.sh - setup kernel bins
# inner_chroot_script: /sabayon/scripts/inner_chroot_script.sh

# Inner chroot script command, to be executed inside destination 
# chroot after
# packages installation and removal
# inner_chroot_script_after: 
# /home/albfneto/Desktop/molecule/inner_chroot_script_after.sh

# 4. Aqui, deve deixar a instruções como estão, para fazer sua ISO # ser instalável:

# Outer chroot script command, to be executed outside destination chroot before
# before entering it (and AFTER inner_chroot_script)
outer_chroot_script_after: /home/sabayonuser/projects/my_custom_sabayon_livedvd/spec/remaster_post.sh
# Extra mkisofs parameters, perhaps something to include/use your bootloader
extra_mkisofs_parameters: -b isolinux/isolinux.bin -c isolinux/boot.cat

# Não necessário modificar:
# Pre-ISO building script. Hook to be able to copy kernel images in place, for example
# pre_iso_script: /sabayon/scripts/cdroot.py

# 5. Aqui deve colocar o diretório onde quer salvar sua ISO remasterizada, por Ex. o mesmo diretório do Ítem 2:

# Destination directory for the ISO image path (MANDATORY)
destination_iso_directory: /home/sabayonuser/projects/my_custom_sabayon_livedvd/livedvd/molecule_

# 6. Nomes para a ISO remasterizada, e para o DVD, coloque nomes ou deixe com está:

# Destination ISO image name, call whatever you want.iso, NOT MANDATORY
 destination_iso_image_name:custom_daily_Sabayon.iso

# Output iso image title NOT MANDATORY
#iso_title:minhaSabayonmodif
iso_title:Sabayon GNOME
# Não necessário mudar aqui:
# Alternative ISO file mount command (default is: mount -o loop -t iso9660)
# iso_mounter:

# Não necessário mudar aqui:
# Alternative ISO umounter command (default is: umount)
# Alternative squashfs file mount command (default is: mount -o loop -t squashfs)
# squash_mounter:

# Não necessário mudar aqui:
# Alternative ISO squashfs umount command (default is: umount)
#squash_umounter:

# Não descomente, induz a êrros, somente para casos especiais
# Merge directory with destination LiveCD root
# merge_livecd_root: /put/more/files/onto/CD/root

# 7. Aqui, se você quiser tirar pacotes da distro original, antes de 
# remasterizar, descomente e substitua "clementine" pelos pacotes # que quer tirar, separados por vírgulas. 

# List of packages that would be removed from chrooted system 
# (comma separated)
# packages_to_remove:clementine

# Se você removeu pacotes, como no Ítem 7, e  estes pacotes tem 
# dependências,descomente. equivale a não usar "equo remove", 
# mas sim"equo remove" sem tirar as dependências e limpando a
# instalação:

# Custom shell call to packages removal (default is: equo remove)
# custom_packages_remove_cmd: 
# equo remove --nodeps --configfiles

# 8. Pacotes a serem adicionados. coloque aqui tudo o que quer 
# adicionar, alem do que já esta na Sabayon ISO original a ser 
# remasterizada. Por exemplo, para remasterizar uma Sabayon 
# completa com todos os ambientes gráficos e já configurada 
# para placa de vídeo NVIDIA use a lista de pacotes do 
# exemplo abaixo.
# para modificar ou adicionar outros pacotes, adicione ou remova o # que quiser:

# List of packages that would be added from chrooted system (comma separated)

packages_to_add:net-p2p/amule,dev-util/molecule,sys-process/cronie,dev-tcltk/expect,dev-db/redis,dev-python/redis-py,dev-python/gntp,app-i18n/ibus-libpinyin,app-i18n/ibus-rime,games-util/steam-launcher,x11-misc/xdotool,x11-apps/xwininfo,media-gfx/imagemagick,media-libs/exiftool,dev-python/pdfrw,net-misc/tightvnc,net-misc/netkit-telnetd,app-emulation/virtualbox-bin,app-emulation/virtualbox-modules,playonlinux,media-libs/opencv,media-video/vlc,media-fonts/arphicfonts,media-fonts/baekmuk-fonts,media-fonts/kochi-substitute,dev-java/oracle-jdk-bin,app-text/fbreader,sci-geosciences/googleearth,dev-python/virtualenv,app-editors/emacs,app-emulation/docker,dev-python/pip,sys-devel/gcc,app-misc/sabayon-devkit,x11-terms/terminator,app-arch/rar,app-arch/unrar,x11-misc/xbindkeys,app-emulation/winetricks,app-portage/eix,dev-util/cmake,net-misc/socat,dev-vcs/git,app-portage/repoman,app-admin/enman,x11-misc/wmctrl,media-fonts/source-pro,app-portage/layman,app-misc/screen,app-misc/tmux,net-vpn/openvpn,app-misc/freemind,x11-apps/xmodmap,www-client/w3m

# Não necessário mudar aqui:
# Custom shell call to packages add (default is: equo install)
#custom_packages_add_cmd: equo install

# 9. Estas sao as linhas para mudar a tela default de Login, Default é # kdm. para a tela de login do GNOME, gdm, crie este 
# arquivo (veja tambem Item 3) e salve externamente, como 
# inner_chroot_script_after.sh e descomente em 10.
# Para detalhes veja os tutoriais na Net, de
# de Joost Ruis e Wolfden

# so I created my inner_chroot_script_after.sh
# !/bin/bash
# Use kdm by default
# sed -i 's/DISPLAYMANAGER=".*"/DISPLAYMANAGER="gdm"/g' /etc/conf.d/xdm
# automatic start of xdm, that loads kdm
# rc-update add xdm
# to be sure, clean the installation. Comment for no cleanup
# equo cleanup

# 10. chamada para o script do item 9.Se não modificou, deixe como # está. Se modificou em 9, descomente:

# All these commands should be put in a file, and we point our specs file to trigger it from within the chroot like this:
# Inner chroot script command, to be executed inside destination chroot after
# packages installation and removal
inner_chroot_script_after:/home/sabayonuser/projects/my_custom_sabayon_livedvd/spec/inner_chroot_script_after.sh

# Não necessário mudar aqui:
# Custom command for updating repositories (default is: equo update)
# repositories_update_cmd: equo update

# 11. Aqui, use yes se quiser atualizar os repositórios novamente, após remasterização:

# Determine whether repositories update should be run (if packages_to_add is # set)
# (default is: no), values are: yes, no.
execute_repositories_update: yes

# 12. Coloque aqui os diretórios que quiser remover ou esvaziar. 
# Se não houver, deixe comentado.

# Directories to remove completely (comma separated)
# paths_to_remove:
# Directories to empty (comma separated)
# paths_to_empty:
    
