#include <stdio.h>
#include <math.h>

#define PI 3.14159265358979323846

// Function to calculate the area of the intersection of two circles
double calculate_area() {
    double d = 1.0; // distance between centers (0,0) and (1,0)
    double r1 = 1.0; // radius of the first circle
    double r2 = 1.0; // radius of the second circle

    // Calculate the angles
    double theta1 = 2 * acos(d / (2 * r1)); // angle for the first circle
    double theta2 = 2 * acos(d / (2 * r2)); // angle for the second circle

    // Area of the segment in the first circle
    double area_segment1 = 0.5 * r1 * r1 * (theta1 - sin(theta1));
    // Area of the segment in the second circle
    double area_segment2 = 0.5 * r2 * r2 * (theta2 - sin(theta2));

    // Total area of the intersection
    return area_segment1 + area_segment2;
}

int main() {
    double area = calculate_area();
    FILE *file = fopen("output.txt", "w");
    if (file != NULL) {
        fprintf(file, "%.6f\n", area);
        fclose(file);
    } else {
        printf("Error opening file.\n");
    }
    return 0;
}

