#Elizabeth Cepernich
#ecepernich@gmail.com
#CMPS112 Winter 2016
#Final Project
#3/11/2016

#prints a map with an x in your position
def map(position):
     p=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]
     p[position-1]="X"
     print"You are here - X"
     print"|      | |      | |      | |      | |      |"
     print"|  ",p[0]," |=|  ",p[1]," |=|  ",p[2]," |=|  ",p[3]," |=|  ",p[4]," |"
     print"|______| |______| |______| |______| |______|"
     print"                     ||                ||"
     print"                  |      | |      | |      |"
     print"                  |  ",p[5]," |=|  ",p[6]," |=|  ",p[7]," |"
     print"                  |______| |______| |______|"
     print"                                       ||"
     print"|      | |      | |      | |               | |      |"
     print"|  ",p[11]," |=|  ",p[10]," |=|  ",p[9]," |=|      ",p[8],"      |=|  ",p[12]," |"
     print"|______| |______| |______| |_______________| |______|"
     print"                                       ||"
     print"                                    |      |"
     print"                                    |  ",p[13]," |"
     print"                                    |______|"
