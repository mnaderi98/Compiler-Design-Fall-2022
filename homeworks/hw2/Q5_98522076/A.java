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
        this.n1 = (this.n2> this.n1) ? this.n1 : this.n2;
    }
    public void M2(int comp)
    {
        this.n2 = (comp > 0) ? this.n2 : this.n1;
    }
}



