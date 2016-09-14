#!/bin/bash

BASE=""
CAMADDRS=""
CAMNAMES=""
CONFIG="./config"
PARSE_CAMERAS=false

while read line
do
  if [[ "$line" == "#cameras" ]]
  then
    PARSE_CAMERAS=true
    continue
  fi

  if [[ "$PARSE_CAMERAS" == true ]]
  then
    CAMNAME=$(echo "$line" | cut -d' ' -f1)
    CAMADDR=$(echo "$line" | cut -d' ' -f2)

    CAMADDRS="$CAMADDRS$CAMADDR "
    CAMNAMES="$CAMNAMES$CAMNAME "
  else
    if [[ "$line" == basedir* ]]
    then
      BASE=$(echo "$line" | cut -d' ' -f2)
    elif [[ "$line" == interval* ]]
    then
      INTERVAL=$(echo "$line" | cut -d' ' -f2)
    fi
  fi

done < $CONFIG

echo -e "\ncameras:"
echo $CAMNAMES
echo -e "\nwith addresses:"
echo $CAMADDRS
echo -e "\nbase directory:"
echo $BASE

if [ ! -d "$BASE" ]; then
  mkdir $BASE
fi

for CAM in $CAMNAMES
do
  if [ ! -d "$BASE/$CAM" ]; then
    mkdir $BASE/$CAM
  fi
done

