import time


#Functia este ca un fel de
#int main(){
# 
# }
#in .cpp
#
#Pot pune inite functii create de mine
#
#
def main():
    
    def sec(timp):

        while timp != -1:
            time.sleep(1)
            print(timp)
            timp = timp-1
    
    i = int(input("Cate secunde? "))

    sec(i)

#aici pun main()-ul

if __name__ == "__main__":
    main()
