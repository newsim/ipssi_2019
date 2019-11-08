Description exam2 Simon Amoyal

================================

Les fichiers présent dans le repertoire exam2

------------------------------------------------

* les exercices
    * exercice1 de type shell
    * exercice2 de type shell
    * exercice3 de python
    * exercice4
    * exercice5
    * exercice6
    * exercice7
    * exercice8
    * exercice9
    * exercice10
    * exercice11
    * exercice12
    * exercice13
    * exercice14
* exemples de codes

Voici un exemple de script bash :

        #!/bin/bash

        set -e

        if [ -z 'www.google.com' ];then
            echo "donnez un nom de site"
            exit 1
        else
            if curl -s -I 'www.google.com' >/dev/null ;then
                echo $(date '+%Y-%m-%d %H:%M:%S') "internet OK" >> internet.log
            else
                echo $(date '+%Y-%m-%d %H:%M:%S') "internet FAIL" >> internet.log
                exit 2
            fi
        fi


        exit 0


