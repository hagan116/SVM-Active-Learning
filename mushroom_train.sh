#!/bin/sh

python shuffler.py mushroom.data holder.data
rm mushroom.data
python shuffler.py holder.data mushroom.data
rm holder.data

python main.py -r mushroom.data mushroom_output_random.txt

python main.py -d mushroom.data mushroom_output_distance.txt

python main.py -v mushroom.data mushroom_output_diversity.txt

python main.py -p mushroom.data mushroom_output_probability.txt

python file_merge.py mushroom_output_random.txt mushroom_output_distance.txt mushroom_output_diversity.txt mushroom_output_probability.txt mushroom_output.txt

gnuplot -persist mushroom_plot.gnuplot