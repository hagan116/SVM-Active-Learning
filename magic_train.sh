#!/bin/sh

python shuffler.py shuffled_magic04.data holder.data
rm shuffled_magic04.data
python shuffler.py holder.data shuffled_magic04.data
rm holder.data

python main.py -r shuffled_magic04.data magic_output_random.txt

python main.py -d shuffled_magic04.data magic_output_distance.txt

python main.py -v shuffled_magic04.data magic_output_diversity.txt

python main.py -p shuffled_magic04.data magic_output_probability.txt

python file_merge.py magic_output_random.txt magic_output_distance.txt magic_output_diversity.txt magic_output_probability.txt magic_output.txt

gnuplot -persist magic_plot.gnuplot