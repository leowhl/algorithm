public class Hanoi {

    public static void main(String[] args){
        move(3,"x","y","z");
    }

    public static void move(int k,String x,String y,String z){
        if(k==1){
            System.out.println(x+"---->"+z);
        }else{
            move(k-1,x,z,y);
            move(1, x, y, z);
            move(k-1,y,x,z);
        }
    }
}
