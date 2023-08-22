# Yet Another Map Reduce
1. The project consists of a multinode environment containing a master node and multiple worker nodes.
The nodes are implemented as processes from multiprocess module.
2. The operations performed are:
- Read : This is done by splitting the input file and assigning the partitions to different workers.
- Write : This is done by joining the output from the reducers into a single output file.
- Map-Reduce : It performs a MapReduce job on the cluster when an input file, mapper and reducer files are given.


## Instructions to Run

1. Clone the repository
```
git clone https://github.com/Projects-RR-2022/BD1_558_594_605_612

```
2. Get into the directory as per your requirements.
3. Pass the command line arguments to specify the path for the input file, output file and pass the number of worker nodes.
```
python3 wordcount.py <INPUT FILE DIRECTORY> <OUTPUT FILE DIRECTORY> <NO OF WORKER NODES>

```
Here number of worker nodes is used to divide the input file and output_files is a temp folder where all the reducer outputs will be stored.
