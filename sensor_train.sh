#!/bin/sh

python shuffler.py sensorShuffled.data holder.data
rm sensorShuffled.data
python shuffler.py holder.data sensorShuffled.data
rm holder.data

python main.py -r sensorShuffled.data sensor_output_random.txt

python main.py -d sensorShuffled.data sensor_output_distance.txt

python main.py -v sensorShuffled.data sensor_output_diversity.txt

python main.py -p sensorShuffled.data sensor_output_probability.txt

python file_merge.py sensor_output_random.txt sensor_output_distance.txt sensor_output_diversity.txt sensor_output_probability.txt sensor_output.txt

gnuplot -persist sensor_plot.gnuplot