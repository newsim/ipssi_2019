cpt=0
while read n;do

acc=$((acc+n))
cpt=$((cpt+1))
done
echo $((acc/cpt))
