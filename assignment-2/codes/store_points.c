#include <stdio.h>

int main() {
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        perror("Unable to open file!");
        return 1;
    }
    float points[3][3] = {
        {5.0f, -4.0f, 6.0f},  // Point 1
        {8.0f, 3.0f, 8.0f},  // Point 2
        {2.0f, -11.0f, 4.0f}   // Point 3
    };
    
    for (int i = 0; i < 3; i++) {
        fprintf(file, "%f %f %f\n", points[i][0], points[i][1], points[i][2]);
    }

    fclose(file);
    printf("Points saved to output.txt\n");
    return 0;
}
