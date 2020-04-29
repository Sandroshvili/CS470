Name:             TestPY
Version:          0.0.1
Release:          1%{?dist}
Summary:          Test  python  script  for  CS470  Lab

Group:            System
License:          GPL
URL:              https://github.com/Sandroshvili/CS470
Packager:         Giorgi Sandroshvili

Requires: bash
Requires: mc
Requires: dmidecode
BuildRoot: /root/rpmbuild/

%description
Some  test  python  script  for  displaying  random  messages. That ’s it.
This  test  script  is  dedicated  for  CS470  lab  course.

%prep
############################################
# Create the build tree and copy the files #
# from the development directories         #
# into the build tree.                     #
############################################

echo "BUILDROOT = $RPM_BUILD_ROOT"
mkdir  -p $RPM_BUILD_ROOT/usr/bin/

cp -R ../SOURCES/test.py  $RPM_BUILD_ROOT/usr/bin

exit

%files
%attr (0777, root, root) /usr/bin/*

%post
#########################################################
# Do some random stuff, e.g. install vim, htop and tmux #
#########################################################
yum  install  vim  htop  tmux -y
cd /usr/bin
# Save  the old  test.py if it  exists
if [ -e test.py ]
then
	cp test.py test.py.orig
fi
if [ ! -e /usr/bin/tst ]
then
	ln -s test.py tst
fi

%changelog
* Tue Apr 21 2020 Giorgi Sandroshvili sandroshvili13@gmail.com
- This is a lab  assignment  for CS470 , SDSU  Georgia.
Shows  simple  example  of  building  an RPM  package.
