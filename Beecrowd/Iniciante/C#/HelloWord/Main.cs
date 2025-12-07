using System.Runtime.Intrinsics.Arm;
//Problemas do BeeCrword 1 a 5 Sorteado C#
internal class Program
{
    static void  HelloWord(){
        System.Console.WriteLine("Hello World");
    }
    static void ExtremamenteBasico(){
        int A = Convert.ToInt32(Console.ReadLine());
        int B = Convert.ToInt32(Console.ReadLine());
        int soma = A+B;
        System.Console.WriteLine("X = " +soma);
    }

    static void AreaDoCirculo(){
        double r = Convert.ToDouble(Console.ReadLine());
        double A = 3.14159*Math.Pow(r,2);
        System.Console.WriteLine($"A={A:F4}");
    }

     static void SomaSimples(){
        int A = Convert.ToInt32(Console.ReadLine());
        int B = Convert.ToInt32(Console.ReadLine());
        int soma = A+B;
        System.Console.WriteLine("SOMA = " +soma);
    }

       static void ProdutoSimples(){
        int A = Convert.ToInt32(Console.ReadLine());
        int B = Convert.ToInt32(Console.ReadLine());
        int PROD = A*B;
        System.Console.WriteLine("PROD = " +PROD);
    }





    private static void Main(string[] args)
    {
        //HelloWord();
        //ExtremamenteBasico();
        //AreaDoCirculo();
        //SomaSimples();
        //ProdutoSimples();
    }
}