import java.util.Random;
import java.util.ArrayList;

public class A
{
    protected String name;
    protected int n1;
    protected int n2;

    protected Piece(String name, int n1, int n2)
    {
        this.name = name;
        this.n1 = n1;
        this.n2 = n2;
    }

    public void M1()
    {
        if ((this.n2> this.n1) )
            {
                this.n1 =  this.n1 ;
            }
            else 
            {
                this.n1 =  this.n2;
            }
    }
    public void M2(int comp)
    {
        if ((comp > 0) )
            {
                this.n2 =  this.n2 ;
            }
            else 
            {
                this.n2 =  this.n1;
            }
    }
}



