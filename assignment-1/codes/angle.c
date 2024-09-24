#include <stdio.h>
#include <math.h>

int main() {
    // Rain falling vertically
    double rain_speed = 35.0; // m/s
    // Wind blowing horizontally (east to west)
    double wind_speed = 12.0; // m/s

    // Calculate angle (in degrees)
    double angle = atan(wind_speed / rain_speed) * (180.0 / M_PI);

    // Print angle to output.tex
    FILE *file = fopen("output.tex", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "%.2f\n", angle);
    fclose(file);

    return 0;
}
