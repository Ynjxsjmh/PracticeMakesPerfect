void replaceSpace(char *str,int length) {
    // +1 because of '\0' at the end
    char * copy = (char *)malloc(length + 1);
    strcpy(copy, str);

    int j = 0;
    for (int i = 0; i < length; i++, j++) {
        if (copy[i] == ' ') {
            str[j] = '%';
            str[j+1] = '2';
            str[j+2] = '0';
            j += 2;
        } else {
            str[j] = copy[i];
        }
    }

    free(copy);
}