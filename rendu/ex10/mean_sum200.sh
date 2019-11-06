#!/bin/bash 



cpt=0
while read n;do
somme=$((somme+n))

acc=$((acc+n))
cpt=$((cpt+1))
done

echo $((acc/cpt))
echo $somme