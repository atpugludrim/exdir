#include<stdio.h>
#include<stdlib.h>
void double_to_bits(double in){
    unsigned char *p = (unsigned char *)&in;
    int f;
    int nibble=0, idx = sizeof(double)*8-1;
    char representation[sizeof(double)*8+1];
    representation[sizeof(double)*8] = '\0';
    char hexrep[sizeof(double)*2+1];
    hexrep[sizeof(double)*2]='\0';
    printf("In memory representation of %.55f:\n",in);
    for(int i = 0; i < sizeof(double); ++i){
        nibble = 0;
        for(int j = 0; j < 8; ++j){
            f = !!((*p)&(1<<j));
            //printf("%d",f); // printing reverse order, how to correct the order?
            representation[idx--] = f + '0';
            nibble = nibble * 2 + f;
            if(j==3){
                //printf(" ");
                //printf("%x",nibble);
                nibble = 0;
            }
        }
        // printf(" ");
        //printf("%x",nibble);
        p++;
    }
    unsigned int number = 0;
    /*char s[2];
    idx = 0;*/
    for(int i = 0; i < sizeof(double)*8+1; i++){
        if(i!=0 && !(i%4)){
            printf("%x",number);
            /*
            sprintf(s,"%x",number);
            hexrep[idx++] = s[0];
            */
            number = 0;
            if(!(i%8))
                printf(" ");
        }
        number = number * 2 + (representation[i] - '0');
    }
    printf("\n");
    int ctr = 0;
    for(int i = 0; i < sizeof(double)*8; i++){
        printf("%c",representation[i]);
        if(i==0||i==11)
            printf(" ");
        if(i>11){
            ctr++;
            if(!(ctr%4))
                printf(" ");
        }
    }
    printf("\n");
    printf("\n");
    return;
}
double get_machine_eps(){
    double eps = 1.0;
    while(eps+1!=(double)1.0){
        eps = eps/(double)2.0;
    }
    return eps;
}
int main(int argc, char *argv[]){
    double in = atof(argv[1]);
    double_to_bits(in); // or just Python3 >>> import struct; ' '.join('{:x}'.format(b) for b in struct.pack('>d',in))
    printf("299792458 * 0.000015 = %.55f\n\n",299792458*0.15);
    double_to_bits(299792458*.000015);
    double_to_bits(0);
    printf("Machine epsilon is: %.55f\n",get_machine_eps());
    double_to_bits(get_machine_eps());
    if(0.1+0.2 == 0.3){
        printf("0.1+0.2 Equal 0.3\n");
    }
    else
        printf("0.1+0.2 not equal 0.3\n");
    return 0;
}
