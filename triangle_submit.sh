#!/bin/sh
#This file is called submit.sh
#SBATCH --partition=pre		# default "univ" if not specified
#SBATCH --time=0-04:30:00		# run time in days-hh:mm:ss
#SBATCH --ntasks=40			# require 32 CPUs (CPUs)
#SBATCH --mem-per-cpu=4000		# RAM in MB (default 4GB, max 8GB)
#Make sure to change the above two lines to reflect your appropriate
# file locations for standard error and output

#Now list your executable command (or a string of them). Example:
module load compile/gcc mpi/gcc/openmpi-1.6.4
mpirun -np 40 /home/ppwilson/dagmc/bin/mcnp5.mpi i=triangle.inp
