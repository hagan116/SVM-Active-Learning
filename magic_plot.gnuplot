set terminal x11
set boxwidth 0.9 absolute
set style fill solid 0.25 border -1
set style histogram clustered gap 1
set style data histogram

set title 'F-Measure vs. Training Size' font 'Arial,14';
set xlabel 'Training Set Size (%)'
set ylabel 'F-Measure'
set xtics ('5' 0, '7.5' 1, '10' 2, '20' 3, '30' 4, '40' 5, '50' 6, '60' 7, '70' 8, '80' 9)
set key left
plot 'magic_output.txt' u 1 title "Random" lc rgb"green",\
     'magic_output.txt' u 2 title "Distance" lc rgb"red",\
     'magic_output.txt' u 3 title "Brinker" lc rgb"blue",\
     'magic_output.txt' u 4 title "Probabilistic" lc rgb"yellow"
