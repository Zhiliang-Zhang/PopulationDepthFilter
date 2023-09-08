# PopulationDepthFilter

## Step 1: Population depth and SD
Format of depth.txt: depth\tSD
```{}
python popdepth.py -s 100 -i depth.txt -o density.txt -x 20 -y 20
```
## Step 2: Genome High Confidence region

choose top N% genome sites

## Step 3: Population variation filter
Format of ID.txt: depth\tSD\tchr-pos
```{}
for i in {41..42};do nohup python popdepth-ID.py -s 100 -i <(awk '{if($1 < 20 && $2 < 20)print}' ${i}-ID.txt) -o ${i}-density.txt -x 20 -y 20 2>${i}.error & done
```
