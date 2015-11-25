#!/bin/sh

python shuffler.py ionosphereShuffle.txt holder.txt
rm ionosphereShuffle.txt
python shuffler.py holder.txt ionosphereShuffle.txt
rm holder.txt

python main.py -r ionosphereShuffle.txt ionosphere_output_random.txt

python main.py -d ionosphereShuffle.txt ionosphere_output_distance.txt

python main.py -v ionosphereShuffle.txt ionosphere_output_diversity.txt

python main.py -p ionosphereShuffle.txt ionosphere_output_probability.txt

python file_merge.py ionosphere_output_random.txt ionosphere_output_distance.txt ionosphere_output_diversity.txt ionosphere_output_probability.txt ionosphere_output.txt

gnuplot -persist ionosphere_plot.gnuplot