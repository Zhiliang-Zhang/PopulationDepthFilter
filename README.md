# PopulationDepthFilter

## Step 1: Population depth and SD
Format of depth.txt: depth\tSD
```{}
for i in {1..42};do nohup python popdepth.py -s 100 -i ${i}-depth.txt -o ${i}-density.txt -x 20 -y 20 & done
Usage:  -s: 100*100
        -x: x max
        -y: y max
```
## Step 2: Genome High Confidence region

choose top N% genome sites

## Step 3: Population variation filter
Format of ID.txt: depth\tSD\tchr-pos
```{}
for i in {1..42};do nohup python popdepth-ID.py -s 100 -i <(awk '{if($1 < 20 && $2 < 20)print}' ${i}-ID.txt) -o ${i}-density.txt -x 20 -y 20 2>${i}.error & done
Usage:  -s: 100*100
        -x: x max
        -y: y max
```
