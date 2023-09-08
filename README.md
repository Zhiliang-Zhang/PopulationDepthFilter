# PopulationDepthFilter

## Step 1: Population depth and SD
```{}
#01 window based depth estimaion
bedtools makewindows -g wheat.genome -w 1000000 |awk '{print "samtools depth -a -r "$1":"$2+1"-"$3" -Q 20 -f WEGA.bam|awk \047{ sum = 0; for (i = 3; i <= NF; i){ sum += $i }; mean = sum / (NF-2);squares = 0;for (i = 3; i <= NF; i) { squares += ($i - mean) ^ 2 } ;sd = sqrt(squares / (NF-3));printf("%s\t%s\t%s\t%.3f\t%.3f\n", $1,$2-1,$2,mean,sd)}\047 >"NR""$1".bed"}' >pop_depth.sh
rush -j 80 {} -i pop_depth.sh
#02 merging
for i in {1..42};do ll *${i}.bed|awk '{print $NF}' |sort -k1,1n|xargs cat |bgzip >chr${i}_popDepth.bed.gz & done
```
## Step 2: Genome High Confidence region
Format of depth.txt: depth\tSD
```{}
for i in {1..42};do nohup python popdepth.py -s 100 -i ${i}-depth.txt -o ${i}-density.txt -x 20 -y 20 & done
Usage:  -s: 100*100
        -x: x max
        -y: y max
```
choose top N% genome sites

## Step 3: Population variation filter
Format of ID.txt: depth\tSD\tchr-pos
```{}
for i in {1..42};do nohup python popdepth-ID.py -s 100 -i <(awk '{if($1 < 20 && $2 < 20)print}' ${i}-ID.txt) -o ${i}-density.txt -x 20 -y 20 2>${i}.error & done
Usage:  -s: 100*100
        -x: x max
        -y: y max
```
